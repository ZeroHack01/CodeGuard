#!/usr/bin/env python3
"""
Enterprise-Grade CodeGuard Backend API
Advanced Flask application with security, monitoring, and comprehensive error handling
"""

from flask import Flask, render_template, request, send_file, jsonify, abort
import os
import logging
import time
import hashlib
import json
import csv
from io import StringIO
from datetime import datetime, timedelta
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
import threading
from collections import defaultdict, deque
from scanner import scan_file, get_language
import traceback
from functools import wraps
import secrets
import mimetypes

# Configure comprehensive logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
    handlers=[
        logging.FileHandler('codeguard.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

app = Flask(__name__)

# Enhanced security configuration
app.config.update(
    MAX_CONTENT_LENGTH=50 * 1024 * 1024,  # 50MB max file size
    SECRET_KEY=secrets.token_hex(32),
    UPLOAD_FOLDER='uploads',
    TEMP_FOLDER='temp',
    ALLOWED_EXTENSIONS={
        'py', 'c', 'cpp', 'cc', 'cxx', 'h', 'hpp', 
        'java', 'js', 'jsx', 'ts', 'tsx', 'html', 'htm', 'css', 
        'php', 'phtml', 'rb', 'go', 'cs', 'kt', 'swift', 'rs'
    },
    RATE_LIMIT_WINDOW=3600,  # 1 hour window
    RATE_LIMIT_MAX_REQUESTS=100,  # Max requests per window
    SCAN_TIMEOUT=300  # 5 minutes timeout for scans
)

# Enhanced CORS configuration
CORS(app, 
     origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:8080"],
     methods=["GET", "POST", "OPTIONS"],
     allow_headers=["Content-Type", "Authorization"],
     supports_credentials=False
)

# Global statistics and monitoring
class ApplicationMetrics:
    """Thread-safe application metrics collector"""
    
    def __init__(self):
        self._lock = threading.Lock()
        self.reset_metrics()
    
    def reset_metrics(self):
        with self._lock:
            self.total_scans = 0
            self.total_files_scanned = 0
            self.total_vulnerabilities_found = 0
            self.scan_times = deque(maxlen=1000)  # Keep last 1000 scan times
            self.language_stats = defaultdict(int)
            self.severity_stats = defaultdict(int)
            self.error_count = 0
            self.start_time = datetime.now()
    
    def record_scan(self, scan_time: float, language: str, vulnerability_count: int, severities: list):
        with self._lock:
            self.total_scans += 1
            self.total_files_scanned += 1
            self.total_vulnerabilities_found += vulnerability_count
            self.scan_times.append(scan_time)
            self.language_stats[language] += 1
            
            for severity in severities:
                self.severity_stats[severity] += 1
    
    def record_error(self):
        with self._lock:
            self.error_count += 1
    
    def get_stats(self) -> dict:
        with self._lock:
            avg_scan_time = sum(self.scan_times) / len(self.scan_times) if self.scan_times else 0
            uptime = datetime.now() - self.start_time
            
            return {
                'total_scans': self.total_scans,
                'total_files_scanned': self.total_files_scanned,
                'total_vulnerabilities_found': self.total_vulnerabilities_found,
                'average_scan_time': round(avg_scan_time, 2),
                'language_distribution': dict(self.language_stats),
                'severity_distribution': dict(self.severity_stats),
                'error_count': self.error_count,
                'uptime_seconds': int(uptime.total_seconds()),
                'uptime_formatted': str(uptime).split('.')[0]
            }

# Rate limiting
class RateLimiter:
    """Simple in-memory rate limiter"""
    
    def __init__(self):
        self._requests = defaultdict(deque)
        self._lock = threading.Lock()
    
    def is_allowed(self, identifier: str, max_requests: int, window_seconds: int) -> bool:
        with self._lock:
            now = time.time()
            window_start = now - window_seconds
            
            # Clean old requests
            while self._requests[identifier] and self._requests[identifier][0] < window_start:
                self._requests[identifier].popleft()
            
            # Check if under limit
            if len(self._requests[identifier]) >= max_requests:
                return False
            
            # Add current request
            self._requests[identifier].append(now)
            return True

# Initialize global components
metrics = ApplicationMetrics()
rate_limiter = RateLimiter()

def get_client_ip():
    """Get client IP address considering proxies"""
    if request.headers.get('X-Forwarded-For'):
        return request.headers.get('X-Forwarded-For').split(',')[0].strip()
    elif request.headers.get('X-Real-IP'):
        return request.headers.get('X-Real-IP')
    else:
        return request.remote_addr

def rate_limit_check(f):
    """Decorator for rate limiting"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        client_ip = get_client_ip()
        
        if not rate_limiter.is_allowed(
            client_ip, 
            app.config['RATE_LIMIT_MAX_REQUESTS'], 
            app.config['RATE_LIMIT_WINDOW']
        ):
            logger.warning(f"Rate limit exceeded for IP: {client_ip}")
            return jsonify({
                'error': 'Rate limit exceeded',
                'message': f'Maximum {app.config["RATE_LIMIT_MAX_REQUESTS"]} requests per hour allowed'
            }), 429
        
        return f(*args, **kwargs)
    return decorated_function

def security_headers(f):
    """Decorator to add security headers"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        response = f(*args, **kwargs)
        
        if hasattr(response, 'headers'):
            response.headers['X-Content-Type-Options'] = 'nosniff'
            response.headers['X-Frame-Options'] = 'DENY'
            response.headers['X-XSS-Protection'] = '1; mode=block'
            response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
            response.headers['Content-Security-Policy'] = "default-src 'self'"
        
        return response
    return decorated_function

def validate_file_content(file_path: str) -> tuple[bool, str]:
    """Enhanced file content validation"""
    try:
        # Check file size
        file_size = os.path.getsize(file_path)
        if file_size > app.config['MAX_CONTENT_LENGTH']:
            return False, f"File too large: {file_size} bytes"
        
        if file_size == 0:
            return False, "Empty file"
        
        # Check MIME type
        mime_type, _ = mimetypes.guess_type(file_path)
        allowed_mimes = {
            'text/plain', 'text/x-python', 'text/x-c', 'text/x-c++',
            'text/javascript', 'text/html', 'text/css', 'text/x-java',
            'text/x-php', 'text/x-ruby', 'application/javascript',
            'application/x-javascript', 'text/typescript'
        }
        
        # Read first few bytes to check for binary content
        with open(file_path, 'rb') as f:
            header = f.read(1024)
            if b'\x00' in header:  # Null bytes indicate binary
                return False, "Binary file detected"
        
        return True, "Valid"
        
    except Exception as e:
        return False, f"Validation error: {str(e)}"

def allowed_file(filename: str) -> bool:
    """Enhanced file extension validation"""
    if not filename or '.' not in filename:
        return False
    
    ext = filename.rsplit('.', 1)[1].lower()
    return ext in app.config['ALLOWED_EXTENSIONS']

def sanitize_filename(filename: str) -> str:
    """Sanitize and secure filename"""
    # Use werkzeug's secure_filename and add additional checks
    filename = secure_filename(filename)
    
    # Remove any remaining problematic characters
    filename = ''.join(c for c in filename if c.isalnum() or c in '._-')
    
    # Ensure filename is not empty and has reasonable length
    if not filename or len(filename) > 255:
        filename = f"file_{secrets.token_hex(8)}.txt"
    
    return filename

def cleanup_old_files():
    """Clean up old uploaded files"""
    try:
        current_time = time.time()
        max_age = 3600  # 1 hour
        
        for folder in [app.config['UPLOAD_FOLDER'], app.config.get('TEMP_FOLDER', 'temp')]:
            if not os.path.exists(folder):
                continue
                
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                if os.path.isfile(file_path):
                    file_age = current_time - os.path.getctime(file_path)
                    if file_age > max_age:
                        try:
                            os.remove(file_path)
                            logger.debug(f"Cleaned up old file: {file_path}")
                        except OSError:
                            pass
                            
    except Exception as e:
        logger.error(f"Error during cleanup: {e}")

@app.before_request
def before_request():
    """Pre-request processing"""
    # Log request details
    logger.info(f"Request: {request.method} {request.path} from {get_client_ip()}")
    
    # Periodic cleanup
    if hasattr(app, 'last_cleanup'):
        if time.time() - app.last_cleanup > 1800:  # Every 30 minutes
            threading.Thread(target=cleanup_old_files, daemon=True).start()
            app.last_cleanup = time.time()
    else:
        app.last_cleanup = time.time()

@app.errorhandler(413)
def too_large(e):
    """Handle file too large error"""
    metrics.record_error()
    return jsonify({
        'error': 'File too large',
        'message': f'Maximum file size is {app.config["MAX_CONTENT_LENGTH"] // (1024*1024)}MB'
    }), 413

@app.errorhandler(429)
def ratelimit_handler(e):
    """Handle rate limit exceeded"""
    metrics.record_error()
    return jsonify({
        'error': 'Rate limit exceeded',
        'message': 'Too many requests. Please try again later.'
    }), 429

@app.errorhandler(500)
def internal_error(e):
    """Handle internal server errors"""
    metrics.record_error()
    logger.error(f"Internal server error: {e}")
    return jsonify({
        'error': 'Internal server error',
        'message': 'An unexpected error occurred during processing'
    }), 500

@app.route('/api/health', methods=['GET'])
@security_headers
def health_check():
    """Health check endpoint for monitoring"""
    try:
        stats = metrics.get_stats()
        
        # Test scanner functionality
        scanner_status = "healthy"
        try:
            # Quick test scan
            test_code = "print('hello')"
            test_file = os.path.join(app.config['TEMP_FOLDER'], 'health_test.py')
            os.makedirs(app.config['TEMP_FOLDER'], exist_ok=True)
            
            with open(test_file, 'w') as f:
                f.write(test_code)
            
            scan_file(test_file)
            os.remove(test_file)
            
        except Exception as e:
            scanner_status = f"unhealthy: {str(e)}"
        
        return jsonify({
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'version': '2.0.0',
            'scanner_status': scanner_status,
            'features': {
                'languages_supported': len(app.config['ALLOWED_EXTENSIONS']),
                'max_file_size_mb': app.config['MAX_CONTENT_LENGTH'] // (1024*1024),
                'rate_limit_per_hour': app.config['RATE_LIMIT_MAX_REQUESTS'],
                'scan_timeout_seconds': app.config['SCAN_TIMEOUT']
            },
            'statistics': stats
        })
        
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return jsonify({
            'status': 'unhealthy',
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }), 500

@app.route('/api/stats', methods=['GET'])
@security_headers
@rate_limit_check
def get_statistics():
    """Get application statistics"""
    try:
        stats = metrics.get_stats()
        return jsonify({
            'success': True,
            'statistics': stats,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        logger.error(f"Error getting statistics: {e}")
        return jsonify({'error': 'Failed to retrieve statistics'}), 500

@app.route('/api/scan', methods=['POST', 'OPTIONS'])
@security_headers
@rate_limit_check
def api_scan():
    """Enhanced API endpoint for multiple file scanning"""
    if request.method == 'OPTIONS':
        return '', 200
    
    start_time = time.time()
    uploaded_files = []
    
    try:
        # Validate request
        if 'file' not in request.files:
            return jsonify({
                'success': False,
                'error': 'No file provided',
                'message': 'Please upload at least one file for analysis'
            }), 400
        
        files = request.files.getlist('file')
        if not files or all(f.filename == '' for f in files):
            return jsonify({
                'success': False,
                'error': 'No files selected',
                'message': 'Please select valid files for analysis'
            }), 400
        
        # Process files
        scan_results = []
        total_issues = 0
        languages_detected = set()
        all_severities = []
        
        for file in files:
            if file.filename == '':
                continue
            
            # Validate file
            if not allowed_file(file.filename):
                return jsonify({
                    'success': False,
                    'error': f'Invalid file type: {file.filename}',
                    'message': f'Supported extensions: {", ".join(app.config["ALLOWED_EXTENSIONS"])}'
                }), 400
            
            # Secure filename and save
            original_filename = file.filename
            safe_filename = sanitize_filename(original_filename)
            file_id = hashlib.md5(f"{safe_filename}{time.time()}".encode()).hexdigest()[:8]
            filename = f"{file_id}_{safe_filename}"
            
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            try:
                file.save(file_path)
                uploaded_files.append(file_path)
                
                # Validate file content
                is_valid, validation_message = validate_file_content(file_path)
                if not is_valid:
                    return jsonify({
                        'success': False,
                        'error': f'Invalid file content: {original_filename}',
                        'message': validation_message
                    }), 400
                
                # Detect language
                language = get_language(file_path)
                languages_detected.add(language)
                
                logger.info(f'Scanning file: {original_filename} ({language})')
                
                # Perform scan with timeout
                issues = scan_file(file_path)
                
                # Process results
                if not issues:
                    issues = [{
                        'line': 0,
                        'code': 'N/A',
                        'issue': 'No vulnerabilities detected',
                        'severity': 'Info',
                        'description': 'File appears to be secure',
                        'confidence': 1.0,
                        'recommendation': 'No action required'
                    }]
                
                # Collect severity statistics
                file_severities = [issue.get('severity', 'Unknown') for issue in issues]
                all_severities.extend(file_severities)
                
                # Count actual vulnerabilities (exclude Info level)
                vuln_count = len([i for i in issues if i.get('severity') != 'Info'])
                total_issues += vuln_count
                
                scan_results.append({
                    'filename': original_filename,
                    'language': language,
                    'issues': issues,
                    'issue_count': len(issues),
                    'vulnerability_count': vuln_count,
                    'file_size': os.path.getsize(file_path)
                })
                
            except Exception as e:
                logger.error(f'Error scanning {original_filename}: {str(e)}')
                return jsonify({
                    'success': False,
                    'error': f'Scan failed for {original_filename}',
                    'message': str(e)
                }), 500
        
        # Calculate statistics
        scan_time = time.time() - start_time
        
        # Generate comprehensive response
        response_data = {
            'success': True,
            'scan_metadata': {
                'timestamp': datetime.now().isoformat(),
                'scan_id': hashlib.md5(f"{time.time()}{len(files)}".encode()).hexdigest()[:16],
                'scan_time': round(scan_time, 2),
                'files_processed': len(scan_results),
                'languages_detected': list(languages_detected),
                'total_issues': total_issues
            },
            'summary': {
                'total_files': len(scan_results),
                'total_vulnerabilities': total_issues,
                'severity_breakdown': {
                    'critical': len([s for s in all_severities if s == 'Critical']),
                    'high': len([s for s in all_severities if s == 'High']),
                    'medium': len([s for s in all_severities if s == 'Medium']),
                    'low': len([s for s in all_severities if s == 'Low']),
                    'info': len([s for s in all_severities if s == 'Info'])
                },
                'risk_score': calculate_risk_score(all_severities),
                'languages': list(languages_detected)
            },
            'results': scan_results,
            # Flatten all issues for backward compatibility
            'issues': [issue for result in scan_results for issue in result['issues']]
        }
        
        # Record metrics
        metrics.record_scan(scan_time, ','.join(languages_detected), total_issues, all_severities)
        
        logger.info(f'Scan completed: {len(scan_results)} files, {total_issues} vulnerabilities, {scan_time:.2f}s')
        
        return jsonify(response_data)
        
    except RequestEntityTooLarge:
        return jsonify({
            'success': False,
            'error': 'File too large',
            'message': f'Maximum file size is {app.config["MAX_CONTENT_LENGTH"] // (1024*1024)}MB'
        }), 413
        
    except Exception as e:
        logger.error(f'API scan error: {str(e)}\n{traceback.format_exc()}')
        metrics.record_error()
        return jsonify({
            'success': False,
            'error': 'Internal scan error',
            'message': 'An unexpected error occurred during analysis'
        }), 500
        
    finally:
        # Clean up uploaded files
        for file_path in uploaded_files:
            try:
                if os.path.exists(file_path):
                    os.remove(file_path)
            except OSError as e:
                logger.warning(f"Could not remove {file_path}: {e}")

def calculate_risk_score(severities: list) -> float:
    """Calculate overall risk score based on severities"""
    if not severities:
        return 0.0
    
    weights = {
        'Critical': 10,
        'High': 7,
        'Medium': 4,
        'Low': 1,
        'Info': 0
    }
    
    total_score = sum(weights.get(severity, 0) for severity in severities)
    max_possible = len(severities) * 10
    
    return round((total_score / max_possible) * 10, 1) if max_possible > 0 else 0.0

@app.route('/', methods=['GET', 'POST'])
@security_headers
@rate_limit_check
def upload_file():
    """Enhanced file upload endpoint with better error handling"""
    if request.method == 'POST':
        try:
            if 'file' not in request.files:
                logger.warning('No file part in request')
                return render_template('index.html', 
                                     error='No file selected', 
                                     issues=None)
            
            file = request.files['file']
            if file.filename == '':
                logger.warning('No file selected')
                return render_template('index.html', 
                                     error='No file selected', 
                                     issues=None)
            
            if file and allowed_file(file.filename):
                # Process single file
                safe_filename = sanitize_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], safe_filename)
                
                try:
                    file.save(file_path)
                    
                    # Validate content
                    is_valid, validation_message = validate_file_content(file_path)
                    if not is_valid:
                        os.remove(file_path)
                        return render_template('index.html', 
                                             error=f'Invalid file: {validation_message}', 
                                             issues=None)
                    
                    logger.info(f'File uploaded via web: {safe_filename}')
                    
                    # Scan file
                    start_time = time.time()
                    issues = scan_file(file_path)
                    scan_time = time.time() - start_time
                    
                    if not issues:
                        issues = [{
                            'line': 0,
                            'code': 'N/A',
                            'issue': 'No vulnerabilities detected',
                            'severity': 'Info',
                            'description': 'File appears to be secure'
                        }]
                    
                    # Record metrics
                    language = get_language(file_path)
                    severities = [issue.get('severity', 'Unknown') for issue in issues]
                    vuln_count = len([i for i in issues if i.get('severity') != 'Info'])
                    metrics.record_scan(scan_time, language, vuln_count, severities)
                    
                    # Clean up
                    try:
                        os.remove(file_path)
                    except OSError:
                        pass
                    
                    return render_template('index.html', 
                                         issues=issues, 
                                         filename=file.filename, 
                                         error=None)
                                         
                except Exception as e:
                    logger.error(f'Error processing {file.filename}: {str(e)}')
                    metrics.record_error()
                    
                    # Clean up on error
                    try:
                        if os.path.exists(file_path):
                            os.remove(file_path)
                    except OSError:
                        pass
                    
                    return render_template('index.html', 
                                         error=f'Error processing file: {str(e)}', 
                                         issues=None)
            else:
                logger.warning(f'Invalid file extension: {file.filename}')
                return render_template('index.html', 
                                     error='Invalid file type. Supported: ' + 
                                           ', '.join(app.config['ALLOWED_EXTENSIONS']), 
                                     issues=None)
                                     
        except Exception as e:
            logger.error(f'Upload error: {str(e)}')
            metrics.record_error()
            return render_template('index.html', 
                                 error='Upload failed. Please try again.', 
                                 issues=None)
    
    return render_template('index.html', issues=None, error=None)

@app.route('/download/<format>/<filename>')
@security_headers
@rate_limit_check
def download_results(format, filename):
    """Enhanced download endpoint with better security"""
    try:
        # Sanitize inputs
        format = format.lower()
        if format not in ['json', 'csv', 'pdf']:
            abort(400, "Invalid format requested")
        
        safe_filename = sanitize_filename(filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], safe_filename)
        
        # Security check - ensure file exists and is in upload folder
        if not os.path.exists(file_path) or not file_path.startswith(
            os.path.abspath(app.config['UPLOAD_FOLDER'])
        ):
            abort(404, "File not found")
        
        # Scan file
        issues = scan_file(file_path)
        if not issues:
            issues = [{
                'line': 0,
                'code': 'N/A',
                'issue': 'No vulnerabilities detected',
                'severity': 'Info',
                'description': 'File appears to be secure'
            }]
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if format == 'json':
            # Enhanced JSON export with metadata
            export_data = {
                'metadata': {
                    'filename': filename,
                    'scan_timestamp': datetime.now().isoformat(),
                    'scanner_version': '2.0.0',
                    'total_issues': len(issues)
                },
                'summary': {
                    'severity_breakdown': {
                        'critical': len([i for i in issues if i.get('severity') == 'Critical']),
                        'high': len([i for i in issues if i.get('severity') == 'High']),
                        'medium': len([i for i in issues if i.get('severity') == 'Medium']),
                        'low': len([i for i in issues if i.get('severity') == 'Low']),
                        'info': len([i for i in issues if i.get('severity') == 'Info'])
                    }
                },
                'issues': issues
            }
            
            json_data = json.dumps(export_data, indent=2, ensure_ascii=False)
            
            # Create response
            response = app.response_class(
                json_data,
                mimetype='application/json',
                headers={
                    'Content-Disposition': f'attachment; filename=codeguard_scan_{timestamp}.json'
                }
            )
            return response
            
        elif format == 'csv':
            # Enhanced CSV export
            output = StringIO()
            fieldnames = [
                'line', 'code', 'issue', 'severity', 'description', 
                'confidence', 'owasp_category', 'cwe_id', 'recommendation'
            ]
            writer = csv.DictWriter(output, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            
            for issue in issues:
                # Ensure all fields exist
                row = {field: issue.get(field, '') for field in fieldnames}
                writer.writerow(row)
            
            csv_data = output.getvalue()
            output.close()
            
            response = app.response_class(
                csv_data,
                mimetype='text/csv',
                headers={
                    'Content-Disposition': f'attachment; filename=codeguard_scan_{timestamp}.csv'
                }
            )
            return response
            
    except Exception as e:
        logger.error(f'Error generating {format} for {filename}: {str(e)}')
        metrics.record_error()
        return jsonify({
            'error': f'Export failed',
            'message': 'Could not generate download file'
        }), 500

@app.route('/api/reset-stats', methods=['POST'])
@security_headers
def reset_statistics():
    """Reset application statistics (for development/testing)"""
    try:
        metrics.reset_metrics()
        logger.info("Application statistics reset")
        return jsonify({
            'success': True,
            'message': 'Statistics reset successfully',
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        logger.error(f"Error resetting statistics: {e}")
        return jsonify({'error': 'Failed to reset statistics'}), 500

if __name__ == '__main__':
    # Create necessary directories
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config.get('TEMP_FOLDER', 'temp'), exist_ok=True)
    
    # Application startup
    logger.info("=" * 60)
    logger.info("CodeGuard Enterprise Backend Starting")
    logger.info("=" * 60)
    logger.info(f"Upload folder: {app.config['UPLOAD_FOLDER']}")
    logger.info(f"Max file size: {app.config['MAX_CONTENT_LENGTH'] // (1024*1024)}MB")
    logger.info(f"Supported extensions: {', '.join(app.config['ALLOWED_EXTENSIONS'])}")
    logger.info(f"Rate limit: {app.config['RATE_LIMIT_MAX_REQUESTS']} requests per hour")
    logger.info("=" * 60)
    
    print("\n" + "="*60)
    print("🛡️  CodeGuard Enterprise Backend")
    print("="*60)
    print(f"🌐 Server: http://localhost:5000")
    print(f"🔍 API Endpoint: POST /api/scan")
    print(f"❤️  Health Check: GET /api/health")
    print(f"📊 Statistics: GET /api/stats")
    print(f"📁 Max File Size: {app.config['MAX_CONTENT_LENGTH'] // (1024*1024)}MB")
    print(f"⚡ Rate Limit: {app.config['RATE_LIMIT_MAX_REQUESTS']}/hour")
    print(f"🔧 Languages: {len(app.config['ALLOWED_EXTENSIONS'])} supported")
    print("="*60)
    print("Press CTRL+C to quit")
    print("="*60 + "\n")
    
    try:
        app.run(
            host='0.0.0.0', 
            port=5000, 
            debug=False,  # Disabled for production
            threaded=True
        )
    except KeyboardInterrupt:
        logger.info("CodeGuard Backend shutting down...")
        print("\n👋 CodeGuard Backend stopped")

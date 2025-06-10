from flask import Flask, render_template, request, send_file, jsonify
import os
import logging
from scanner import scan_file
import json
import csv
from io import StringIO
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for web interface

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'py', 'c', 'cpp', 'java', 'js', 'html', 'css', 'php', 'rb', 'go', 'ts', 'cs', 'kt', 'swift'}

# Configure logging
logging.basicConfig(
    filename='codeguard.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/scan', methods=['POST'])
def api_scan():
    """API endpoint for web interface"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type'}), 400
        
        # Save and scan file
        filename = file.filename
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        
        logging.info(f'API scan for file: {filename}')
        issues = scan_file(file_path)
        
        if not issues:
            issues = [{'line': 0, 'code': 'N/A', 'issue': 'No vulnerabilities detected', 'severity': 'Info'}]
        
        # Clean up uploaded file
        try:
            os.remove(file_path)
        except:
            pass
        
        return jsonify({
            'success': True,
            'filename': filename,
            'issues': issues,
            'total_issues': len(issues)
        })
        
    except Exception as e:
        logging.error(f'API scan error: {str(e)}')
        return jsonify({'error': f'Scan failed: {str(e)}'}), 500

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    """Original endpoint for backward compatibility"""
    if request.method == 'POST':
        if 'file' not in request.files:
            logging.error('No file part in request')
            return render_template('index.html', error='No file selected', issues=None)
        file = request.files['file']
        if file.filename == '':
            logging.error('No file selected')
            return render_template('index.html', error='No file selected', issues=None)
        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            try:
                file.save(file_path)
                logging.info(f'File uploaded: {filename}')
                issues = scan_file(file_path)
                if not issues:
                    issues = [{'line': 0, 'code': 'N/A', 'issue': 'No vulnerabilities detected', 'severity': 'Info'}]
                return render_template('index.html', issues=issues, filename=filename, error=None)
            except Exception as e:
                logging.error(f'Error processing {filename}: {str(e)}')
                return render_template('index.html', error=f'Error processing file: {str(e)}', issues=None)
        else:
            logging.error(f'Invalid file extension: {file.filename}')
            return render_template('index.html', error='Invalid file type', issues=None)
    return render_template('index.html', issues=None, error=None)

@app.route('/download/<format>/<filename>')
def download_results(format, filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    try:
        issues = scan_file(file_path)
        if not issues:
            issues = [{'line': 0, 'code': 'N/A', 'issue': 'No vulnerabilities detected', 'severity': 'Info'}]
        
        if format == 'json':
            json_data = json.dumps(issues, indent=2)
            return send_file(
                StringIO(json_data),
                mimetype='application/json',
                as_attachment=True,
                download_name=f'{filename}_scan_results.json'
            )
        elif format == 'csv':
            output = StringIO()
            writer = csv.DictWriter(output, fieldnames=['line', 'code', 'issue', 'severity'])
            writer.writeheader()
            writer.writerows(issues)
            output.seek(0)
            return send_file(
                StringIO(output.getvalue()),
                mimetype='text/csv',
                as_attachment=True,
                download_name=f'{filename}_scan_results.csv'
            )
    except Exception as e:
        logging.error(f'Error generating {format} for {filename}: {str(e)}')
        return render_template('index.html', error=f'Error generating {format}: {str(e)}', issues=None)

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    print(" * CodeGuard Backend running on http://localhost:5000")
    print(" * API endpoint: POST /api/scan")
    print(" * Press CTRL+C to quit")
    app.run(host='0.0.0.0', port=5000, debug=True)
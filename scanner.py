import re
import logging
import esprima
from bs4 import BeautifulSoup
import subprocess
import os
import hashlib

logging.basicConfig(
    filename='codeguard.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Vulnerability patterns with detailed descriptions
PATTERNS = {
    'python': [
        {
            'pattern': r'\b(password|pwd|secret|key|token|api_key|auth)\s*=\s*[\'"][^\'"]{3,}[\'"]',
            'issue': 'Hardcoded Credentials',
            'severity': 'Critical',
            'description': 'Sensitive credentials found in source code'
        },
        {
            'pattern': r'\beval\s*\(',
            'issue': 'Code Injection',
            'severity': 'Critical',
            'description': 'Dynamic code execution can lead to arbitrary code execution'
        },
        {
            'pattern': r'\bexec\s*\(',
            'issue': 'Code Execution',
            'severity': 'Critical',
            'description': 'Direct code execution detected'
        },
        {
            'pattern': r'\bos\.system\s*\(',
            'issue': 'Command Injection',
            'severity': 'High',
            'description': 'System command execution without proper sanitization'
        },
        {
            'pattern': r'\bsubprocess\.call\s*\([^,)]*\+',
            'issue': 'Command Injection',
            'severity': 'High',
            'description': 'Subprocess call with string concatenation'
        },
        {
            'pattern': r'\bpickle\.loads?\s*\(',
            'issue': 'Insecure Deserialization',
            'severity': 'High',
            'description': 'Pickle deserialization can execute arbitrary code'
        },
        {
            'pattern': r'sql.*?[\'"].*?\+.*?[\'"]',
            'issue': 'SQL Injection',
            'severity': 'High',
            'description': 'SQL query with string concatenation detected'
        },
        {
            'pattern': r'\brandom\.random\(\)',
            'issue': 'Weak Random Number Generation',
            'severity': 'Medium',
            'description': 'Use secrets module for cryptographic operations'
        },
        {
            'pattern': r'debug\s*=\s*True',
            'issue': 'Debug Mode Enabled',
            'severity': 'Medium',
            'description': 'Debug mode should be disabled in production'
        },
        {
            'pattern': r'ssl_verify\s*=\s*False',
            'issue': 'SSL Verification Disabled',
            'severity': 'High',
            'description': 'SSL certificate verification is disabled'
        }
    ],
    'javascript': [
        {
            'pattern': r'\beval\s*\(',
            'issue': 'Code Injection',
            'severity': 'Critical',
            'description': 'eval() can execute arbitrary JavaScript code'
        },
        {
            'pattern': r'\.innerHTML\s*=.*?\+',
            'issue': 'XSS Vulnerability',
            'severity': 'High',
            'description': 'innerHTML with concatenation can lead to XSS'
        },
        {
            'pattern': r'document\.write\s*\(',
            'issue': 'XSS Vulnerability',
            'severity': 'High',
            'description': 'document.write can be exploited for XSS attacks'
        },
        {
            'pattern': r'window\.location\s*=.*?\+',
            'issue': 'Open Redirect',
            'severity': 'Medium',
            'description': 'URL redirection with user input'
        },
        {
            'pattern': r'\$\([\'"][^\'")]*[\'"].*?\+',
            'issue': 'DOM-based XSS',
            'severity': 'High',
            'description': 'jQuery selector with concatenated user input'
        },
        {
            'pattern': r'localStorage\.setItem.*?[\'"][^\'"]*[\'"].*?\+',
            'issue': 'Client-side Data Exposure',
            'severity': 'Medium',
            'description': 'Sensitive data stored in localStorage'
        },
        {
            'pattern': r'Math\.random\(\)',
            'issue': 'Weak Random Number Generation',
            'severity': 'Low',
            'description': 'Math.random() is not cryptographically secure'
        }
    ],
    'typescript': [
        {
            'pattern': r'\beval\s*\(',
            'issue': 'Code Injection',
            'severity': 'Critical',
            'description': 'eval() can execute arbitrary code'
        },
        {
            'pattern': r'any\s+\w+.*?=.*?document\.',
            'issue': 'Type Safety Issue',
            'severity': 'Medium',
            'description': 'Using any type with DOM manipulation'
        }
    ],
    'c': [
        {
            'pattern': r'\bgets\s*\(',
            'issue': 'Buffer Overflow',
            'severity': 'Critical',
            'description': 'gets() is unsafe and can cause buffer overflow'
        },
        {
            'pattern': r'\bstrcpy\s*\(',
            'issue': 'Buffer Overflow',
            'severity': 'High',
            'description': 'strcpy() does not check buffer boundaries'
        },
        {
            'pattern': r'\bstrcat\s*\(',
            'issue': 'Buffer Overflow',
            'severity': 'High',
            'description': 'strcat() can cause buffer overflow'
        },
        {
            'pattern': r'\bsprintf\s*\(',
            'issue': 'Buffer Overflow',
            'severity': 'High',
            'description': 'sprintf() does not check buffer size'
        },
        {
            'pattern': r'\bsystem\s*\(',
            'issue': 'Command Injection',
            'severity': 'Critical',
            'description': 'system() can execute arbitrary commands'
        },
        {
            'pattern': r'\bmalloc\s*\([^)]*\)\s*;(?!\s*if)',
            'issue': 'Memory Management',
            'severity': 'Medium',
            'description': 'malloc() return value not checked'
        }
    ],
    'cpp': [
        {
            'pattern': r'\bgets\s*\(',
            'issue': 'Buffer Overflow',
            'severity': 'Critical',
            'description': 'gets() is unsafe and deprecated'
        },
        {
            'pattern': r'\bstrcpy\s*\(',
            'issue': 'Buffer Overflow',
            'severity': 'High',
            'description': 'Use strncpy() or std::string instead'
        },
        {
            'pattern': r'\bsystem\s*\(',
            'issue': 'Command Injection',
            'severity': 'Critical',
            'description': 'system() can execute arbitrary shell commands'
        },
        {
            'pattern': r'\bstrcat\s*\(',
            'issue': 'Buffer Overflow',
            'severity': 'High',
            'description': 'strcat() can cause buffer overflow'
        },
        {
            'pattern': r'\bsprintf\s*\(',
            'issue': 'Buffer Overflow',
            'severity': 'High',
            'description': 'sprintf() does not check buffer size'
        },
        {
            'pattern': r'\bdelete\s+\w+;.*?\bdelete\s+\w+;',
            'issue': 'Double Free',
            'severity': 'High',
            'description': 'Potential double delete detected'
        }
    ],
    'java': [
        {
            'pattern': r'\bRuntime\.getRuntime\(\)\.exec\s*\(',
            'issue': 'Command Injection',
            'severity': 'Critical',
            'description': 'Runtime.exec() can execute system commands'
        },
        {
            'pattern': r'\bClass\.forName\s*\(',
            'issue': 'Reflection Injection',
            'severity': 'High',
            'description': 'Dynamic class loading can be dangerous'
        },
        {
            'pattern': r'new\s+File\s*\([^)]*\+',
            'issue': 'Path Traversal',
            'severity': 'High',
            'description': 'File path with concatenation can lead to path traversal'
        },
        {
            'pattern': r'Math\.random\(\)',
            'issue': 'Weak Random Number Generation',
            'severity': 'Medium',
            'description': 'Use SecureRandom for cryptographic operations'
        }
    ],
    'php': [
        {
            'pattern': r'\beval\s*\(',
            'issue': 'Code Injection',
            'severity': 'Critical',
            'description': 'eval() executes arbitrary PHP code'
        },
        {
            'pattern': r'\bexec\s*\(',
            'issue': 'Command Execution',
            'severity': 'Critical',
            'description': 'exec() can execute system commands'
        },
        {
            'pattern': r'\bshell_exec\s*\(',
            'issue': 'Command Execution',
            'severity': 'Critical',
            'description': 'shell_exec() executes shell commands'
        },
        {
            'pattern': r'\$_GET\[.*?\].*?echo',
            'issue': 'XSS Vulnerability',
            'severity': 'High',
            'description': 'Direct output of GET parameter'
        },
        {
            'pattern': r'mysql_query.*?\$_',
            'issue': 'SQL Injection',
            'severity': 'Critical',
            'description': 'SQL query with user input'
        },
        {
            'pattern': r'md5\s*\(\s*\$',
            'issue': 'Weak Hash Algorithm',
            'severity': 'Medium',
            'description': 'MD5 is cryptographically broken'
        }
    ],
    'ruby': [
        {
            'pattern': r'\beval\s*\(',
            'issue': 'Code Injection',
            'severity': 'Critical',
            'description': 'eval() can execute arbitrary Ruby code'
        },
        {
            'pattern': r'\bsystem\s*\(',
            'issue': 'Command Injection',
            'severity': 'Critical',
            'description': 'system() executes shell commands'
        },
        {
            'pattern': r'`[^`]*\#\{',
            'issue': 'Command Injection',
            'severity': 'High',
            'description': 'Shell command with interpolation'
        }
    ],
    'go': [
        {
            'pattern': r'\bos/exec\.Command\s*\(',
            'issue': 'Command Execution',
            'severity': 'High',
            'description': 'Command execution detected'
        },
        {
            'pattern': r'\bunsafe\.',
            'issue': 'Unsafe Operations',
            'severity': 'High',
            'description': 'Unsafe package bypasses type safety'
        },
        {
            'pattern': r'sql\.DB\.Query.*?\+',
            'issue': 'SQL Injection',
            'severity': 'High',
            'description': 'SQL query with string concatenation'
        }
    ],
    'html': [
        {
            'pattern': r'<script[^>]*src=[\'"][^\'")]*[\'"][^>]*>',
            'issue': 'External Script Loading',
            'severity': 'Medium',
            'description': 'Loading external JavaScript resources'
        },
        {
            'pattern': r'<iframe[^>]*src=[\'"][^\'")]*[\'"]',
            'issue': 'Frame Injection',
            'severity': 'Medium',
            'description': 'iframe with external source'
        },
        {
            'pattern': r'javascript:',
            'issue': 'JavaScript Protocol',
            'severity': 'High',
            'description': 'javascript: protocol can lead to XSS'
        }
    ]
}

def get_language(file_path):
    """Detect programming language from file extension"""
    ext = file_path.rsplit('.', 1)[1].lower() if '.' in file_path else ''
    language_map = {
        'py': 'python',
        'c': 'c',
        'cpp': 'cpp',
        'cc': 'cpp',
        'cxx': 'cpp',
        'js': 'javascript',
        'jsx': 'javascript',
        'ts': 'typescript',
        'tsx': 'typescript',
        'html': 'html',
        'htm': 'html',
        'java': 'java',
        'php': 'php',
        'phtml': 'php',
        'rb': 'ruby',
        'go': 'go',
        'cs': 'csharp',
        'kt': 'kotlin',
        'swift': 'swift',
    }
    return language_map.get(ext, 'unknown')

def scan_patterns(content, file_path, language):
    """Pattern-based vulnerability scanning"""
    issues = []
    patterns = PATTERNS.get(language, [])
    
    for pattern_info in patterns:
        pattern = pattern_info['pattern']
        issue_type = pattern_info['issue']
        severity = pattern_info['severity']
        description = pattern_info['description']
        
        for line_num, line in enumerate(content.splitlines(), 1):
            # Don't skip lines with comments entirely, just check the code part
            code_part = line
            if language in ['c', 'cpp']:
                # For C/C++, check the part before // comment
                code_part = line.split('//')[0].strip()
            elif language in ['python', 'ruby']:
                # For Python/Ruby, check the part before # comment  
                code_part = line.split('#')[0].strip()
                
            # Skip if the entire line is just a comment
            if not code_part:
                continue
                
            if re.search(pattern, code_part, re.IGNORECASE):
                issues.append({
                    'line': line_num,
                    'code': line.strip(),
                    'issue': issue_type,
                    'severity': severity,
                    'description': description
                })
                logging.debug(f"Found {issue_type} in {file_path} at line {line_num}: {code_part}")
    
    return issues

def scan_javascript_ast(content, file_path):
    """JavaScript AST analysis"""
    issues = []
    try:
        ast = esprima.parseScript(content, {'loc': True, 'range': True})
        
        def traverse(node, parent=None):
            if not isinstance(node, dict):
                return
                
            node_type = node.get('type')
            
            # Detect dangerous function calls
            if node_type == 'CallExpression':
                callee = node.get('callee', {})
                if callee.get('name') == 'eval':
                    line_num = node.get('loc', {}).get('start', {}).get('line', 0)
                    issues.append({
                        'line': line_num,
                        'code': content.splitlines()[line_num - 1].strip() if line_num > 0 else 'N/A',
                        'issue': 'eval() Function Call',
                        'severity': 'Critical',
                        'description': 'eval() can execute arbitrary JavaScript code'
                    })
                    
            # Detect innerHTML assignments
            elif node_type == 'AssignmentExpression':
                left = node.get('left', {})
                if (left.get('type') == 'MemberExpression' and 
                    left.get('property', {}).get('name') == 'innerHTML'):
                    line_num = node.get('loc', {}).get('start', {}).get('line', 0)
                    issues.append({
                        'line': line_num,
                        'code': content.splitlines()[line_num - 1].strip() if line_num > 0 else 'N/A',
                        'issue': 'innerHTML Assignment',
                        'severity': 'High',
                        'description': 'innerHTML can lead to XSS vulnerabilities'
                    })
            
            # Recursively traverse child nodes
            for key, value in node.items():
                if isinstance(value, dict):
                    traverse(value, node)
                elif isinstance(value, list):
                    for item in value:
                        if isinstance(item, dict):
                            traverse(item, node)
        
        traverse(ast)
        
    except Exception as e:
        issues.append({
            'line': 0,
            'code': 'N/A',
            'issue': f'JavaScript Parse Error: {str(e)}',
            'severity': 'Low',
            'description': 'Could not parse JavaScript syntax'
        })
        logging.error(f"JS AST parsing error in {file_path}: {str(e)}")
    
    return issues

def scan_html_content(content, file_path):
    """HTML security scanning"""
    issues = []
    
    try:
        soup = BeautifulSoup(content, 'html.parser')
        
        # Check for inline scripts
        scripts = soup.find_all('script')
        for i, script in enumerate(scripts):
            if script.string:
                script_issues = scan_javascript_ast(script.string, f"{file_path}:script-{i}")
                issues.extend(script_issues)
        
        # Check for dangerous attributes
        for tag in soup.find_all():
            # Check for javascript: protocols
            for attr in ['href', 'src', 'action']:
                if tag.get(attr, '').strip().lower().startswith('javascript:'):
                    issues.append({
                        'line': 0,
                        'code': str(tag),
                        'issue': 'JavaScript Protocol Usage',
                        'severity': 'High',
                        'description': 'javascript: protocol can lead to XSS'
                    })
            
            # Check for event handlers
            event_attrs = [attr for attr in tag.attrs if attr.startswith('on')]
            for event_attr in event_attrs:
                issues.append({
                    'line': 0,
                    'code': str(tag),
                    'issue': 'Inline Event Handler',
                    'severity': 'Medium',
                    'description': f'Inline {event_attr} event handler detected'
                })
                
    except Exception as e:
        logging.error(f"HTML parsing error in {file_path}: {str(e)}")
    
    return issues

def scan_file(file_path):
    """Main file scanning function with analysis"""
    language = get_language(file_path)
    logging.info(f"Starting scan for {file_path} as {language}")
    
    # Read file content
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='latin-1') as file:
                content = file.read()
            logging.warning(f"Used latin-1 encoding for {file_path}")
        except Exception as e:
            logging.error(f"Error reading {file_path}: {str(e)}")
            return [{'line': 0, 'code': 'N/A', 'issue': f'File Read Error: {str(e)}', 'severity': 'High', 'description': 'Could not read file'}]
    except Exception as e:
        logging.error(f"Error reading {file_path}: {str(e)}")
        return [{'line': 0, 'code': 'N/A', 'issue': f'File Read Error: {str(e)}', 'severity': 'High', 'description': 'Could not read file'}]

    issues = []
    
    # Pattern-based scanning for all languages
    pattern_issues = scan_patterns(content, file_path, language)
    issues.extend(pattern_issues)
    
    # Language-specific scanning
    if language == 'javascript' or language == 'typescript':
        ast_issues = scan_javascript_ast(content, file_path)
        issues.extend(ast_issues)
    elif language == 'html':
        html_issues = scan_html_content(content, file_path)
        issues.extend(html_issues)
    elif language in ['c', 'cpp']:
        # Try to use static analysis tools if available
        try:
            result = subprocess.run(['cppcheck', '--enable=all', '--suppress=missingIncludeSystem', 
                                   '--quiet', file_path], capture_output=True, text=True, timeout=30)
            for line in result.stderr.splitlines():
                if any(severity in line.lower() for severity in ['error', 'warning']):
                    match = re.search(r':(\d+):.*?\[(.*?)\]', line)
                    if match:
                        line_num = int(match.group(1))
                        issue = match.group(2)
                        issues.append({
                            'line': line_num,
                            'code': content.splitlines()[line_num - 1].strip() if line_num <= len(content.splitlines()) else 'N/A',
                            'issue': f'Static Analysis: {issue}',
                            'severity': 'High' if 'error' in line.lower() else 'Medium',
                            'description': 'Issue found by static analysis tool'
                        })
        except subprocess.SubprocessError:
            logging.warning(f"Cppcheck not available for {file_path}")
    
    # Remove duplicates based on line and issue type
    unique_issues = []
    seen = set()
    for issue in issues:
        key = (issue['line'], issue['issue'])
        if key not in seen:
            seen.add(key)
            unique_issues.append(issue)
    
    if not unique_issues:
        logging.info(f"No vulnerabilities found in {file_path}")
        unique_issues.append({
            'line': 0,
            'code': 'N/A',
            'issue': 'No vulnerabilities detected',
            'severity': 'Info',
            'description': 'File appears to be secure'
        })
    
    logging.info(f"Scan completed for {file_path}: {len(unique_issues)} issues found")
    return unique_issues

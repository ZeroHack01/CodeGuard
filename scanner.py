#!/usr/bin/env python3
"""
Enterprise-Grade CodeGuard Security Scanner
Advanced static code analysis with comprehensive vulnerability detection
"""

import re
import logging
import esprima
from bs4 import BeautifulSoup
import subprocess
import os
import hashlib
import json
from typing import Dict, List, Any, Tuple, Optional
from dataclasses import dataclass, asdict
from datetime import datetime
import secrets
import ast

# Configure enhanced logging
logging.basicConfig(
    filename='codeguard.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
)

@dataclass
class Vulnerability:
    """Enhanced vulnerability data structure"""
    line: int
    code: str
    issue: str
    severity: str
    description: str
    confidence: float = 0.0
    owasp_category: str = ""
    cwe_id: str = ""
    recommendation: str = ""
    category: str = ""

class EnterpriseSecurityScanner:
    """Enterprise-grade security scanner with advanced detection capabilities"""
    
    def __init__(self):
        self.patterns = self._initialize_advanced_patterns()
        self.language_analyzers = self._initialize_language_analyzers()
        self.framework_patterns = self._initialize_framework_patterns()
        self.false_positive_filters = self._initialize_false_positive_filters()
        
    def _initialize_advanced_patterns(self) -> Dict[str, List[Dict]]:
        """Initialize comprehensive vulnerability patterns with enterprise-grade detection"""
        return {
            'python': [
                # Code Injection Patterns
                {
                    'pattern': r'\beval\s*\([^)]*[a-zA-Z_$][a-zA-Z0-9_$]*',
                    'issue': 'Code Injection via eval()',
                    'severity': 'Critical',
                    'description': 'Dynamic code execution using eval() with user input',
                    'confidence': 0.9,
                    'owasp_category': 'A03:2021-Injection',
                    'cwe_id': 'CWE-95',
                    'recommendation': 'Replace eval() with safe alternatives like ast.literal_eval() for data parsing',
                    'category': 'code_injection'
                },
                {
                    'pattern': r'\bexec\s*\([^)]*[a-zA-Z_$][a-zA-Z0-9_$]*',
                    'issue': 'Code Execution via exec()',
                    'severity': 'Critical',
                    'description': 'Direct code execution with user input detected',
                    'confidence': 0.9,
                    'owasp_category': 'A03:2021-Injection',
                    'cwe_id': 'CWE-95',
                    'recommendation': 'Avoid exec() entirely. Use specific APIs for required functionality',
                    'category': 'code_injection'
                },
                
                # SQL Injection Patterns
                {
                    'pattern': r'(cursor|connection)\.execute\s*\([^)]*[\'\"]\s*SELECT.*[\'\"]\s*%',
                    'issue': 'SQL Injection Vulnerability',
                    'severity': 'Critical',
                    'description': 'SQL query with string formatting vulnerability',
                    'confidence': 0.9,
                    'owasp_category': 'A03:2021-Injection',
                    'cwe_id': 'CWE-89',
                    'recommendation': 'Use parameterized queries: cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))',
                    'category': 'sql_injection'
                },
                {
                    'pattern': r'f[\'\"]\s*SELECT\s+.*\s+FROM\s+.*\s+WHERE\s+.*\{[^}]*\}',
                    'issue': 'SQL Injection via F-string',
                    'severity': 'Critical',
                    'description': 'SQL injection via f-string formatting',
                    'confidence': 0.9,
                    'owasp_category': 'A03:2021-Injection',
                    'cwe_id': 'CWE-89',
                    'recommendation': 'Use parameterized queries instead of f-string formatting',
                    'category': 'sql_injection'
                },
                
                # Command Injection Patterns
                {
                    'pattern': r'\bos\.system\s*\([^)]*[a-zA-Z_$][a-zA-Z0-9_$]*',
                    'issue': 'Command Injection Vulnerability',
                    'severity': 'Critical',
                    'description': 'OS command execution with user input',
                    'confidence': 0.9,
                    'owasp_category': 'A03:2021-Injection',
                    'cwe_id': 'CWE-78',
                    'recommendation': 'Use subprocess with shell=False and validate inputs: subprocess.run(["ls", user_path], shell=False)',
                    'category': 'command_injection'
                },
                {
                    'pattern': r'\bsubprocess\.(call|run|Popen)\s*\([^)]*shell\s*=\s*True',
                    'issue': 'Shell Injection Risk',
                    'severity': 'High',
                    'description': 'Subprocess with shell=True can lead to command injection',
                    'confidence': 0.8,
                    'owasp_category': 'A03:2021-Injection',
                    'cwe_id': 'CWE-78',
                    'recommendation': 'Set shell=False and pass command as list: subprocess.run(["command", "arg"], shell=False)',
                    'category': 'command_injection'
                },
                
                # Credential Exposure
                {
                    'pattern': r'\b(password|pwd|secret|key|token|api_key|auth)\s*=\s*[\'"][^\'"]{8,}[\'"]',
                    'issue': 'Hardcoded Credentials',
                    'severity': 'High',
                    'description': 'Sensitive credentials found in source code',
                    'confidence': 0.8,
                    'owasp_category': 'A07:2021-Identification and Authentication Failures',
                    'cwe_id': 'CWE-798',
                    'recommendation': 'Store credentials in environment variables: password = os.getenv("DB_PASSWORD")',
                    'category': 'credentials'
                },
                {
                    'pattern': r'-----BEGIN\s+(RSA\s+|DSA\s+|EC\s+)?PRIVATE\s+KEY-----',
                    'issue': 'Private Key Exposure',
                    'severity': 'Critical',
                    'description': 'Private key embedded in source code',
                    'confidence': 1.0,
                    'owasp_category': 'A02:2021-Cryptographic Failures',
                    'cwe_id': 'CWE-798',
                    'recommendation': 'Store private keys in secure key management systems or encrypted files',
                    'category': 'credentials'
                },
                
                # Deserialization Issues
                {
                    'pattern': r'\bpickle\.loads?\s*\([^)]*[a-zA-Z_$]',
                    'issue': 'Insecure Deserialization',
                    'severity': 'Critical',
                    'description': 'Pickle deserialization can execute arbitrary code',
                    'confidence': 0.9,
                    'owasp_category': 'A08:2021-Software and Data Integrity Failures',
                    'cwe_id': 'CWE-502',
                    'recommendation': 'Use JSON for data serialization or verify pickle data with HMAC signatures',
                    'category': 'deserialization'
                },
                {
                    'pattern': r'\byaml\.load\s*\([^)]*Loader\s*=\s*yaml\.Loader',
                    'issue': 'Unsafe YAML Deserialization',
                    'severity': 'High',
                    'description': 'YAML loading with unsafe Loader can execute arbitrary code',
                    'confidence': 0.9,
                    'owasp_category': 'A08:2021-Software and Data Integrity Failures',
                    'cwe_id': 'CWE-502',
                    'recommendation': 'Use yaml.safe_load() instead of yaml.load() with unsafe loaders',
                    'category': 'deserialization'
                },
                
                # Cryptographic Issues
                {
                    'pattern': r'\b(md5|MD5)\s*\(',
                    'issue': 'Weak Cryptographic Hash (MD5)',
                    'severity': 'Medium',
                    'description': 'MD5 is cryptographically broken and should not be used',
                    'confidence': 0.9,
                    'owasp_category': 'A02:2021-Cryptographic Failures',
                    'cwe_id': 'CWE-327',
                    'recommendation': 'Use SHA-256 or bcrypt for password hashing: hashlib.sha256() or bcrypt.hashpw()',
                    'category': 'crypto'
                },
                {
                    'pattern': r'\brandom\.random\(\)',
                    'issue': 'Weak Random Number Generation',
                    'severity': 'Medium',
                    'description': 'random.random() is not cryptographically secure',
                    'confidence': 0.7,
                    'owasp_category': 'A02:2021-Cryptographic Failures',
                    'cwe_id': 'CWE-338',
                    'recommendation': 'Use secrets module for cryptographic operations: secrets.randbelow()',
                    'category': 'crypto'
                },
                
                # Path Traversal
                {
                    'pattern': r'\bopen\s*\([^)]*\.\.\/',
                    'issue': 'Path Traversal Vulnerability',
                    'severity': 'High',
                    'description': 'File access with path traversal patterns',
                    'confidence': 0.8,
                    'owasp_category': 'A01:2021-Broken Access Control',
                    'cwe_id': 'CWE-22',
                    'recommendation': 'Validate file paths: os.path.abspath(os.path.join(safe_dir, filename))',
                    'category': 'path_traversal'
                },
                
                # Configuration Issues
                {
                    'pattern': r'debug\s*=\s*True',
                    'issue': 'Debug Mode Enabled',
                    'severity': 'Medium',
                    'description': 'Debug mode should be disabled in production',
                    'confidence': 0.8,
                    'owasp_category': 'A05:2021-Security Misconfiguration',
                    'cwe_id': 'CWE-489',
                    'recommendation': 'Set debug=False in production and use environment variables for configuration',
                    'category': 'configuration'
                },
                {
                    'pattern': r'ssl_verify\s*=\s*False',
                    'issue': 'SSL Verification Disabled',
                    'severity': 'High',
                    'description': 'SSL certificate verification is disabled',
                    'confidence': 0.9,
                    'owasp_category': 'A02:2021-Cryptographic Failures',
                    'cwe_id': 'CWE-295',
                    'recommendation': 'Always verify SSL certificates or use custom CA bundle if needed',
                    'category': 'crypto'
                }
            ],
            
            'javascript': [
                # Code Injection
                {
                    'pattern': r'\beval\s*\([^)]*[a-zA-Z_$]',
                    'issue': 'Code Injection via eval()',
                    'severity': 'Critical',
                    'description': 'eval() can execute arbitrary JavaScript code',
                    'confidence': 0.9,
                    'owasp_category': 'A03:2021-Injection',
                    'cwe_id': 'CWE-95',
                    'recommendation': 'Use JSON.parse() for JSON data or implement proper input validation',
                    'category': 'code_injection'
                },
                {
                    'pattern': r'Function\s*\([^)]*[a-zA-Z_$]',
                    'issue': 'Dynamic Function Creation',
                    'severity': 'High',
                    'description': 'Dynamic function creation with user input',
                    'confidence': 0.8,
                    'owasp_category': 'A03:2021-Injection',
                    'cwe_id': 'CWE-95',
                    'recommendation': 'Avoid dynamic function creation with user input',
                    'category': 'code_injection'
                },
                
                # XSS Vulnerabilities
                {
                    'pattern': r'\.innerHTML\s*=\s*[a-zA-Z_$]',
                    'issue': 'Cross-Site Scripting (XSS)',
                    'severity': 'High',
                    'description': 'innerHTML assignment with user data can lead to XSS',
                    'confidence': 0.8,
                    'owasp_category': 'A03:2021-Injection',
                    'cwe_id': 'CWE-79',
                    'recommendation': 'Use textContent for safe text insertion or sanitize HTML with DOMPurify',
                    'category': 'xss'
                },
                {
                    'pattern': r'document\.write\s*\([^)]*[a-zA-Z_$]',
                    'issue': 'XSS via document.write',
                    'severity': 'High',
                    'description': 'document.write with user input can lead to XSS',
                    'confidence': 0.8,
                    'owasp_category': 'A03:2021-Injection',
                    'cwe_id': 'CWE-79',
                    'recommendation': 'Use modern DOM methods like createElement() and textContent',
                    'category': 'xss'
                },
                {
                    'pattern': r'dangerouslySetInnerHTML\s*:\s*\{\s*__html\s*:\s*[a-zA-Z_$]',
                    'issue': 'React XSS Vulnerability',
                    'severity': 'High',
                    'description': 'dangerouslySetInnerHTML with user data',
                    'confidence': 0.9,
                    'owasp_category': 'A03:2021-Injection',
                    'cwe_id': 'CWE-79',
                    'recommendation': 'Sanitize HTML content with DOMPurify before using dangerouslySetInnerHTML',
                    'category': 'xss'
                },
                
                # Client-side Security
                {
                    'pattern': r'localStorage\.setItem.*?[a-zA-Z_$].*?(password|token|key)',
                    'issue': 'Sensitive Data in Local Storage',
                    'severity': 'Medium',
                    'description': 'Sensitive data stored in localStorage',
                    'confidence': 0.8,
                    'owasp_category': 'A02:2021-Cryptographic Failures',
                    'cwe_id': 'CWE-922',
                    'recommendation': 'Use secure HTTP-only cookies or sessionStorage with encryption',
                    'category': 'data_exposure'
                },
                {
                    'pattern': r'Math\.random\(\)',
                    'issue': 'Weak Random Number Generation',
                    'severity': 'Low',
                    'description': 'Math.random() is not cryptographically secure',
                    'confidence': 0.6,
                    'owasp_category': 'A02:2021-Cryptographic Failures',
                    'cwe_id': 'CWE-338',
                    'recommendation': 'Use crypto.getRandomValues() for cryptographic random numbers',
                    'category': 'crypto'
                },
                
                # URL Manipulation
                {
                    'pattern': r'window\.location\s*=\s*[a-zA-Z_$]',
                    'issue': 'Open Redirect Vulnerability',
                    'severity': 'Medium',
                    'description': 'URL redirection with user input',
                    'confidence': 0.7,
                    'owasp_category': 'A01:2021-Broken Access Control',
                    'cwe_id': 'CWE-601',
                    'recommendation': 'Validate redirect URLs against whitelist of allowed domains',
                    'category': 'redirect'
                }
            ],
            
            'typescript': [
                # Inherit JavaScript patterns plus TypeScript-specific
                {
                    'pattern': r'\beval\s*\(',
                    'issue': 'Code Injection via eval()',
                    'severity': 'Critical',
                    'description': 'eval() can execute arbitrary code',
                    'confidence': 0.9,
                    'owasp_category': 'A03:2021-Injection',
                    'cwe_id': 'CWE-95',
                    'recommendation': 'Use JSON.parse() for JSON data or proper input validation',
                    'category': 'code_injection'
                },
                {
                    'pattern': r'any\s+\w+.*?=.*?(req\.|request\.|user)',
                    'issue': 'Type Safety Bypass',
                    'severity': 'Medium',
                    'description': 'Using any type with user input bypasses type safety',
                    'confidence': 0.7,
                    'owasp_category': 'A06:2021-Vulnerable and Outdated Components',
                    'cwe_id': 'CWE-20',
                    'recommendation': 'Use proper TypeScript types and input validation instead of any',
                    'category': 'type_safety'
                }
            ],
            
            'c': [
                # Buffer Overflow Patterns
                {
                    'pattern': r'\bgets\s*\(',
                    'issue': 'Buffer Overflow (gets)',
                    'severity': 'Critical',
                    'description': 'gets() is unsafe and can cause buffer overflow',
                    'confidence': 1.0,
                    'owasp_category': 'A06:2021-Vulnerable and Outdated Components',
                    'cwe_id': 'CWE-120',
                    'recommendation': 'Use fgets() with buffer size limit: fgets(buffer, sizeof(buffer), stdin)',
                    'category': 'buffer_overflow'
                },
                {
                    'pattern': r'\bstrcpy\s*\(',
                    'issue': 'Buffer Overflow (strcpy)',
                    'severity': 'High',
                    'description': 'strcpy() does not check buffer boundaries',
                    'confidence': 0.9,
                    'owasp_category': 'A06:2021-Vulnerable and Outdated Components',
                    'cwe_id': 'CWE-120',
                    'recommendation': 'Use strncpy() or snprintf(): strncpy(dest, src, sizeof(dest)-1)',
                    'category': 'buffer_overflow'
                },
                {
                    'pattern': r'\bsprintf\s*\(',
                    'issue': 'Buffer Overflow (sprintf)',
                    'severity': 'High',
                    'description': 'sprintf() does not check buffer size',
                    'confidence': 0.9,
                    'owasp_category': 'A06:2021-Vulnerable and Outdated Components',
                    'cwe_id': 'CWE-120',
                    'recommendation': 'Use snprintf(): snprintf(buffer, sizeof(buffer), format, args)',
                    'category': 'buffer_overflow'
                },
                
                # Memory Management
                {
                    'pattern': r'\bmalloc\s*\([^)]*\)\s*;(?!\s*if)',
                    'issue': 'Unchecked malloc()',
                    'severity': 'Medium',
                    'description': 'malloc() return value not checked for NULL',
                    'confidence': 0.7,
                    'owasp_category': 'A06:2021-Vulnerable and Outdated Components',
                    'cwe_id': 'CWE-252',
                    'recommendation': 'Always check malloc() return value: if (!ptr) { handle_error(); }',
                    'category': 'memory_management'
                },
                
                # Command Injection
                {
                    'pattern': r'\bsystem\s*\([^)]*[a-zA-Z_$]',
                    'issue': 'Command Injection',
                    'severity': 'Critical',
                    'description': 'system() can execute arbitrary commands',
                    'confidence': 0.9,
                    'owasp_category': 'A03:2021-Injection',
                    'cwe_id': 'CWE-78',
                    'recommendation': 'Use execv() family functions with validated arguments',
                    'category': 'command_injection'
                }
            ],
            
            'cpp': [
                # All C patterns plus C++ specific
                {
                    'pattern': r'\bstd::system\s*\(',
                    'issue': 'Command Injection (C++)',
                    'severity': 'Critical',
                    'description': 'std::system() can execute arbitrary shell commands',
                    'confidence': 0.9,
                    'owasp_category': 'A03:2021-Injection',
                    'cwe_id': 'CWE-78',
                    'recommendation': 'Use safer alternatives or validate input thoroughly',
                    'category': 'command_injection'
                },
                {
                    'pattern': r'\bdelete\s+\w+;.*?\1',
                    'issue': 'Double Delete',
                    'severity': 'High',
                    'description': 'Potential double delete detected',
                    'confidence': 0.6,
                    'owasp_category': 'A06:2021-Vulnerable and Outdated Components',
                    'cwe_id': 'CWE-415',
                    'recommendation': 'Set pointer to nullptr after delete and use smart pointers',
                    'category': 'memory_management'
                }
            ],
            
            'java': [
                # Command Injection
                {
                    'pattern': r'\bRuntime\.getRuntime\(\)\.exec\s*\([^)]*[a-zA-Z_$]',
                    'issue': 'Command Injection',
                    'severity': 'Critical',
                    'description': 'Runtime.exec() can execute system commands',
                    'confidence': 0.9,
                    'owasp_category': 'A03:2021-Injection',
                    'cwe_id': 'CWE-78',
                    'recommendation': 'Use ProcessBuilder with validated arguments',
                    'category': 'command_injection'
                },
                
                # Deserialization
                {
                    'pattern': r'\breadObject\s*\([^)]*ObjectInputStream',
                    'issue': 'Unsafe Deserialization',
                    'severity': 'Critical',
                    'description': 'Custom readObject() method may be vulnerable',
                    'confidence': 0.8,
                    'owasp_category': 'A08:2021-Software and Data Integrity Failures',
                    'cwe_id': 'CWE-502',
                    'recommendation': 'Implement input validation and use allow-lists for deserialization',
                    'category': 'deserialization'
                },
                
                # Reflection
                {
                    'pattern': r'\bClass\.forName\s*\([^)]*[a-zA-Z_$]',
                    'issue': 'Reflection Injection',
                    'severity': 'High',
                    'description': 'Dynamic class loading with user input',
                    'confidence': 0.8,
                    'owasp_category': 'A03:2021-Injection',
                    'cwe_id': 'CWE-470',
                    'recommendation': 'Validate class names against whitelist before dynamic loading',
                    'category': 'reflection'
                },
                
                # Path Traversal
                {
                    'pattern': r'new\s+File\s*\([^)]*\+.*?[a-zA-Z_$]',
                    'issue': 'Path Traversal',
                    'severity': 'High',
                    'description': 'File path construction with user input',
                    'confidence': 0.8,
                    'owasp_category': 'A01:2021-Broken Access Control',
                    'cwe_id': 'CWE-22',
                    'recommendation': 'Validate file paths and use Path.normalize() to prevent traversal',
                    'category': 'path_traversal'
                }
            ],
            
            'php': [
                # Code Injection
                {
                    'pattern': r'\beval\s*\([^)]*\$_',
                    'issue': 'Code Injection via eval()',
                    'severity': 'Critical',
                    'description': 'eval() with user input can execute arbitrary PHP code',
                    'confidence': 0.9,
                    'owasp_category': 'A03:2021-Injection',
                    'cwe_id': 'CWE-95',
                    'recommendation': 'Never use eval() with user input. Use safe alternatives or validation',
                    'category': 'code_injection'
                },
                
                # Command Injection
                {
                    'pattern': r'\b(exec|shell_exec|system|passthru)\s*\([^)]*\$_',
                    'issue': 'Command Injection',
                    'severity': 'Critical',
                    'description': 'Command execution with user input',
                    'confidence': 0.9,
                    'owasp_category': 'A03:2021-Injection',
                    'cwe_id': 'CWE-78',
                    'recommendation': 'Use escapeshellarg() and validate input before command execution',
                    'category': 'command_injection'
                },
                
                # XSS
                {
                    'pattern': r'echo\s+\$_(GET|POST|REQUEST)\[',
                    'issue': 'Cross-Site Scripting (XSS)',
                    'severity': 'High',
                    'description': 'Direct output of user input without sanitization',
                    'confidence': 0.8,
                    'owasp_category': 'A03:2021-Injection',
                    'cwe_id': 'CWE-79',
                    'recommendation': 'Use htmlspecialchars() to escape output: htmlspecialchars($input, ENT_QUOTES)',
                    'category': 'xss'
                },
                
                # SQL Injection
                {
                    'pattern': r'mysql_query\s*\([^)]*\$_',
                    'issue': 'SQL Injection',
                    'severity': 'Critical',
                    'description': 'SQL query with user input using deprecated mysql_query',
                    'confidence': 0.9,
                    'owasp_category': 'A03:2021-Injection',
                    'cwe_id': 'CWE-89',
                    'recommendation': 'Use PDO with prepared statements instead of deprecated mysql functions',
                    'category': 'sql_injection'
                },
                
                # File Inclusion
                {
                    'pattern': r'(include|require)(_once)?\s*\([^)]*\$_',
                    'issue': 'File Inclusion Vulnerability',
                    'severity': 'Critical',
                    'description': 'File inclusion with user input',
                    'confidence': 0.9,
                    'owasp_category': 'A03:2021-Injection',
                    'cwe_id': 'CWE-98',
                    'recommendation': 'Validate file paths against whitelist and use basename() to prevent traversal',
                    'category': 'file_inclusion'
                },
                
                # Cryptographic Issues
                {
                    'pattern': r'\bmd5\s*\(\s*\$_(POST|GET|REQUEST)',
                    'issue': 'Weak Hash Algorithm (MD5)',
                    'severity': 'Medium',
                    'description': 'MD5 is cryptographically broken',
                    'confidence': 0.8,
                    'owasp_category': 'A02:2021-Cryptographic Failures',
                    'cwe_id': 'CWE-327',
                    'recommendation': 'Use password_hash() for passwords or hash() with SHA-256 for data integrity',
                    'category': 'crypto'
                }
            ],
            
            'html': [
                {
                    'pattern': r'<script[^>]*src=[\'"][^\'")]*[\'"][^>]*>',
                    'issue': 'External Script Loading',
                    'severity': 'Medium',
                    'description': 'Loading external JavaScript resources',
                    'confidence': 0.6,
                    'owasp_category': 'A06:2021-Vulnerable and Outdated Components',
                    'cwe_id': 'CWE-829',
                    'recommendation': 'Use Content Security Policy (CSP) and verify external script integrity',
                    'category': 'external_resources'
                },
                {
                    'pattern': r'javascript:',
                    'issue': 'JavaScript Protocol Usage',
                    'severity': 'High',
                    'description': 'javascript: protocol can lead to XSS',
                    'confidence': 0.8,
                    'owasp_category': 'A03:2021-Injection',
                    'cwe_id': 'CWE-79',
                    'recommendation': 'Use proper event handlers instead of javascript: protocol',
                    'category': 'xss'
                }
            ]
        }
    
    def _initialize_language_analyzers(self) -> Dict[str, callable]:
        """Initialize language-specific deep analyzers"""
        return {
            'python': self._analyze_python_advanced,
            'javascript': self._analyze_javascript_advanced,
            'php': self._analyze_php_advanced,
            'java': self._analyze_java_advanced
        }
    
    def _initialize_framework_patterns(self) -> Dict[str, List[Dict]]:
        """Initialize framework-specific vulnerability patterns"""
        return {
            'django': [
                {
                    'pattern': r'DEBUG\s*=\s*True',
                    'issue': 'Django Debug Mode Enabled',
                    'severity': 'Medium',
                    'description': 'Debug mode exposes sensitive information',
                    'confidence': 0.9,
                    'recommendation': 'Set DEBUG = False in production'
                },
                {
                    'pattern': r'\.extra\s*\([^)]*select\s*=.*[a-zA-Z_$]',
                    'issue': 'Django ORM SQL Injection',
                    'severity': 'High',
                    'description': 'Django ORM extra() method with user input',
                    'confidence': 0.8,
                    'recommendation': 'Use parameterized queries in extra() method'
                }
            ],
            'flask': [
                {
                    'pattern': r'app\.run\s*\([^)]*debug\s*=\s*True',
                    'issue': 'Flask Debug Mode Enabled',
                    'severity': 'Medium',
                    'description': 'Flask debug mode should be disabled in production',
                    'confidence': 0.9,
                    'recommendation': 'Set debug=False in production'
                }
            ],
            'react': [
                {
                    'pattern': r'dangerouslySetInnerHTML\s*:\s*\{\s*__html\s*:\s*[a-zA-Z_$]',
                    'issue': 'React XSS Risk',
                    'severity': 'High',
                    'description': 'dangerouslySetInnerHTML with user data',
                    'confidence': 0.9,
                    'recommendation': 'Sanitize HTML with DOMPurify before rendering'
                }
            ]
        }
    
    def _initialize_false_positive_filters(self) -> List[str]:
        """Initialize filters to reduce false positives"""
        return [
            r'^\s*(#|//|\*|/\*)',  # Comments
            r'test|mock|stub|dummy|example',  # Test context
            r'console\.log|print\s*\(',  # Debug statements
            r'import|from\s+.*\s+import',  # Import statements
        ]
    
    def scan_file(self, file_path: str) -> List[Dict[str, Any]]:
        """Main file scanning function with enterprise-grade analysis"""
        try:
            language = self._get_language(file_path)
            logging.info(f"Scanning {file_path} as {language}")
            
            # Read file content
            content = self._read_file_safely(file_path)
            if not content:
                return self._create_error_result("Could not read file")
            
            # Skip if test file
            if self._is_test_file(file_path, content):
                return [self._create_info_result("Test file skipped")]
            
            vulnerabilities = []
            
            # Pattern-based analysis
            pattern_vulns = self._scan_patterns(content, file_path, language)
            vulnerabilities.extend(pattern_vulns)
            
            # Language-specific deep analysis
            if language in self.language_analyzers:
                deep_vulns = self.language_analyzers[language](content, file_path)
                vulnerabilities.extend(deep_vulns)
            
            # Framework-specific analysis
            framework_vulns = self._scan_frameworks(content, file_path)
            vulnerabilities.extend(framework_vulns)
            
            # Remove duplicates and filter false positives
            vulnerabilities = self._deduplicate_vulnerabilities(vulnerabilities)
            vulnerabilities = self._filter_false_positives(vulnerabilities, content)
            
            # Sort by severity and confidence
            vulnerabilities = self._sort_vulnerabilities(vulnerabilities)
            
            if not vulnerabilities:
                return [self._create_info_result("No vulnerabilities detected")]
            
            # Convert to dict format for API response
            return [asdict(vuln) if isinstance(vuln, Vulnerability) else vuln 
                   for vuln in vulnerabilities]
            
        except Exception as e:
            logging.error(f"Error scanning {file_path}: {str(e)}")
            return [self._create_error_result(f"Scan error: {str(e)}")]
    
    def _scan_patterns(self, content: str, file_path: str, language: str) -> List[Vulnerability]:
        """Enhanced pattern scanning with confidence scoring"""
        vulnerabilities = []
        patterns = self.patterns.get(language, [])
        
        for pattern_info in patterns:
            matches = re.finditer(pattern_info['pattern'], content, re.IGNORECASE | re.MULTILINE)
            
            for match in matches:
                line_num = content[:match.start()].count('\n') + 1
                line_content = content.split('\n')[line_num - 1] if line_num <= len(content.split('\n')) else ''
                
                # Skip if line is commented or in test context
                if self._is_false_positive_line(line_content):
                    continue
                
                vuln = Vulnerability(
                    line=line_num,
                    code=line_content.strip(),
                    issue=pattern_info['issue'],
                    severity=pattern_info['severity'],
                    description=pattern_info['description'],
                    confidence=pattern_info.get('confidence', 0.7),
                    owasp_category=pattern_info.get('owasp_category', ''),
                    cwe_id=pattern_info.get('cwe_id', ''),
                    recommendation=pattern_info.get('recommendation', ''),
                    category=pattern_info.get('category', 'general')
                )
                vulnerabilities.append(vuln)
        
        return vulnerabilities
    
    def _analyze_python_advanced(self, content: str, file_path: str) -> List[Vulnerability]:
        """Advanced Python-specific analysis"""
        vulnerabilities = []
        
        try:
            # Parse Python AST for deeper analysis
            tree = ast.parse(content)
            
            class SecurityVisitor(ast.NodeVisitor):
                def __init__(self):
                    self.vulns = []
                
                def visit_Call(self, node):
                    # Check for dangerous function calls
                    if isinstance(node.func, ast.Name):
                        if node.func.id == 'eval' and len(node.args) > 0:
                            if not isinstance(node.args[0], ast.Constant):
                                self.vulns.append(Vulnerability(
                                    line=node.lineno,
                                    code=f"eval() call at line {node.lineno}",
                                    issue="AST: eval() with dynamic input",
                                    severity="Critical",
                                    description="eval() called with non-constant argument",
                                    confidence=0.9,
                                    owasp_category="A03:2021-Injection",
                                    cwe_id="CWE-95",
                                    recommendation="Use ast.literal_eval() for safe evaluation",
                                    category="code_injection"
                                ))
                    
                    self.generic_visit(node)
            
            visitor = SecurityVisitor()
            visitor.visit(tree)
            vulnerabilities.extend(visitor.vulns)
            
        except SyntaxError:
            # If AST parsing fails, continue with pattern matching
            pass
        except Exception as e:
            logging.warning(f"Python AST analysis failed for {file_path}: {e}")
        
        return vulnerabilities
    
    def _analyze_javascript_advanced(self, content: str, file_path: str) -> List[Vulnerability]:
        """Advanced JavaScript analysis using AST"""
        vulnerabilities = []
        
        try:
            ast = esprima.parseScript(content, {'loc': True, 'range': True})
            
            def traverse(node, parent=None):
                if not isinstance(node, dict):
                    return
                
                node_type = node.get('type')
                
                # Enhanced eval detection
                if (node_type == 'CallExpression' and 
                    node.get('callee', {}).get('name') == 'eval'):
                    
                    line_num = node.get('loc', {}).get('start', {}).get('line', 0)
                    vulnerabilities.append(Vulnerability(
                        line=line_num,
                        code=content.split('\n')[line_num - 1].strip() if line_num > 0 else 'N/A',
                        issue='AST: eval() Function Call',
                        severity='Critical',
                        description='eval() can execute arbitrary JavaScript code',
                        confidence=0.9,
                        owasp_category='A03:2021-Injection',
                        cwe_id='CWE-95',
                        recommendation='Use JSON.parse() for JSON data or implement proper validation',
                        category='code_injection'
                    ))
                
                # Enhanced innerHTML detection
                elif (node_type == 'AssignmentExpression' and
                      node.get('left', {}).get('type') == 'MemberExpression' and
                      node.get('left', {}).get('property', {}).get('name') == 'innerHTML'):
                    
                    line_num = node.get('loc', {}).get('start', {}).get('line', 0)
                    vulnerabilities.append(Vulnerability(
                        line=line_num,
                        code=content.split('\n')[line_num - 1].strip() if line_num > 0 else 'N/A',
                        issue='AST: innerHTML Assignment',
                        severity='High',
                        description='innerHTML assignment can lead to XSS vulnerabilities',
                        confidence=0.8,
                        owasp_category='A03:2021-Injection',
                        cwe_id='CWE-79',
                        recommendation='Use textContent for safe text or sanitize HTML with DOMPurify',
                        category='xss'
                    ))
                
                # Recursively traverse
                for key, value in node.items():
                    if isinstance(value, dict):
                        traverse(value, node)
                    elif isinstance(value, list):
                        for item in value:
                            if isinstance(item, dict):
                                traverse(item, node)
            
            traverse(ast)
            
        except Exception as e:
            logging.warning(f"JavaScript AST analysis failed for {file_path}: {e}")
        
        return vulnerabilities
    
    def _analyze_php_advanced(self, content: str, file_path: str) -> List[Vulnerability]:
        """Advanced PHP-specific analysis"""
        vulnerabilities = []
        
        # Check for unvalidated superglobal usage
        superglobal_patterns = [
            (r'\$_(GET|POST|REQUEST|COOKIE)\[[^\]]+\](?!\s*,\s*(FILTER_|filter_))', 'Unvalidated Superglobal', 'High'),
            (r'extract\s*\(\s*\$_(GET|POST|REQUEST)', 'Variable Extraction from User Input', 'Critical'),
            (r'parse_str\s*\([^,)]*\$_(GET|POST|REQUEST)', 'Parse String from User Input', 'High')
        ]
        
        for pattern, issue, severity in superglobal_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                line_num = content[:match.start()].count('\n') + 1
                line_content = content.split('\n')[line_num - 1] if line_num <= len(content.split('\n')) else ''
                
                vulnerabilities.append(Vulnerability(
                    line=line_num,
                    code=line_content.strip(),
                    issue=issue,
                    severity=severity,
                    description=f'PHP superglobal usage without validation: {match.group()}',
                    confidence=0.8,
                    owasp_category='A03:2021-Injection',
                    cwe_id='CWE-20',
                    recommendation='Use filter_input() or validate user input before use',
                    category='input_validation'
                ))
        
        return vulnerabilities
    
    def _analyze_java_advanced(self, content: str, file_path: str) -> List[Vulnerability]:
        """Advanced Java-specific analysis"""
        vulnerabilities = []
        
        # Check for serialization issues
        if 'implements Serializable' in content:
            serialization_patterns = [
                (r'readObject\s*\([^)]*ObjectInputStream', 'Unsafe Deserialization'),
                (r'readExternal\s*\([^)]*ObjectInput', 'Unsafe External Deserialization')
            ]
            
            for pattern, issue in serialization_patterns:
                matches = re.finditer(pattern, content)
                for match in matches:
                    line_num = content[:match.start()].count('\n') + 1
                    line_content = content.split('\n')[line_num - 1] if line_num <= len(content.split('\n')) else ''
                    
                    vulnerabilities.append(Vulnerability(
                        line=line_num,
                        code=line_content.strip(),
                        issue=issue,
                        severity='High',
                        description='Custom deserialization method detected',
                        confidence=0.8,
                        owasp_category='A08:2021-Software and Data Integrity Failures',
                        cwe_id='CWE-502',
                        recommendation='Implement input validation and use allow-lists for deserialization',
                        category='deserialization'
                    ))
        
        return vulnerabilities
    
    def _scan_frameworks(self, content: str, file_path: str) -> List[Vulnerability]:
        """Scan for framework-specific vulnerabilities"""
        vulnerabilities = []
        
        # Detect frameworks
        frameworks = []
        if any(keyword in content.lower() for keyword in ['django', 'from django']):
            frameworks.append('django')
        if any(keyword in content.lower() for keyword in ['flask', 'from flask']):
            frameworks.append('flask')
        if any(keyword in content.lower() for keyword in ['react', 'dangerouslysetinnerhtml']):
            frameworks.append('react')
        
        # Scan framework-specific patterns
        for framework in frameworks:
            patterns = self.framework_patterns.get(framework, [])
            for pattern_info in patterns:
                matches = re.finditer(pattern_info['pattern'], content, re.IGNORECASE)
                for match in matches:
                    line_num = content[:match.start()].count('\n') + 1
                    line_content = content.split('\n')[line_num - 1] if line_num <= len(content.split('\n')) else ''
                    
                    vulnerabilities.append(Vulnerability(
                        line=line_num,
                        code=line_content.strip(),
                        issue=pattern_info['issue'],
                        severity=pattern_info['severity'],
                        description=pattern_info['description'],
                        confidence=pattern_info.get('confidence', 0.8),
                        recommendation=pattern_info.get('recommendation', ''),
                        category=f'framework_{framework}'
                    ))
        
        return vulnerabilities
    
    def _get_language(self, file_path: str) -> str:
        """Enhanced language detection"""
        ext = file_path.rsplit('.', 1)[1].lower() if '.' in file_path else ''
        language_map = {
            'py': 'python', 'c': 'c', 'cpp': 'cpp', 'cc': 'cpp', 'cxx': 'cpp',
            'js': 'javascript', 'jsx': 'javascript', 'ts': 'typescript', 'tsx': 'typescript',
            'html': 'html', 'htm': 'html', 'java': 'java', 'php': 'php', 'phtml': 'php',
            'rb': 'ruby', 'go': 'go', 'cs': 'csharp', 'kt': 'kotlin', 'swift': 'swift',
            'rs': 'rust'
        }
        return language_map.get(ext, 'unknown')
    
    def _read_file_safely(self, file_path: str) -> Optional[str]:
        """Safely read file with multiple encoding attempts"""
        encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
        
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as file:
                    return file.read()
            except (UnicodeDecodeError, UnicodeError):
                continue
            except Exception as e:
                logging.error(f"Error reading {file_path}: {e}")
                return None
        
        logging.warning(f"Could not read {file_path} with any encoding")
        return None
    
    def _is_test_file(self, file_path: str, content: str) -> bool:
        """Enhanced test file detection"""
        test_indicators = [
            'test_', '_test.', '/test/', '\\test\\', 'tests/', '\\tests\\',
            'spec_', '_spec.', '/spec/', '\\spec\\', '__pycache__', '.git/',
            'node_modules/', '.pytest_cache', 'coverage'
        ]
        
        filename_lower = file_path.lower()
        return any(indicator in filename_lower for indicator in test_indicators)
    
    def _is_false_positive_line(self, line: str) -> bool:
        """Check if line is likely a false positive"""
        line_stripped = line.strip()
        
        # Skip empty lines
        if not line_stripped:
            return True
        
        # Check against false positive patterns
        for pattern in self.false_positive_filters:
            if re.search(pattern, line_stripped, re.IGNORECASE):
                return True
        
        return False
    
    def _filter_false_positives(self, vulnerabilities: List[Vulnerability], content: str) -> List[Vulnerability]:
        """Advanced false positive filtering"""
        filtered = []
        
        for vuln in vulnerabilities:
            # Skip if confidence is too low
            if vuln.confidence < 0.5:
                continue
            
            # Additional context-based filtering
            lines = content.split('\n')
            if vuln.line <= len(lines):
                line = lines[vuln.line - 1]
                
                # Skip if in comment context
                if re.search(r'^\s*(#|//|\*)', line.strip()):
                    continue
                
                # Skip test-related code
                if re.search(r'test|mock|stub|example', line, re.IGNORECASE):
                    continue
            
            filtered.append(vuln)
        
        return filtered
    
    def _deduplicate_vulnerabilities(self, vulnerabilities: List[Vulnerability]) -> List[Vulnerability]:
        """Remove duplicate vulnerabilities"""
        seen = set()
        unique = []
        
        for vuln in vulnerabilities:
            key = (vuln.line, vuln.issue, vuln.severity)
            if key not in seen:
                seen.add(key)
                unique.append(vuln)
        
        return unique
    
    def _sort_vulnerabilities(self, vulnerabilities: List[Vulnerability]) -> List[Vulnerability]:
        """Sort vulnerabilities by severity and confidence"""
        severity_order = {'Critical': 0, 'High': 1, 'Medium': 2, 'Low': 3, 'Info': 4}
        
        return sorted(vulnerabilities, key=lambda v: (
            severity_order.get(v.severity, 5),
            -v.confidence,
            v.line
        ))
    
    def _create_error_result(self, message: str) -> Dict[str, Any]:
        """Create standardized error result"""
        return {
            'line': 0,
            'code': 'N/A',
            'issue': f'Scan Error: {message}',
            'severity': 'High',
            'description': 'Error occurred during security analysis',
            'confidence': 1.0,
            'recommendation': 'Review file for syntax errors or encoding issues'
        }
    
    def _create_info_result(self, message: str) -> Dict[str, Any]:
        """Create standardized info result"""
        return {
            'line': 0,
            'code': 'N/A',
            'issue': message,
            'severity': 'Info',
            'description': 'File analysis completed',
            'confidence': 1.0,
            'recommendation': 'No action required'
        }

# Global scanner instance
scanner = EnterpriseSecurityScanner()

def scan_file(file_path: str) -> List[Dict[str, Any]]:
    """Main scanning function for backward compatibility"""
    return scanner.scan_file(file_path)

def get_language(file_path: str) -> str:
    """Get language for backward compatibility"""
    return scanner._get_language(file_path)

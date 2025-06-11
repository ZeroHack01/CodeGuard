<div align="center">

<!-- Animated Wave Header -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=280&section=header&text=CodeGuard&fontSize=80&fontColor=fff&animation=twinkling&fontAlignY=35&desc=🛡️%20Security%20Code%20Scanner&descAlignY=55&descSize=28" />

<br/>

<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=600&size=32&pause=1000&color=00D9FF&center=true&vCenter=true&width=800&lines=Static+Code+Security+Scanner;Vulnerability+Detection+Engine;Multi-Language+Analysis;Cross-Platform+Support;Real-Time+Security+Scanning" />

<br/>

![Version](https://img.shields.io/badge/VERSION-2.0.0-00D9FF?style=for-the-badge&labelColor=0a0a23&color=1a1a2e)
![Python](https://img.shields.io/badge/PYTHON-3.8+-00FF88?style=for-the-badge&labelColor=0a0a23&color=1a1a2e)
![License](https://img.shields.io/badge/LICENSE-MIT-FF3366?style=for-the-badge&labelColor=0a0a23&color=1a1a2e)
![Stars](https://img.shields.io/github/stars/ZeroHack01/CodeGuard?style=for-the-badge&labelColor=0a0a23&color=1a1a2e&label=STARS)

<br/>

**🔍 Advanced static code analysis tool for comprehensive security vulnerability detection**

[🚀 Quick Start](#installation) • [📱 Live Demo](#web-interface-preview) • [📖 Documentation](#usage-guide) • [🔧 API Reference](#api-reference) • [🌐 Languages](#supported-languages)

</div>

---

## 🛡️ **What Makes CodeGuard Special**

<div align="center">

### **Powerful Security Analysis Engine**

CodeGuard is a cutting-edge static code analyzer that identifies security vulnerabilities using advanced pattern matching and comprehensive code analysis across multiple programming languages.

</div>

<table>
<tr>
<td width="50%">

### 🔍 **Advanced Security Detection**
- **Code Injection** - eval(), exec(), dynamic execution
- **Authentication Flaws** - Hardcoded secrets & credentials  
- **Command Injection** - System command vulnerabilities
- **Memory Safety** - Buffer overflows (C/C++)
- **Web Security** - XSS, CSRF, DOM manipulation
- **Database Security** - SQL injection patterns
- **Cryptography** - Weak algorithms & implementations

</td>
<td width="50%">

### 📊 **Professional Features**
- **Real-time Analysis** - Instant vulnerability detection
- **Severity Classification** - Critical, High, Medium, Low
- **Smart Recommendations** - Auto-generated fix suggestions
- **Multiple Formats** - JSON, CSV, HTML reports
- **Web Dashboard** - Interactive browser interface
- **REST API** - Programmatic access & integration
- **CI/CD Ready** - Pipeline integration support

</td>
</tr>
</table>

---

## 🚀 **Installation & Setup**

<div align="center">

### **🌍 Cross-Platform Installation**

</div>

<table>
<tr>
<td width="33%" align="center">

### 🪟 **Windows**

```powershell
# PowerShell (Admin recommended)
git clone https://github.com/ZeroHack01/CodeGuard.git
cd CodeGuard

# Virtual Environment
python -m venv venv
venv\Scripts\activate

# Dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Launch Scanner
python app.py
```

**💡 Access:** `http://localhost:5000`

</td>
<td width="33%" align="center">

### 🍎 **macOS**

```bash
# Terminal
git clone https://github.com/ZeroHack01/CodeGuard.git
cd CodeGuard

# Virtual Environment  
python3 -m venv venv
source venv/bin/activate

# Dependencies
pip3 install --upgrade pip
pip3 install -r requirements.txt

# Launch Scanner
python3 app.py
```

**💡 Access:** `http://localhost:5000`

</td>
<td width="33%" align="center">

### 🐧 **Linux**

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install -y \
  python3 python3-pip python3-venv git

# CentOS/RHEL/Fedora
sudo dnf install python3 python3-pip git

# Setup
git clone https://github.com/ZeroHack01/CodeGuard.git
cd CodeGuard
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

# Launch
python3 app.py
```

**💡 Access:** `http://localhost:5000`

</td>
</tr>
</table>

### 🐳 **Docker Deployment**

<div align="center">

```bash
# Option 1: Docker Hub (Recommended)
docker pull zerohack01/codeguard:latest
docker run -d -p 5000:5000 --name codeguard-scanner zerohack01/codeguard:latest

# Option 2: Build from Source
git clone https://github.com/ZeroHack01/CodeGuard.git && cd CodeGuard
docker build -t codeguard-scanner .
docker run -d -p 5000:5000 --name codeguard-scanner codeguard-scanner

# Container Management
docker stop codeguard-scanner      # Stop container
docker start codeguard-scanner     # Start container  
docker rm codeguard-scanner        # Remove container
docker logs codeguard-scanner      # View logs
```

**🌐 Web Interface:** `http://localhost:5000` | **📡 API Endpoint:** `http://localhost:5000/api`

</div>

---

## 📱 **Web Interface Preview**

### 🎮 **Interactive Dashboard**

<div align="center">

![CodeGuard Dashboard](https://raw.githubusercontent.com/ZeroHack01/CodeGuard/main/screenshots/dashboard.png)

**🎯 Main Dashboard** - Clean, intuitive interface for uploading and managing code analysis

</div>

### 📤 **Smart File Upload System**

<div align="center">

![File Upload Interface](https://raw.githubusercontent.com/ZeroHack01/CodeGuard/main/screenshots/upload.png)

**🔄 Drag & Drop Upload** - Support for multiple files with automatic language detection

</div>

### 📊 **Comprehensive Results Dashboard**

<div align="center">

![Security Analysis Results](https://raw.githubusercontent.com/ZeroHack01/CodeGuard/main/screenshots/results.png)

**🔍 Detailed Analysis** - Line-by-line vulnerability reporting with severity levels and fix recommendations

</div>

---

## 📖 **Usage Guide**

### 🖥️ **Platform-Specific Instructions**

<table>
<tr>
<td width="33%" align="center">

### 🪟 **Windows Workflow**
1. **Launch** browser → `localhost:5000`
2. **Upload** code files via drag-drop
3. **Select** scan options & language
4. **Execute** security analysis  
5. **Review** detailed vulnerability report
6. **Export** results in preferred format

</td>
<td width="33%" align="center">

### 🍎 **macOS Workflow**
1. **Navigate** to `localhost:5000`
2. **Drop** files into upload zone
3. **Configure** analysis parameters
4. **Run** comprehensive security scan
5. **Analyze** results with recommendations  
6. **Download** reports for review

</td>
<td width="33%" align="center">

### 🐧 **Linux Workflow**
1. **Access** via Firefox/Chrome: `localhost:5000`
2. **Select** multiple files for batch scanning
3. **Customize** security check preferences
4. **Process** vulnerability analysis
5. **Examine** color-coded severity results
6. **Generate** exportable compliance reports

</td>
</tr>
</table>

### 💻 **Command Line Interface**

```python
# Python Integration
from scanner import scan_file, scan_directory

# Single file analysis
results = scan_file('vulnerable_app.py')
for vulnerability in results:
    print(f"🚨 Line {vulnerability['line']}: {vulnerability['issue']}")
    print(f"   Severity: {vulnerability['severity']}")
    print(f"   Fix: {vulnerability['recommendation']}")

# Directory scanning
batch_results = scan_directory('/path/to/project')
print(f"📊 Total vulnerabilities found: {len(batch_results)}")
```

```bash
# REST API Usage
# Upload and scan file
curl -X POST -F "file=@security_test.py" \
     -H "Content-Type: multipart/form-data" \
     http://localhost:5000/api/scan

# Get scan history
curl -X GET http://localhost:5000/api/history

# Download specific report
curl -X GET http://localhost:5000/api/download/json/scan_results_2024
```

---

## 📊 **Live Example Output**

<details>
<summary><b>🔍 Real Security Scan Results</b></summary>

```json
{
  "scan_metadata": {
    "filename": "payment_processor.py",
    "language": "python",
    "file_size": "3.2 KB",
    "scan_duration": "1.2s",
    "timestamp": "2024-06-11T12:30:45Z"
  },
  "vulnerability_summary": {
    "total_issues": 6,
    "critical": 2,
    "high": 3,
    "medium": 1,
    "low": 0,
    "risk_score": 8.7
  },
  "detailed_findings": [
    {
      "line_number": 23,
      "code_snippet": "eval(payment_data)",
      "vulnerability_type": "Code Injection",
      "severity": "CRITICAL",
      "cwe_id": "CWE-94",
      "description": "Arbitrary code execution through eval() function",
      "impact": "Complete system compromise possible",
      "recommendation": "Replace eval() with safe JSON parsing: json.loads(payment_data)",
      "fix_complexity": "Easy",
      "references": ["https://owasp.org/www-community/attacks/Code_Injection"]
    },
    {
      "line_number": 8,
      "code_snippet": "api_key = 'sk-prod-abc123xyz789'",
      "vulnerability_type": "Hardcoded Credential",
      "severity": "CRITICAL", 
      "cwe_id": "CWE-798",
      "description": "Production API key exposed in source code",
      "impact": "Unauthorized access to payment systems",
      "recommendation": "Use environment variables: api_key = os.getenv('PAYMENT_API_KEY')",
      "fix_complexity": "Easy",
      "references": ["https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure"]
    },
    {
      "line_number": 45,
      "code_snippet": "os.system(f'payment_cli --amount {amount}')",
      "vulnerability_type": "Command Injection",
      "severity": "HIGH",
      "cwe_id": "CWE-78",
      "description": "User input directly passed to system command",
      "impact": "Remote code execution via payment amount manipulation",
      "recommendation": "Use subprocess with parameterization and input validation",
      "fix_complexity": "Medium",
      "references": ["https://owasp.org/www-community/attacks/Command_Injection"]
    }
  ],
  "recommendations": {
    "immediate_actions": [
      "Remove hardcoded credentials immediately",
      "Replace eval() with safe parsing functions",
      "Implement input validation and sanitization"
    ],
    "security_improvements": [
      "Add comprehensive input validation",
      "Implement proper error handling",
      "Use parameterized queries for database operations",
      "Enable security logging and monitoring"
    ]
  }
}
```

</details>

---

## 🌐 **Supported Languages & Frameworks**

<div align="center">

| Language | Extensions | Security Patterns | Framework Support |
|----------|------------|-------------------|-------------------|
| 🐍 **Python** | `.py` `.pyw` `.pyc` | eval(), exec(), os.system(), pickle.loads() | Django, Flask, FastAPI |
| 🟨 **JavaScript** | `.js` `.jsx` `.mjs` | innerHTML, eval(), document.write() | React, Vue, Angular |
| ⚡ **TypeScript** | `.ts` `.tsx` `.d.ts` | Type safety issues, XSS vulnerabilities | Angular, React TS |
| 🔵 **C/C++** | `.c` `.cpp` `.h` `.hpp` | gets(), strcpy(), malloc(), system() | Native, Qt, Boost |
| ☕ **Java** | `.java` `.jar` `.class` | Runtime.exec(), reflection, deserialization | Spring, Struts, JSF |
| 🐘 **PHP** | `.php` `.phtml` `.php3` | eval(), shell_exec(), include(), mysqli | Laravel, Symfony, CodeIgniter |
| 💎 **Ruby** | `.rb` `.rbw` `.rake` | eval(), system(), send(), constantize() | Rails, Sinatra, Hanami |
| 🐹 **Go** | `.go` `.mod` `.sum` | exec.Command(), unsafe.Pointer, sql.Query | Gin, Echo, Fiber |
| 🌐 **HTML/CSS** | `.html` `.htm` `.css` | Script injection, unsafe protocols | Bootstrap, Tailwind |

</div>

### 🔧 **Advanced Detection Capabilities**

<details>
<summary><b>🛡️ Security Pattern Categories</b></summary>

#### **Injection Vulnerabilities**
- SQL Injection (SQLi)
- NoSQL Injection  
- LDAP Injection
- Command Injection
- Code Injection
- XPath Injection

#### **Authentication & Authorization**
- Hardcoded credentials
- Weak password policies
- Session management flaws
- JWT token vulnerabilities
- OAuth implementation issues

#### **Data Protection**
- Sensitive data exposure
- Insufficient encryption
- Weak cryptographic storage
- Data validation bypass
- Information leakage

#### **Memory Safety (C/C++)**
- Buffer overflows
- Memory leaks
- Use-after-free
- Double-free vulnerabilities
- Stack smashing

#### **Web Application Security**
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- DOM-based vulnerabilities
- Insecure redirects
- HTTP header injection

</details>

---

## 🔧 **API Documentation**

### 📡 **REST API Endpoints**

| Method | Endpoint | Description | Parameters |
|--------|----------|-------------|------------|
| `POST` | `/api/scan` | Upload and analyze file | `file` (multipart/form-data) |
| `GET` | `/api/scan/{scan_id}` | Get specific scan results | `scan_id` (string) |
| `GET` | `/api/history` | List all scan history | `limit`, `offset` (optional) |
| `GET` | `/api/download/{format}/{scan_id}` | Export scan results | `format` (json/csv/html) |
| `DELETE` | `/api/scan/{scan_id}` | Delete scan results | `scan_id` (string) |
| `GET` | `/api/stats` | Get scanning statistics | None |
| `POST` | `/api/batch` | Batch scan multiple files | `files[]` (multipart/form-data) |

### 📝 **API Usage Examples**

```bash
# Basic file scan
curl -X POST \
  -F "file=@vulnerable_code.py" \
  -H "Accept: application/json" \
  http://localhost:5000/api/scan

# Batch scanning
curl -X POST \
  -F "files=@app.py" \
  -F "files=@config.js" \
  -F "files=@database.sql" \
  http://localhost:5000/api/batch

# Download results
curl -X GET \
  -H "Accept: application/json" \
  http://localhost:5000/api/download/json/scan_20240611_123045 \
  -o security_report.json

# Get scan statistics
curl -X GET http://localhost:5000/api/stats
```

### 🔐 **API Authentication (Optional)**

```bash
# If API authentication is enabled
curl -X POST \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -F "file=@secure_app.py" \
  http://localhost:5000/api/scan
```

---

## ⚙️ **Advanced Configuration**

<details>
<summary><b>🔧 Environment Variables & Settings</b></summary>

```bash
# Server Configuration
export CODEGUARD_HOST=0.0.0.0              # Bind address
export CODEGUARD_PORT=5000                  # Port number
export CODEGUARD_DEBUG=false                # Debug mode
export CODEGUARD_WORKERS=4                  # Worker processes

# Security Settings
export MAX_FILE_SIZE=52428800               # 50MB file limit
export UPLOAD_TIMEOUT=60                    # Upload timeout (seconds)
export SCAN_TIMEOUT=300                     # Scan timeout (seconds)
export RATE_LIMIT=100                       # Requests per minute

# Analysis Configuration
export ENABLE_AST_ANALYSIS=true             # Advanced syntax tree analysis
export DEEP_SCAN_MODE=false                 # Resource-intensive deep scanning
export CUSTOM_RULES_PATH=/path/to/rules     # Custom security rules
export SEVERITY_THRESHOLD=medium            # Minimum severity to report

# Output Options
export DEFAULT_EXPORT_FORMAT=json           # Default export format
export INCLUDE_FIX_SUGGESTIONS=true         # Include auto-fix recommendations
export GENERATE_COMPLIANCE_REPORT=false     # Generate compliance reports
export REPORT_TEMPLATE_PATH=/path/templates # Custom report templates

# Database & Storage
export DATABASE_URL=sqlite:///codeguard.db  # Database connection
export RESULT_RETENTION_DAYS=30             # How long to keep results
export ENABLE_RESULT_CACHING=true           # Cache scan results

# Integrations
export SLACK_WEBHOOK_URL=https://hooks...   # Slack notifications
export EMAIL_SMTP_SERVER=smtp.gmail.com     # Email server
export JIRA_INTEGRATION=false               # JIRA ticket creation
```

</details>

---

## 🧪 **Testing & Quality Assurance**

### 🔬 **Built-in Test Suite**

```bash
# Run comprehensive tests
python -m pytest tests/ -v --cov=scanner

# Test specific vulnerability types
python test_injection_detection.py
python test_authentication_flaws.py
python test_cryptography_issues.py

# Performance benchmarking
python benchmark_scanner.py --files 1000 --iterations 10
```

### 📋 **Sample Vulnerable Code for Testing**

Create test files to verify CodeGuard detection:

```python
# test_vulnerabilities.py - Python test case
import os
import pickle

# Critical: Hardcoded credentials
api_secret = "sk-prod-1234567890abcdef"
database_password = "admin123!@#"

# Critical: Code injection
user_input = input("Enter calculation: ")
result = eval(user_input)  # Never do this!

# High: Command injection  
filename = input("Enter filename: ")
os.system(f"cat {filename}")  # Dangerous!

# High: Insecure deserialization
with open('user_data.pkl', 'rb') as f:
    data = pickle.load(f)  # Can execute arbitrary code

# Medium: Weak random generation
import random
session_token = str(random.randint(1000, 9999))
```

```javascript
// test_vulnerabilities.js - JavaScript test case
// Critical: XSS vulnerability
function displayUserContent(content) {
    document.getElementById('output').innerHTML = content; // Dangerous!
}

// High: eval() usage
const userCode = prompt("Enter JavaScript code:");
eval(userCode); // Never do this!

// Medium: Insecure random
const sessionId = Math.random().toString(); // Predictable
```

**Expected Results:** CodeGuard should detect 6+ vulnerabilities across these test files.

---

## 🤝 **Contributing & Community**

### 🌟 **How to Contribute**

1. **Fork** the repository
2. **Create** feature branch: `git checkout -b feature/amazing-detection`
3. **Implement** your security improvements  
4. **Add** comprehensive tests for new detection rules
5. **Commit** changes: `git commit -m "Add advanced XSS detection"`
6. **Push** to branch: `git push origin feature/amazing-detection`
7. **Submit** Pull Request with detailed description

### 🐛 **Bug Reports & Feature Requests**

- **🐛 Bug Reports:** Use [GitHub Issues](https://github.com/ZeroHack01/CodeGuard/issues) with detailed reproduction steps
- **💡 Feature Requests:** Create [GitHub Issues](https://github.com/ZeroHack01/CodeGuard/issues) with enhancement label
- **🔒 Security Issues:** Email [mongwoiching2080@gmail.com](mailto:mongwoiching2080@gmail.com) for responsible disclosure

### 📚 **Development Setup**

```bash
# Development environment
git clone https://github.com/ZeroHack01/CodeGuard.git
cd CodeGuard

# Install development dependencies
pip install -r requirements-dev.txt

# Run in development mode
export FLASK_ENV=development
export FLASK_DEBUG=true
python app.py

# Code formatting and linting
black . --line-length 88
flake8 . --max-line-length 88
mypy scanner/ --strict
```

---

## 📄 **License & Legal**

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for complete terms.

### 📜 **Third-Party Libraries**
- Flask (BSD-3-Clause)
- Werkzeug (BSD-3-Clause) 
- Jinja2 (BSD-3-Clause)
- Click (BSD-3-Clause)

---

## 📈 **Project Statistics**

<div align="center">

![GitHub stars](https://img.shields.io/github/stars/ZeroHack01/CodeGuard?style=social)
![GitHub forks](https://img.shields.io/github/forks/ZeroHack01/CodeGuard?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/ZeroHack01/CodeGuard?style=social)

![GitHub issues](https://img.shields.io/github/issues/ZeroHack01/CodeGuard)
![GitHub pull requests](https://img.shields.io/github/issues-pr/ZeroHack01/CodeGuard)
![GitHub last commit](https://img.shields.io/github/last-commit/ZeroHack01/CodeGuard)
![GitHub code size](https://img.shields.io/github/languages/code-size/ZeroHack01/CodeGuard)

</div>

---

<!-- Animated Wave Footer -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=180&section=footer&text=Secure%20Code%2C%20Secure%20Future&fontSize=45&fontColor=fff&animation=twinkling&fontAlignY=75" />

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=600&size=24&pause=1000&color=00D9FF&center=true&vCenter=true&width=600&lines=Built+with+❤️+by+@ZeroHack01;Static+Code+Security+Analysis;Open+Source+%26+Community+Driven;Making+Code+Safer+Everywhere" />

<br/>

**[🐛 Report Issues](https://github.com/ZeroHack01/CodeGuard/issues) • [💼 LinkedIn](https://www.linkedin.com/in/mongwoi/) • [📧 Email](mailto:mongwoiching2080@gmail.com) • [🌟 Star this repo](https://github.com/ZeroHack01/CodeGuard)**

[![GitHub followers](https://img.shields.io/github/followers/ZeroHack01?style=social)](https://github.com/ZeroHack01)
[![Twitter Follow](https://img.shields.io/twitter/follow/ZeroHack01?style=social)](https://twitter.com/ZeroHack01)

**⭐ Star this repository if CodeGuard helped secure your code!**

*Trusted by developers worldwide for comprehensive security analysis*

</div>

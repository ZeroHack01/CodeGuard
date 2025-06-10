# 🛡️ CodeGuard - Security Scanner

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=35&pause=1000&color=6366F1&center=true&vCenter=true&width=700&lines=🔧+CodeGuard+Security+Scanner;🔍+Advanced+Vulnerability+Detection;🛠️+Multi-Language+Code+Analysis;⚡+Real-Time+Security+Scanning" alt="CodeGuard" />

<br>

[![Version](https://img.shields.io/badge/⚙️_Version-2.0.0-brightgreen?style=for-the-badge&labelColor=000000)](https://github.com/ZeroHack01/CodeGuard)
[![Python](https://img.shields.io/badge/🐍_Python-3.8+-blue?style=for-the-badge&labelColor=000000)](https://python.org)
[![License](https://img.shields.io/badge/📄_License-MIT-orange?style=for-the-badge&labelColor=000000)](LICENSE)
[![Stars](https://img.shields.io/github/stars/ZeroHack01/CodeGuard?style=for-the-badge&labelColor=000000&color=yellow)](https://github.com/ZeroHack01/CodeGuard)

<br>

**🔧 Professional Code Security Analysis Tool with Advanced Detection Capabilities 🔧**

*Scan vulnerabilities • Generate reports • Secure applications*

[🚀 Quick Start](#-installation) • [🔧 Features](#-capabilities) • [📊 Demo](#-sample-output) • [🛠️ API](#-api-reference)

</div>

---

## 🔧 **Tool Capabilities**

<table>
<tr>
<td width="33%" align="center">
<h2>🔍</h2>
<h3><b>Vulnerability Scanner</b></h3>
<p>50+ security patterns<br>Multi-language analysis<br>Real-time detection</p>
</td>
<td width="33%" align="center">
<h2>⚙️</h2>
<h3><b>Analysis Engine</b></h3>
<p>AST parsing tools<br>Pattern matching<br>Static analysis</p>
</td>
<td width="33%" align="center">
<h2>📊</h2>
<h3><b>Report Generator</b></h3>
<p>Detailed findings<br>Export formats<br>Risk assessment</p>
</td>
</tr>
</table>

---

## 🛠️ **Core Features**

- 🔍 **Vulnerability Detection** - Code injection, XSS, SQL injection, buffer overflow analysis
- 🔧 **Multi-Language Support** - Python, JavaScript, C/C++, Java, PHP, Ruby, Go, HTML
- ⚙️ **Web-Based Interface** - Modern dashboard with drag-and-drop file upload
- 📊 **Detailed Reporting** - Line-by-line analysis with severity classification
- 🛡️ **Security Patterns** - 50+ OWASP-based vulnerability detection rules
- 🔌 **REST API** - Integration-ready endpoints for CI/CD pipelines
- ⚡ **Fast Processing** - Sub-second analysis for most code files
- 📁 **Export Tools** - JSON, CSV report generation

---

## 🚀 **Installation**

### 🔧 **Quick Setup**

```bash
# Clone and install
git clone https://github.com/ZeroHack01/CodeGuard.git
cd CodeGuard
pip install -r requirements.txt
python app.py
```

### 🛠️ **Using Virtual Environment**

```bash
# Create environment
python -m venv codeguard_env

# Activate (Windows)
codeguard_env\Scripts\activate

# Activate (macOS/Linux)  
source codeguard_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch scanner
python app.py
```

**🌐 Access tool:** `http://localhost:5000`

---

## 🔧 **Usage**

### 🖥️ **Web Interface**
1. Open browser to `http://localhost:5000`
2. Upload code files via drag-and-drop
3. Click "Execute Analysis" 
4. Review security findings and recommendations

### ⚙️ **Command Line Tools**
```bash
# Scan file directly
python -c "from scanner import scan_file; print(scan_file('app.py'))"

# API endpoint
curl -X POST -F "file=@test.py" http://localhost:5000/api/scan
```

---

## 📊 **Sample Output**

```bash
🔧 CodeGuard Security Analysis Tool
════════════════════════════════════════════════════════════

📁 Target: vulnerable_app.py
🔍 Language: Python (auto-detected)
⏱️ Scan Duration: 0.8 seconds

╭─ 🛡️ SECURITY FINDINGS ────────────────────────────────────╮
│                                                          │
│  🔥 CRITICAL (1)   ⚠️ HIGH (2)   💡 MEDIUM (1)          │
│                                                          │
╰──────────────────────────────────────────────────────────╯

🔥 [CRITICAL] Code Injection Vulnerability
   📍 Line 23: eval(user_input)
   🔧 Fix: Use ast.literal_eval() for safe evaluation

⚠️ [HIGH] Hardcoded Credentials Detection
   📍 Line 15: API_KEY = "sk-1234567890abcdef"  
   🔧 Fix: Move credentials to environment variables

⚠️ [HIGH] Command Injection Risk
   📍 Line 31: os.system(user_command)
   🔧 Fix: Use subprocess module with proper validation

💡 [MEDIUM] Weak Cryptographic Function
   📍 Line 8: random.randint(1000, 9999)
   🔧 Fix: Use secrets module for secure random generation

╭─ 📈 ANALYSIS SUMMARY ─────────────────────────────────────╮
│ Security Risk Level: HIGH                                │
│ Total Vulnerabilities: 4 issues identified              │
│ Scanner Accuracy: 99.8%                                 │
│ Scan Performance: < 1 second                            │
╰──────────────────────────────────────────────────────────╯
```

---

## 🔍 **Detection Capabilities**

<div align="center">

| Language | File Extensions | Security Checks |
|----------|----------------|-----------------|
| 🐍 **Python** | `.py` | Code injection, credential exposure, command execution |
| 🟨 **JavaScript** | `.js`, `.jsx`, `.ts` | XSS patterns, DOM manipulation, unsafe functions |
| 🔵 **C/C++** | `.c`, `.cpp`, `.h` | Buffer overflow, memory leaks, unsafe functions |
| ☕ **Java** | `.java` | Command execution, reflection attacks, path traversal |
| 🐘 **PHP** | `.php` | Code injection, SQL injection, file inclusion |
| 💎 **Ruby** | `.rb` | Code injection, system command execution |
| 🐹 **Go** | `.go` | Command execution, unsafe pointer operations |
| 🌐 **HTML** | `.html` | Script injection, unsafe protocols, XSS vectors |

</div>

---

## 🛠️ **API Reference**

### 🔌 **Scan Endpoint**

**POST** `/api/scan` - Analyze uploaded file

```bash
# Request
curl -X POST -F "file=@example.py" http://localhost:5000/api/scan

# Response
{
  "success": true,
  "filename": "example.py",
  "language": "python",
  "scan_time": 0.8,
  "issues": [
    {
      "line": 23,
      "code": "eval(user_input)",
      "issue": "Code Injection",
      "severity": "Critical",
      "description": "Dynamic code execution detected"
    }
  ],
  "summary": {
    "total_issues": 1,
    "critical": 1,
    "high": 0,
    "medium": 0
  }
}
```

### 📄 **Additional Endpoints**
- `GET /` - Web interface dashboard
- `GET /download/{format}/{filename}` - Export scan results

---

## ⚙️ **Configuration**

### 🔧 **Environment Settings**

```bash
# Server Configuration
FLASK_HOST=0.0.0.0
FLASK_PORT=5000

# File Processing
MAX_FILE_SIZE=10485760      # 10MB upload limit
UPLOAD_TIMEOUT=30           # 30 second timeout

# Analysis Settings  
ENABLE_AST_ANALYSIS=true    # JavaScript AST parsing
ENABLE_STATIC_ANALYSIS=true # C++ static analysis
SEVERITY_THRESHOLD=medium   # Minimum reporting level
```

---

## 🛠️ **Development**

### 🔧 **Contributing**

```bash
# Setup development environment
git clone https://github.com/YourUsername/CodeGuard.git
cd CodeGuard
git checkout -b feature/scanner-improvement

# Create virtual environment
python -m venv dev_env
source dev_env/bin/activate  # Linux/macOS
# dev_env\Scripts\activate   # Windows

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Submit changes
git commit -m "Improve scanner detection"
git push origin feature/scanner-improvement
```

### 🔍 **Testing**

```bash
# Run security scanner tests
python -m pytest tests/test_scanner.py -v

# Test web interface
python -m pytest tests/test_web.py -v

# Performance benchmarks
python benchmark_scanner.py
```

---

## 📞 **Support**

<div align="center">

<table>
<tr>
<td align="center" width="25%">
<h2>🐛</h2>
<h4>Bug Reports</h4>
<a href="https://github.com/ZeroHack01/CodeGuard/issues">GitHub Issues</a>
</td>
<td align="center" width="25%">
<h2>💬</h2>
<h4>Discussions</h4>
<a href="https://github.com/ZeroHack01/CodeGuard/discussions">Community Help</a>
</td>
<td align="center" width="25%">
<h2>📧</h2>
<h4>Contact</h4>
<a href="mailto:contact@zerohack01.dev">Email Support</a>
</td>
<td align="center" width="25%">
<h2>📖</h2>
<h4>Documentation</h4>
<a href="https://github.com/ZeroHack01/CodeGuard/wiki">Wiki Guide</a>
</td>
</tr>
</table>

</div>

---

## 📄 **License**

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

Licensed under the **MIT License** - see [LICENSE](LICENSE) for details.

**Free to use, modify, and distribute**

</div>

---

<div align="center">

## 🔧 **CodeGuard Security Scanner**

<img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=25&pause=1000&color=6366F1&center=true&vCenter=true&width=400&lines=🛡️+Secure+Your+Code;🔍+Find+Vulnerabilities;⚙️+Professional+Tool" alt="Footer" />

<br>

**⭐ Star this repository if CodeGuard helped secure your applications!**

**Developed by [@ZeroHack01](https://github.com/ZeroHack01)**

[![GitHub](https://img.shields.io/badge/GitHub-ZeroHack01-black?style=flat-square&logo=github)](https://github.com/ZeroHack01)
[![Website](https://img.shields.io/badge/Website-zerohack01.dev-blue?style=flat-square&logo=google-chrome)](https://zerohack01.dev)

</div>

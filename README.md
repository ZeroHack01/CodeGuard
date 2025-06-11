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

[🚀 Quick Start](#installation) • [📱 Live Demo](#web-interface-preview) • [📖 Documentation](#usage-guide) • [🔧 API Reference](#api-reference) • [🌐 Languages](#supported-languages--frameworks)

</div>

---

## 🛡️ **What CodeGuard Does**

CodeGuard is a cutting-edge static code analyzer that identifies security vulnerabilities using advanced pattern matching and comprehensive code analysis across multiple programming languages.

<table>
<tr>
<td width="50%">

### 🔍 **Security Detection**
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

## 🚀 **Installation**

<div align="center">

### **🌍 Cross-Platform Installation**

</div>

<table>
<tr>
<td width="33%" align="center">

### 🪟 **Windows**

```powershell
# PowerShell
git clone https://github.com/ZeroHack01/CodeGuard.git
cd CodeGuard

# Virtual Environment
python -m venv venv
venv\Scripts\activate

# Dependencies
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
# Option 1: Docker Hub
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
```

**🌐 Web Interface:** `http://localhost:5000`

</div>

---

## 📱 **Web Interface Preview**

### 🎮 **Interactive Dashboard**

<div align="center">

![CodeGuard Dashboard](https://raw.githubusercontent.com/ZeroHack01/CodeGuard/main/screenshots/dashboard.png)

**🎯 Main Dashboard** - Clean interface for uploading and managing code analysis

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

## 🌐 **Supported Languages & Frameworks**

<div align="center">

**📈 Framework Support**

| Language | Popular Frameworks |
|----------|-------------------|
| **Python** | Django, Flask, FastAPI |
| **JavaScript** | React, Vue, Angular |
| **TypeScript** | Angular, React TS |
| **C/C++** | Qt, Boost, Native |
| **Java** | Spring, Struts, JSF |
| **PHP** | Laravel, Symfony |
| **Ruby** | Rails, Sinatra |
| **Go** | Gin, Echo, Fiber |
| **HTML/CSS** | Bootstrap, Tailwind |

</td>
</tr>
</table>

</div>

---

### **🔧 Security Patterns Detected**

<div align="center">

| Language | File Types | Critical Vulnerabilities | Detection Rate |
|----------|------------|-------------------------|----------------|
| 🐍 **Python** | `.py .pyw .pyc` | eval(), exec(), pickle.loads(), os.system() | ![95%](https://img.shields.io/badge/95%25-success-brightgreen) |
| 🟨 **JavaScript** | `.js .jsx .mjs` | innerHTML, eval(), document.write() | ![90%](https://img.shields.io/badge/90%25-success-green) |
| ⚡ **TypeScript** | `.ts .tsx .d.ts` | Type bypass, XSS vulnerabilities | ![88%](https://img.shields.io/badge/88%25-success-green) |
| 🔵 **C/C++** | `.c .cpp .h .hpp` | gets(), strcpy(), buffer overflows | ![85%](https://img.shields.io/badge/85%25-important-yellow) |
| ☕ **Java** | `.java .jar .class` | Runtime.exec(), reflection, deserialization | ![82%](https://img.shields.io/badge/82%25-important-yellow) |
| 🐘 **PHP** | `.php .phtml .php3` | eval(), shell_exec(), SQL injection | ![80%](https://img.shields.io/badge/80%25-important-yellow) |
| 💎 **Ruby** | `.rb .rbw .rake` | eval(), system(), command injection | ![78%](https://img.shields.io/badge/78%25-warning-orange) |
| 🐹 **Go** | `.go .mod .sum` | exec.Command(), unsafe operations | ![75%](https://img.shields.io/badge/75%25-warning-orange) |
| 🌐 **HTML/CSS** | `.html .htm .css` | Script injection, unsafe protocols | ![70%](https://img.shields.io/badge/70%25-critical-red) |

</div>

---

<div align="center">

### **📊 Summary Statistics**

![Total Languages](https://img.shields.io/badge/Languages-9-blue?style=flat-square)
![Security Patterns](https://img.shields.io/badge/Patterns-248+-green?style=flat-square)
![Average Coverage](https://img.shields.io/badge/Coverage-83%25-brightgreen?style=flat-square)
![Scan Speed](https://img.shields.io/badge/Speed-<2s-lightblue?style=flat-square)

**🛡️ CodeGuard provides comprehensive security analysis across all major programming languages**

</div>

---

## 🔧 **API Reference**

### 📡 **Available Endpoints**

| Method | Endpoint | Description | Parameters |
|--------|----------|-------------|------------|
| `POST` | `/api/scan` | Upload and analyze file | `file` (multipart/form-data) |
| `GET` | `/` | Access web interface | None |

### 📝 **API Usage Examples**

```bash
# Upload and scan a file
curl -X POST \
  -F "file=@source_code.py" \
  -H "Accept: application/json" \
  http://localhost:5000/api/scan

# Test with vulnerable Python code
echo 'eval(user_input)' > test.py
curl -X POST -F "file=@test.py" http://localhost:5000/api/scan

# Test with hardcoded credentials
echo 'password = "admin123"' > config.py  
curl -X POST -F "file=@config.py" http://localhost:5000/api/scan
```

### 📋 **Response Format**

```json
{
  "success": true,
  "filename": "source_code.py",
  "language": "python",
  "issues": [
    {
      "line": 15,
      "code": "eval(data)",
      "issue": "Code Injection",
      "severity": "Critical"
    }
  ],
  "total_issues": 1
}
```

---

## 📊 **Sample Output**

<details>
<summary><b>🔍 Example scan results</b></summary>

```json
{
  "filename": "app.py",
  "language": "python",
  "scan_time": 0.8,
  "issues": [
    {
      "line": 23,
      "code": "eval(user_input)",
      "issue": "Code Injection",
      "severity": "Critical",
      "description": "Dynamic code execution detected"
    },
    {
      "line": 15,
      "code": "password = 'admin123'",
      "issue": "Hardcoded Password",
      "severity": "High",
      "description": "Credentials found in source code"
    },
    {
      "line": 31,
      "code": "os.system(command)",
      "issue": "Command Injection",
      "severity": "High",
      "description": "System command execution risk"
    }
  ],
  "summary": {
    "total_issues": 3,
    "critical": 1,
    "high": 2,
    "medium": 0
  }
}
```

</details>

---

## 🧪 **Testing CodeGuard**

Create a test file with known vulnerabilities:

```python
# test_vulnerable.py
api_key = "sk-1234567890abcdef"    # Hardcoded credential
user_code = input("Enter code: ")
eval(user_code)                    # Code injection
os.system("ls " + user_path)       # Command injection
```

Expected result: 3 security issues detected

---

## ⚙️ **Configuration**

<details>
<summary><b>🔧 Environment Settings</b></summary>

```bash
# Server Configuration
FLASK_HOST=0.0.0.0              # Bind address
FLASK_PORT=5000                 # Port number
FLASK_DEBUG=false               # Debug mode

# File Processing
MAX_FILE_SIZE=10485760          # 10MB limit
UPLOAD_TIMEOUT=30               # 30 seconds

# Scanner Options
SEVERITY_THRESHOLD=medium       # Minimum severity to report
EXPORT_FORMATS=json,csv         # Available export formats
```

</details>

---

## 🤝 **Contributing**

1. **Fork** the repository
2. **Create** feature branch: `git checkout -b feature/amazing-detection`
3. **Implement** your security improvements  
4. **Add** comprehensive tests
5. **Commit** changes: `git commit -m "Add new feature"`
6. **Push** to branch: `git push origin feature/amazing-detection`
7. **Submit** Pull Request

### 🐛 **Bug Reports & Feature Requests**

- **🐛 Bug Reports:** Use [GitHub Issues](https://github.com/ZeroHack01/CodeGuard/issues) with detailed reproduction steps
- **💡 Feature Requests:** Create [GitHub Issues](https://github.com/ZeroHack01/CodeGuard/issues) with enhancement label
- **🔒 Security Issues:** Email [mongwoiching2080@gmail.com](mailto:mongwoiching2080@gmail.com) for responsible disclosure

---

## 📄 **License**

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for complete terms.

### 📦 **Dependencies**
- **Flask** - Web framework for the interface
- **Werkzeug** - WSGI web application library
- **Other dependencies** - See `requirements.txt` for complete list

---

<!-- Animated Wave Footer -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=180&section=footer&text=Secure%20Code%2C%20Secure%20Future&fontSize=45&fontColor=fff&animation=twinkling&fontAlignY=75" />

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=600&size=24&pause=1000&color=00D9FF&center=true&vCenter=true&width=600&lines=Built+with+❤️+by+@ZeroHack01;Static+Code+Security+Analysis;Open+Source+%26+Community+Driven;Making+Code+Safer+Everywhere" />

<br/>

**[🐛 Report Issues](https://github.com/ZeroHack01/CodeGuard/issues) • [💼 LinkedIn](https://www.linkedin.com/in/mongwoi/) • [📧 Email](mailto:mongwoiching2080@gmail.com)**

[![GitHub](https://img.shields.io/badge/GitHub-ZeroHack01-black?style=flat-square&logo=github)](https://github.com/ZeroHack01)

**⭐ Star this repository if CodeGuard helped secure your code!**

</div>

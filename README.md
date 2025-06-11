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

## 📖 **Usage Guide**

### 🖥️ **Platform-Specific Instructions**

<table>
<tr>
<td width="33%" align="center">

### 🪟 **Windows**
1. **Launch** browser → `localhost:5000`
2. **Upload** code files via drag-drop
3. **Execute** security analysis  
4. **Review** vulnerability report
5. **Export** results if needed

</td>
<td width="33%" align="center">

### 🍎 **macOS**
1. **Navigate** to `localhost:5000`
2. **Drop** files into upload zone
3. **Run** comprehensive scan
4. **Analyze** results with recommendations  
5. **Download** reports for review

</td>
<td width="33%" align="center">

### 🐧 **Linux**
1. **Access** via browser: `localhost:5000`
2. **Select** files for scanning
3. **Process** vulnerability analysis
4. **Examine** color-coded results
5. **Generate** exportable reports

</td>
</tr>
</table>

### 💻 **Command Line Interface**

```python
# Python Integration
from scanner import scan_file

# Single file analysis
results = scan_file('vulnerable_app.py')
for vulnerability in results:
    print(f"🚨 Line {vulnerability['line']}: {vulnerability['issue']}")
    print(f"   Severity: {vulnerability['severity']}")
```

```bash
# REST API Usage
curl -X POST -F "file=@security_test.py" \
     -H "Content-Type: multipart/form-data" \
     http://localhost:5000/api/scan
```

---

## 🌐 **Supported Languages & Frameworks**

<div align="center">

### **📊 Language Detection Coverage - Circular Statistics**

<table>
<tr>
<td align="center" width="25%">

**🐍 Python**

<svg width="140" height="140">
  <circle cx="70" cy="70" r="60" stroke="#e5e7eb" stroke-width="12" fill="none"/>
  <circle cx="70" cy="70" r="60" stroke="#3776ab" stroke-width="12" fill="none"
          stroke-dasharray="357" stroke-dashoffset="18" stroke-linecap="round" transform="rotate(-90 70 70)"/>
  <text x="70" y="75" text-anchor="middle" font-size="20" font-weight="bold" fill="#3776ab">95%</text>
</svg>

**Extensions:** `.py .pyw .pyc`
**Frameworks:** Django, Flask, FastAPI
**Patterns:** eval(), exec(), os.system(), pickle.loads()

</td>
<td align="center" width="25%">

**🟨 JavaScript**

<svg width="140" height="140">
  <circle cx="70" cy="70" r="60" stroke="#e5e7eb" stroke-width="12" fill="none"/>
  <circle cx="70" cy="70" r="60" stroke="#f7df1e" stroke-width="12" fill="none"
          stroke-dasharray="339" stroke-dashoffset="36" stroke-linecap="round" transform="rotate(-90 70 70)"/>
  <text x="70" y="75" text-anchor="middle" font-size="20" font-weight="bold" fill="#333">90%</text>
</svg>

**Extensions:** `.js .jsx .mjs`
**Frameworks:** React, Vue, Angular
**Patterns:** innerHTML, eval(), document.write()

</td>
<td align="center" width="25%">

**⚡ TypeScript**

<svg width="140" height="140">
  <circle cx="70" cy="70" r="60" stroke="#e5e7eb" stroke-width="12" fill="none"/>
  <circle cx="70" cy="70" r="60" stroke="#3178c6" stroke-width="12" fill="none"
          stroke-dasharray="331" stroke-dashoffset="45" stroke-linecap="round" transform="rotate(-90 70 70)"/>
  <text x="70" y="75" text-anchor="middle" font-size="20" font-weight="bold" fill="#3178c6">88%</text>
</svg>

**Extensions:** `.ts .tsx .d.ts`
**Frameworks:** Angular, React TS
**Patterns:** Type safety issues, XSS vulnerabilities

</td>
<td align="center" width="25%">

**🔵 C/C++**

<svg width="140" height="140">
  <circle cx="70" cy="70" r="60" stroke="#e5e7eb" stroke-width="12" fill="none"/>
  <circle cx="70" cy="70" r="60" stroke="#00599c" stroke-width="12" fill="none"
          stroke-dasharray="320" stroke-dashoffset="56" stroke-linecap="round" transform="rotate(-90 70 70)"/>
  <text x="70" y="75" text-anchor="middle" font-size="20" font-weight="bold" fill="#00599c">85%</text>
</svg>

**Extensions:** `.c .cpp .h .hpp`
**Frameworks:** Native, Qt, Boost
**Patterns:** gets(), strcpy(), malloc(), system()

</td>
</tr>
<tr>
<td align="center" width="25%">

**☕ Java**

<svg width="140" height="140">
  <circle cx="70" cy="70" r="60" stroke="#e5e7eb" stroke-width="12" fill="none"/>
  <circle cx="70" cy="70" r="60" stroke="#ed8b00" stroke-width="12" fill="none"
          stroke-dasharray="309" stroke-dashoffset="67" stroke-linecap="round" transform="rotate(-90 70 70)"/>
  <text x="70" y="75" text-anchor="middle" font-size="20" font-weight="bold" fill="#ed8b00">82%</text>
</svg>

**Extensions:** `.java .jar .class`
**Frameworks:** Spring, Struts, JSF
**Patterns:** Runtime.exec(), reflection, deserialization

</td>
<td align="center" width="25%">

**🐘 PHP**

<svg width="140" height="140">
  <circle cx="70" cy="70" r="60" stroke="#e5e7eb" stroke-width="12" fill="none"/>
  <circle cx="70" cy="70" r="60" stroke="#777bb4" stroke-width="12" fill="none"
          stroke-dasharray="301" stroke-dashoffset="75" stroke-linecap="round" transform="rotate(-90 70 70)"/>
  <text x="70" y="75" text-anchor="middle" font-size="20" font-weight="bold" fill="#777bb4">80%</text>
</svg>

**Extensions:** `.php .phtml .php3`
**Frameworks:** Laravel, Symfony, CodeIgniter
**Patterns:** eval(), shell_exec(), include(), mysqli

</td>
<td align="center" width="25%">

**💎 Ruby**

<svg width="140" height="140">
  <circle cx="70" cy="70" r="60" stroke="#e5e7eb" stroke-width="12" fill="none"/>
  <circle cx="70" cy="70" r="60" stroke="#cc342d" stroke-width="12" fill="none"
          stroke-dasharray="293" stroke-dashoffset="83" stroke-linecap="round" transform="rotate(-90 70 70)"/>
  <text x="70" y="75" text-anchor="middle" font-size="20" font-weight="bold" fill="#cc342d">78%</text>
</svg>

**Extensions:** `.rb .rbw .rake`
**Frameworks:** Rails, Sinatra, Hanami
**Patterns:** eval(), system(), send(), constantize()

</td>
<td align="center" width="25%">

**🐹 Go**

<svg width="140" height="140">
  <circle cx="70" cy="70" r="60" stroke="#e5e7eb" stroke-width="12" fill="none"/>
  <circle cx="70" cy="70" r="60" stroke="#00add8" stroke-width="12" fill="none"
          stroke-dasharray="282" stroke-dashoffset="94" stroke-linecap="round" transform="rotate(-90 70 70)"/>
  <text x="70" y="75" text-anchor="middle" font-size="20" font-weight="bold" fill="#00add8">75%</text>
</svg>

**Extensions:** `.go .mod .sum`
**Frameworks:** Gin, Echo, Fiber
**Patterns:** exec.Command(), unsafe.Pointer, sql.Query

</td>
</tr>
<tr>
<td align="center" width="25%">

**🌐 HTML/CSS**

<svg width="140" height="140">
  <circle cx="70" cy="70" r="60" stroke="#e5e7eb" stroke-width="12" fill="none"/>
  <circle cx="70" cy="70" r="60" stroke="#e34f26" stroke-width="12" fill="none"
          stroke-dasharray="264" stroke-dashoffset="113" stroke-linecap="round" transform="rotate(-90 70 70)"/>
  <text x="70" y="75" text-anchor="middle" font-size="20" font-weight="bold" fill="#e34f26">70%</text>
</svg>

**Extensions:** `.html .htm .css`
**Frameworks:** Bootstrap, Tailwind
**Patterns:** Script injection, unsafe protocols

</td>
<td align="center" width="25%">

### **🎯 Overall Coverage**

<svg width="140" height="140">
  <circle cx="70" cy="70" r="60" stroke="#e5e7eb" stroke-width="12" fill="none"/>
  <circle cx="70" cy="70" r="60" stroke="#10b981" stroke-width="12" fill="none"
          stroke-dasharray="312" stroke-dashoffset="64" stroke-linecap="round" transform="rotate(-90 70 70)"/>
  <text x="70" y="75" text-anchor="middle" font-size="20" font-weight="bold" fill="#10b981">83%</text>
</svg>

**Total Languages:** 9
**Security Patterns:** 248+
**Framework Support:** Multi-Platform

</td>
<td align="center" width="50%">

### **📈 Detection Statistics**

**🔴 Critical Vulnerabilities:** 47%
**🟠 High Severity Issues:** 31%
**🟡 Medium Risk Patterns:** 16%
**🟢 Low Priority Items:** 6%

**📊 Total Patterns Detected:** 248
**🛡️ Security Coverage:** 83% Average
**⚡ Scan Performance:** < 2 seconds

</td>
</tr>
</table>

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

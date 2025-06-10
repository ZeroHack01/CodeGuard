<div align="center">

<!-- Animated Wave Header -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=250&section=header&text=CodeGuard&fontSize=70&fontColor=fff&animation=twinkling&fontAlignY=35&desc=Security%20Code%20Scanner&descAlignY=55&descSize=25" />

<br/>

<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=600&size=28&pause=1000&color=00D9FF&center=true&vCenter=true&width=700&lines=Advanced+Vulnerability+Detection;Cross-Platform+Security+Scanner;Real-Time+Code+Analysis;Multi-Language+Support" />

<br/>

![Version](https://img.shields.io/badge/VERSION-2.0.0-00D9FF?style=for-the-badge&labelColor=0a0a23&color=1a1a2e)
![Python](https://img.shields.io/badge/PYTHON-3.8+-00FF88?style=for-the-badge&labelColor=0a0a23&color=1a1a2e)
![License](https://img.shields.io/badge/LICENSE-MIT-FF3366?style=for-the-badge&labelColor=0a0a23&color=1a1a2e)
![Stars](https://img.shields.io/github/stars/ZeroHack01/CodeGuard?style=for-the-badge&labelColor=0a0a23&color=1a1a2e&label=STARS)

<br/>

**Static code analysis tool for security vulnerability detection**

[🚀 Install](#installation) • [📖 Usage](#usage) • [🔧 API](#api-reference) • [🌐 Languages](#supported-languages)

</div>

---

## ⚡ **What It Does**

CodeGuard scans source code files to identify common security vulnerabilities using pattern matching and static analysis techniques.

<table>
<tr>
<td width="50%">

**🔍 Detects:**
- Code injection (eval, exec)
- Hardcoded credentials & API keys
- Command injection vulnerabilities
- Buffer overflows (C/C++)
- XSS patterns (JavaScript/HTML)
- SQL injection risks
- Insecure cryptographic functions

</td>
<td width="50%">

**📊 Features:**
- Line-by-line vulnerability analysis
- Severity classification (Critical/High/Medium)
- Fix recommendations
- Web dashboard interface
- JSON/CSV export capabilities
- REST API for automation
- Real-time scanning results

</td>
</tr>
</table>

---

## 🚀 **Installation**

<div align="center">

### Cross-Platform Setup

</div>

<table>
<tr>
<td width="33%" align="center">

### <img src="https://img.icons8.com/color/48/000000/windows-10.png" width="24"/> Windows

```powershell
# PowerShell
git clone https://github.com/ZeroHack01/CodeGuard.git
cd CodeGuard

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch scanner
python app.py
```

</td>
<td width="33%" align="center">

### <img src="https://img.icons8.com/color/48/000000/mac-os.png" width="24"/> macOS

```bash
# Terminal
git clone https://github.com/ZeroHack01/CodeGuard.git
cd CodeGuard

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip3 install -r requirements.txt

# Launch scanner
python3 app.py
```

</td>
<td width="33%" align="center">

### <img src="https://img.icons8.com/color/48/000000/linux.png" width="24"/> Linux

```bash
# Terminal
git clone https://github.com/ZeroHack01/CodeGuard.git
cd CodeGuard

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip3 install -r requirements.txt

# Launch scanner
python3 app.py
```

</td>
</tr>
</table>

<div align="center">

### 🐳 Docker (All Platforms)

```bash
docker run -p 5000:5000 zerohack01/codeguard:latest
```

**🌐 Access:** `http://localhost:5000`

</div>

---

## 📖 **Usage**

### 🖥️ **Web Interface**

<table>
<tr>
<td width="33%" align="center">

### <img src="https://img.icons8.com/color/48/000000/windows-10.png" width="20"/> Windows
1. Open browser to `localhost:5000`
2. Drag & drop code files
3. Click "Execute Analysis"
4. Review security findings

</td>
<td width="33%" align="center">

### <img src="https://img.icons8.com/color/48/000000/mac-os.png" width="20"/> macOS
1. Open Safari/Chrome to `localhost:5000`
2. Upload files via web interface
3. Start security scan
4. Export results as needed

</td>
<td width="33%" align="center">

### <img src="https://img.icons8.com/color/48/000000/linux.png" width="20"/> Linux
1. Open Firefox to `localhost:5000`
2. Select code files for analysis
3. Run vulnerability scan
4. Download detailed reports

</td>
</tr>
</table>

### 💻 **Command Line**

```python
# Direct file scanning
from scanner import scan_file
results = scan_file('example.py')
print(results)
```

```bash
# API usage
curl -X POST -F "file=@test.py" http://localhost:5000/api/scan
```

---

## 📊 **Sample Results**

<details>
<summary><b>🔍 Click to see scan output</b></summary>

```json
{
  "filename": "vulnerable_app.py",
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
      "code": "API_KEY = 'sk-1234567890'",
      "issue": "Hardcoded Credentials",
      "severity": "High",
      "description": "API key found in source code"
    },
    {
      "line": 31,
      "code": "os.system(user_command)",
      "issue": "Command Injection",
      "severity": "High", 
      "description": "System command execution with user input"
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

## 🌐 **Supported Languages**

<div align="center">

| Language | Extensions | Key Detections |
|----------|------------|----------------|
| 🐍 **Python** | `.py .pyw` | eval(), exec(), os.system(), hardcoded secrets |
| 🟨 **JavaScript** | `.js .jsx` | innerHTML, eval(), XSS patterns, DOM manipulation |
| ⚡ **TypeScript** | `.ts .tsx` | Unsafe type assertions, XSS vulnerabilities |
| 🔵 **C/C++** | `.c .cpp .h` | gets(), strcpy(), buffer overflows, system() |
| ☕ **Java** | `.java` | Runtime.exec(), reflection attacks, path traversal |
| 🐘 **PHP** | `.php` | eval(), shell_exec(), SQL injection, file inclusion |
| 💎 **Ruby** | `.rb` | eval(), system(), command injection |
| 🐹 **Go** | `.go` | exec.Command(), unsafe operations |
| 🌐 **HTML** | `.html` | Script injection, javascript: protocols |

</div>

---

## 🔧 **API Reference**

### 📡 **Endpoints**

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/scan` | Upload and analyze file |
| `GET` | `/` | Web interface |
| `GET` | `/download/{format}/{filename}` | Export results |

### 📝 **Example Request**

```bash
curl -X POST \
  -F "file=@code.py" \
  -H "Content-Type: multipart/form-data" \
  http://localhost:5000/api/scan
```

### 📋 **Response Format**

```json
{
  "success": true,
  "filename": "code.py",
  "language": "python",
  "issues": [...],
  "total_issues": 2
}
```

---

## ⚙️ **Configuration**

<details>
<summary><b>🔧 Environment Variables</b></summary>

```bash
# Server Settings
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
FLASK_DEBUG=false

# File Limits
MAX_FILE_SIZE=10485760    # 10MB
UPLOAD_TIMEOUT=30         # 30 seconds

# Analysis Options
ENABLE_AST_ANALYSIS=true
SEVERITY_THRESHOLD=medium
EXPORT_FORMATS=json,csv
```

</details>

---

## 🧪 **Testing**

Test CodeGuard with this vulnerable sample:

```python
# test_vulnerable.py
password = "admin123"              # Hardcoded credential
eval(input("Enter code: "))        # Code injection
os.system("rm -rf " + user_path)   # Command injection
```

Expected: 3 security issues detected

---

## 🤝 **Contributing**

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Make changes and test
4. Commit: `git commit -m "Add feature"`
5. Push: `git push origin feature-name`
6. Submit Pull Request

---

## 📄 **License**

MIT License - see [LICENSE](LICENSE) file for details.

---

<!-- Animated Wave Footer -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=150&section=footer&text=Thank%20You&fontSize=40&fontColor=fff&animation=twinkling&fontAlignY=70" />

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=600&size=22&pause=1000&color=00D9FF&center=true&vCenter=true&width=500&lines=Built+by+@ZeroHack01;Star+This+Repository;Secure+Your+Code" />

<br/>

**[🐛 Issues](https://github.com/ZeroHack01/CodeGuard/issues) • [💬 Discussions](https://github.com/ZeroHack01/CodeGuard/discussions) • [📧 Contact](mailto:contact@zerohack01.dev)**

[![GitHub](https://img.shields.io/badge/GitHub-ZeroHack01-black?style=flat-square&logo=github)](https://github.com/ZeroHack01)
[![Website](https://img.shields.io/badge/Website-zerohack01.dev-blue?style=flat-square&logo=google-chrome)](https://zerohack01.dev)

**⭐ Star if this helped secure your code!**

</div>

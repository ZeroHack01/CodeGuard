# 🛡️ CodeGuard

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=32&pause=1000&color=2563EB&center=true&vCenter=true&width=500&lines=Security+Code+Scanner;Vulnerability+Detection;Multi-Language+Analysis" alt="CodeGuard" />

<br>

![Version](https://img.shields.io/badge/version-2.0.0-blue?style=flat-square)
![Python](https://img.shields.io/badge/python-3.8+-green?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-orange?style=flat-square)
![Stars](https://img.shields.io/github/stars/ZeroHack01/CodeGuard?style=flat-square&color=yellow)

**Static code analysis scanner for security vulnerability detection**

[Install](#installation) • [Usage](#usage) • [API](#api) • [Languages](#supported-languages)

</div>

---

## ⚡ **Quick Start**

```bash
git clone https://github.com/ZeroHack01/CodeGuard.git
cd CodeGuard
pip install -r requirements.txt
python app.py
```

**Web Interface:** http://localhost:5000

---

## 🎯 **What It Does**

CodeGuard scans source code files to identify common security vulnerabilities using pattern matching and static analysis.

<table>
<tr>
<td width="50%">

**🔍 Detects:**
- Code injection (eval, exec)
- Hardcoded credentials
- Command injection  
- Buffer overflows (C/C++)
- XSS patterns (JavaScript)
- SQL injection risks
- Insecure functions

</td>
<td width="50%">

**📊 Provides:**
- Line-by-line analysis
- Severity classification
- Fix recommendations
- JSON/CSV exports
- Web dashboard
- REST API access

</td>
</tr>
</table>

---

## 🚀 **Installation**

### Standard Install
```bash
git clone https://github.com/ZeroHack01/CodeGuard.git
cd CodeGuard
pip install -r requirements.txt
python app.py
```

### Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
python app.py
```

### Docker
```bash
docker run -p 5000:5000 zerohack01/codeguard
```

---

## 📖 **Usage**

### Web Interface
1. Open http://localhost:5000
2. Upload code file
3. Click "Execute Analysis"
4. Review results

### Command Line
```python
from scanner import scan_file
results = scan_file('example.py')
print(results)
```

### API Call
```bash
curl -X POST -F "file=@test.py" http://localhost:5000/api/scan
```

---

## 📋 **Sample Results**

```json
{
  "filename": "app.py",
  "language": "python", 
  "issues": [
    {
      "line": 15,
      "code": "eval(user_input)",
      "issue": "Code Injection",
      "severity": "Critical"
    },
    {
      "line": 8,
      "code": "password = 'admin123'", 
      "issue": "Hardcoded Password",
      "severity": "High"
    }
  ],
  "total_issues": 2
}
```

---

## 🌐 **Supported Languages**

<div align="center">

| Language | Extensions | Key Patterns |
|----------|------------|--------------|
| Python | `.py` | eval(), exec(), os.system() |
| JavaScript | `.js`, `.jsx`, `.ts` | innerHTML, eval(), XSS |
| C/C++ | `.c`, `.cpp`, `.h` | gets(), strcpy(), system() |
| Java | `.java` | Runtime.exec(), reflection |
| PHP | `.php` | eval(), shell_exec(), include |
| Ruby | `.rb` | eval(), system() |
| Go | `.go` | exec.Command(), unsafe |
| HTML | `.html` | script tags, javascript: |

</div>

---

## 🔌 **API**

### POST /api/scan
Upload and analyze file

**Request:**
```bash
curl -X POST -F "file=@code.py" http://localhost:5000/api/scan
```

**Response:**
```json
{
  "success": true,
  "filename": "code.py",
  "issues": [...],
  "total_issues": 3
}
```

### GET /download/{format}/{filename}
Export results as JSON or CSV

---

## ⚙️ **Configuration**

Environment variables:

```bash
FLASK_HOST=0.0.0.0        # Server host
FLASK_PORT=5000           # Server port  
MAX_FILE_SIZE=10485760    # 10MB file limit
UPLOAD_TIMEOUT=30         # Upload timeout
```

---

## 🧪 **Testing**

Test with sample vulnerable code:

```python
# test.py - Contains vulnerabilities
password = "secret123"           # Hardcoded credential
eval(input("Enter code: "))      # Code injection
os.system("ls " + user_path)     # Command injection
```

Expected output: 3 security issues detected

---

## 🤝 **Contributing**

1. Fork repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Add feature"`
4. Push branch: `git push origin feature-name`
5. Submit pull request

---

## 📄 **License**

MIT License - see [LICENSE](LICENSE) file

---

<div align="center">

**Built by [@ZeroHack01](https://github.com/ZeroHack01)**

[🐛 Report Issues](https://github.com/ZeroHack01/CodeGuard/issues) • [💬 Discussions](https://github.com/ZeroHack01/CodeGuard/discussions) • [📧 Contact](mailto:contact@zerohack01.dev)

⭐ **Star if this helped secure your code!**

</div>

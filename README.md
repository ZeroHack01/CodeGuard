# 🛡️ CodeGuard - Security Scanner

<div align="center">

![Version](https://img.shields.io/badge/Version-2.0.0-brightgreen?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-orange?style=flat-square)

**Advanced code security analysis tool with modern web interface**

*Detect vulnerabilities • Generate reports • Secure your code*

</div>

---

## 🚀 **Features**

- 🔍 **Multi-Language Support** - Python, JavaScript, C/C++, Java, PHP, Ruby, Go, HTML
- 🌐 **Web Interface** - Modern drag & drop file upload with real-time analysis
- 🛡️ **50+ Security Patterns** - Code injection, XSS, SQL injection, buffer overflow detection
- 📊 **Detailed Reports** - Line-by-line vulnerability analysis with severity levels
- ⚡ **Fast Scanning** - Average scan time under 1 second
- 🔧 **API Integration** - RESTful API for automated security scanning

---

## 📦 **Installation**

### Quick Install

```bash
# Clone repository
git clone https://github.com/ZeroHack01/CodeGuard.git
cd CodeGuard

# Install dependencies
pip install -r requirements.txt

# Run scanner
python app.py
```

### Using Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv codeguard_env

# Activate (Windows)
codeguard_env\Scripts\activate

# Activate (macOS/Linux)
source codeguard_env/bin/activate

# Install and run
pip install -r requirements.txt
python app.py
```

**Access web interface:** http://localhost:5000

---

## 🎯 **Usage**

### Web Interface
1. Open http://localhost:5000 in your browser
2. Drag & drop your code files or click to browse
3. Click "Execute Analysis" 
4. Review security issues and recommendations

### Command Line
```bash
# Scan single file
python -c "from scanner import scan_file; print(scan_file('example.py'))"

# API usage
curl -X POST -F "file=@test.py" http://localhost:5000/api/scan
```

---

## 🔍 **Supported Languages**

| Language | Extensions | Vulnerability Patterns |
|----------|------------|------------------------|
| Python | `.py` | Code injection, hardcoded secrets, command injection |
| JavaScript | `.js`, `.jsx`, `.ts` | XSS, DOM manipulation, eval() usage |
| C/C++ | `.c`, `.cpp`, `.h` | Buffer overflow, unsafe functions |
| Java | `.java` | Command execution, reflection injection |
| PHP | `.php` | Code injection, SQL injection, XSS |
| Ruby | `.rb` | Code injection, command execution |
| Go | `.go` | Command execution, unsafe operations |
| HTML | `.html` | Script injection, unsafe protocols |

---

## 📋 **Sample Output**

```bash
🛡️ Analysis Report
══════════════════════════════════════

📁 File: vulnerable.py
🔍 Language: Python
⏱️ Scan Time: 0.8s

🚨 Issues Found:

🔥 [CRITICAL] Code Injection
   Line 23: eval(user_input)
   Fix: Use ast.literal_eval() instead

⚠️ [HIGH] Hardcoded API Key  
   Line 15: API_KEY = "secret123"
   Fix: Move to environment variables

💡 [MEDIUM] Weak Random Generation
   Line 8: random.randint(1000, 9999)
   Fix: Use secrets module for crypto

📊 Summary: 3 issues found (1 Critical, 1 High, 1 Medium)
```

---

## 🔧 **Configuration**

Create `.env` file for custom settings:

```bash
# Server settings
FLASK_HOST=0.0.0.0
FLASK_PORT=5000

# File limits
MAX_FILE_SIZE=10485760  # 10MB
UPLOAD_TIMEOUT=30       # seconds

# Analysis options
ENABLE_AST_ANALYSIS=true
SEVERITY_THRESHOLD=medium
```

---

## 🛠️ **API Reference**

### POST /api/scan
Upload and scan a file for vulnerabilities.

**Request:**
```bash
curl -X POST -F "file=@example.py" http://localhost:5000/api/scan
```

**Response:**
```json
{
  "success": true,
  "filename": "example.py",
  "issues": [
    {
      "line": 23,
      "code": "eval(user_input)",
      "issue": "Code Injection",
      "severity": "Critical"
    }
  ],
  "total_issues": 1
}
```

---

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make your changes and test
4. Commit: `git commit -m "Add new feature"`
5. Push: `git push origin feature/new-feature`
6. Create a Pull Request

---

## 📞 **Support**

- 🐛 **Issues**: [GitHub Issues](https://github.com/ZeroHack01/CodeGuard/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/ZeroHack01/CodeGuard/discussions)
- 📧 **Contact**: contact@zerohack01.dev

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with ❤️ by [@ZeroHack01](https://github.com/ZeroHack01)**

⭐ **Star this repo if you find it useful!**

</div>

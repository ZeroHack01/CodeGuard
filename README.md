<div align="center">

<!-- Animated Wave Header -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,6,15&height=250§ion=header&text=CodeGuard&fontSize=70&fontColor=fff&animation=twinkling&fontAlignY=38&desc=🛡️%20Secure%20Your%20Code%20with%20Confidence&descAlignY=55&descSize=24" />

<br/>

<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=600&size=28&pause=1000&color=00D9FF¢er=true&vCenter=true&width=600&lines=Advanced+Static+Code+Analysis;Real-Time+Vulnerability+Detection;Multi-Language+Security+Scanning" />

<br/>

<image-card alt="Version" src="https://img.shields.io/badge/VERSION-2.0.0-00D9FF?style=flat-square&labelColor=0a0a23&color=1a1a2e" ></image-card>
<image-card alt="Python" src="https://img.shields.io/badge/PYTHON-3.8+-00FF88?style=flat-square&labelColor=0a0a23&color=1a1a2e" ></image-card>
<image-card alt="License" src="https://img.shields.io/badge/LICENSE-MIT-FF3366?style=flat-square&labelColor=0a0a23&color=1a1a2e" ></image-card>
<image-card alt="Stars" src="https://img.shields.io/github/stars/ZeroHack01/CodeGuard?style=flat-square&labelColor=0a0a23&color=1a1a2e&label=STARS" ></image-card>

<br/>

**🔍 A powerful static code analyzer for detecting security vulnerabilities across multiple languages**

[🚀 Get Started](#installation) | [📱 Web Interface](#web-interface) | [📖 Documentation](#usage) | [🔧 API](#api) | [🌐 Languages](#languages)

</div>

---

## 🛡️ **Why CodeGuard?**

CodeGuard is an advanced static code analysis tool designed to identify and mitigate security vulnerabilities with precision. It offers real-time scanning, detailed reporting, and seamless integration for developers and security professionals.

<div align="center">

| **🔍 Security Capabilities** | **🚀 Professional Features** |
|-----------------------------|-----------------------------|
| Code & Command Injection    | Real-Time Scanning         |
| Hardcoded Secrets           | Severity-Based Reporting   |
| XSS & CSRF Vulnerabilities  | Auto-Fix Suggestions       |
| SQL Injection Detection     | JSON, CSV, HTML Reports    |
| Weak Cryptography           | Interactive Web Dashboard  |
| Buffer Overflows (C/C++)    | REST API & CI/CD Support   |

</div>

---

## 🚀 **Installation**

### 🌍 **Cross-Platform Setup**

<div align="center">

| **🪟 Windows** | **🍎 macOS** | **🐧 Linux** |
|---------------|-------------|-------------|
| ```powershell<br>git clone https://github.com/ZeroHack01/CodeGuard.git<br>cd CodeGuard<br>python -m venv venv<br>venv\Scripts\activate<br>pip install -r requirements.txt<br>python app.py<br>```<br>**Access:** `http://localhost:5000` | ```bash<br>git clone https://github.com/ZeroHack01/CodeGuard.git<br>cd CodeGuard<br>python3 -m venv venv<br>source venv/bin/activate<br>pip3 install -r requirements.txt<br>python3 app.py<br>```<br>**Access:** `http://localhost:5000` | ```bash<br>sudo apt update && sudo apt install -y python3 python3-pip git<br>git clone https://github.com/ZeroHack01/CodeGuard.git<br>cd CodeGuard<br>python3 -m venv venv<br>source venv/bin/activate<br>pip3 install -r requirements.txt<br>python3 app.py<br>```<br>**Access:** `http://localhost:5000` |

</div>

### 🐳 **Docker**

```bash
# Pull from Docker Hub
docker pull zerohack01/codeguard:latest
docker run -d -p 5000:5000 zerohack01/codeguard:latest

# Or build from source
git clone https://github.com/ZeroHack01/CodeGuard.git
cd CodeGuard
docker build -t codeguard .
docker run -d -p 5000:5000 codeguard
🌐 Access: http://localhost:5000

📱 Web Interface

<image-card alt="Dashboard](https://raw.githubusercontent.com/ZeroHack01/CodeGuard/main/screenshots/dashboard.png) Interactive Dashboard	Drag & Drop Upload	![Results" src="https://raw.githubusercontent.com/ZeroHack01/CodeGuard/main/screenshots/results.png" > Detailed Reporting
📖 Usage
🖥️ Web Interface
Open http://localhost:5000 in your browser
Upload code files via drag-and-drop
Run the scan and review detailed results
Export reports in JSON, CSV, or HTML
💻 CLI & API
python

Collapse

Wrap

Run

Copy
# CLI Example
from scanner import scan_file
results = scan_file('app.py')
for issue in results:
    print(f"🚨 {issue['line']}: {issue['issue']} ({issue['severity']})")
bash

Collapse

Wrap

Run

Copy
# API Example
curl -X POST -F "file=@app.py" http://localhost:5000/api/scan
🌐 Languages
CodeGuard supports a wide range of programming languages with comprehensive security pattern detection.


Grok can make mistakes. Always check original sources.
Download
Supported Frameworks:

Python: Django, Flask, FastAPI
JavaScript/TypeScript: React, Vue, Angular
C/C++: Qt, Boost
Java: Spring, Struts
PHP: Laravel, Symfony
Ruby: Rails, Sinatra
Go: Gin, Echo
🔧 API
Endpoints

Method	Endpoint	Description	Parameters
POST	/api/scan	Scan uploaded file	file (multipart)
GET	/	Web interface	None
Example
bash

Collapse

Wrap

Run

Copy
curl -X POST -F "file=@app.py" -H "Accept: application/json" http://localhost:5000/api/scan
Response:

json

Collapse

Wrap

Copy
{
  "success": true,
  "filename": "app.py",
  "language": "python",
  "issues": [
    {
      "line": 10,
      "issue": "Code Injection",
      "severity": "Critical",
      "code": "eval(input())"
    }
  ],
  "total_issues": 1
}
🧪 Test It Out
Create a test file:

python

Collapse

Wrap

Run

Copy
# test.py
api_key = "sk-123456"  # Hardcoded secret
eval(input())           # Code injection
Run: curl -X POST -F "file=@test.py" http://localhost:5000/api/scan

Expected: 2 issues (Hardcoded Secret, Code Injection)

🤝 Contributing
Fork the repo
Create a branch: git checkout -b feature/new-detection
Commit changes: git commit -m "Add new detection"
Push: git push origin feature/new-detection
Submit a Pull Request
Issues & Features: Use GitHub Issues

Security Reports: Email mongwoiching2080@gmail.com

📄 License
MIT License - see LICENSE for details.

Dependencies: Flask, Werkzeug, and more (see requirements.txt)


[
Failed to load image

View link


⭐ Star this repo to support secure coding!

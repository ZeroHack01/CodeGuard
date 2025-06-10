<div align="center">
  <img src="https://user-images.githubusercontent.com/58953348/187422368-8748c148-525a-472e-b695-d3683a37542d.png" alt="CodeGuard Logo" width="150"/>
  <h1>🛡️ CodeGuard</h1>
  <p><strong>Your vigilant shield against malicious code lurking in your files.</strong></p>
  
  <p>
    <a href="https://github.com/ZeroHack01/CodeGuard/stargazers"><img src="https://img.shields.io/github/stars/ZeroHack01/CodeGuard?style=for-the-badge&logo=github&color=FFC107" alt="Stars"></a>
    <a href="https://github.com/ZeroHack01/CodeGuard/network/members"><img src="https://img.shields.io/github/forks/ZeroHack01/CodeGuard?style=for-the-badge&logo=github&color=4CAF50" alt="Forks"></a>
    <a href="https://github.com/ZeroHack01/CodeGuard/blob/main/LICENSE"><img src="https://img.shields.io/github/license/ZeroHack01/CodeGuard?style=for-the-badge&color=2196F3" alt="License"></a>
    <a href="#"><img src="https://img.shields.io/badge/python-3.x-blue.svg?style=for-the-badge&logo=python" alt="Python 3.x"></a>
  </p>
</div>

---

CodeGuard is a simple yet powerful Python command-line tool designed to detect and optionally remove known malicious code patterns from your files. Whether you're dealing with a compromised web server, a suspicious download, or just want to perform a security audit, CodeGuard helps you find and neutralize threats quickly.

## ✨ Key Features

-   **📁 Directory Scanning**: Recursively scan entire directories for threats.
-   **🎯 Pattern-Based Detection**: Uses a curated list of regular expressions to identify common malware, webshells (like c99, r57), and suspicious functions (`eval`, `base64_decode`, `exec`, etc.).
-   **🔍 Scan-Only Mode**: Safely detect threats without modifying any files.
-   **✂️ Removal Mode**: Automatically remove detected malicious code snippets.
-   **📝 Detailed Logging**: Keeps a log (`codeguard.log`) of all findings and actions taken.
-   **🪶 Lightweight & Dependency-Free**: No `pip install` needed. It runs with standard Python libraries!

## 🚀 Getting Started

Getting started with CodeGuard is as simple as cloning the repository.

### Prerequisites

-   Python 3.x

### Installation

1.  Clone the repository to your local machine:
    ```sh
    git clone https://github.com/ZeroHack01/CodeGuard.git
    ```

2.  Navigate to the cloned directory:
    ```sh
    cd CodeGuard
    ```

That's it! No further installation is required.

## 🕹️ Usage

CodeGuard is run from the command line. You can choose to either `--scan` for threats or `--remove` them.

### Basic Command Structure

```sh
python CodeGuard.py [MODE] --path [FILE_OR_DIRECTORY_PATH]
Use code with caution.
Markdown
Examples
1. Scan a single file for malicious code
This will check suspicious_file.php for threats and report them in the console and codeguard.log, without changing the file.
python CodeGuard.py --scan --path /var/www/html/suspicious_file.php
Use code with caution.
Sh
2. Scan an entire directory recursively
This will scan every file in the /var/www/html directory and all its subdirectories.
python CodeGuard.py --scan --path /var/www/html
Use code with caution.
Sh
3. Remove malicious code from a single file
This will find and remove malicious patterns from infected_file.py.
python CodeGuard.py --remove --path /path/to/infected_file.py
Use code with caution.
Sh
4. Clean an entire directory
This will scan and remove threats from all files in the specified directory. Use with extreme caution!
python CodeGuard.py --remove --path /var/www/html
Use code with caution.
Sh
🎬 Demo
Here’s a simulation of creating a malicious file, scanning it, and then cleaning it with CodeGuard.
# 1. Create a directory for our test
mkdir my_project
cd my_project

# 2. Create a dummy file with a common obfuscated backdoor
echo "<?php eval(base64_decode('aWYo……')); ?>" > backdoor.php
echo "This is a safe file." > safe.php

# 3. Run CodeGuard in SCAN mode
python ../CodeGuard.py --scan --path .

# --- Expected Output (in console and codeguard.log) ---
# INFO: [SCAN] Found malicious pattern 'eval(base64_decode(...))' in file: ./backdoor.php
# INFO: Scan complete. Found 1 potential threat(s).

# 4. Now, run CodeGuard in REMOVE mode
python ../CodeGuard.py --remove --path .

# --- Expected Output (in console and codeguard.log) ---
# INFO: [SCAN] Found malicious pattern 'eval(base64_decode(...))' in file: ./backdoor.php
# WARNING: [REMOVE] Removing malicious code from: ./backdoor.php
# INFO: Scan complete. Found 1 potential threat(s). 1 file(s) cleaned.

# 5. Check the file content. The malicious code is gone!
cat backdoor.php
# --- Output ---
# <?php  ?>
Use code with caution.
Sh
🚨 Important: Use With Caution!
The --remove feature directly modifies your files by deleting lines that match the malicious patterns. This action is irreversible.
ALWAYS create a backup of your files and directories before running the --remove command. You are responsible for any data loss that may occur.
🛠️ How It Works
CodeGuard maintains a dictionary of regular expression patterns in CodeGuard.py. These patterns are designed to catch common signatures of malicious code. The script reads each file and checks its content against every pattern.
You can easily extend CodeGuard's capabilities by adding new patterns to the patterns dictionary in the script.
🙌 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.
Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Add new detection patterns or improve the code.
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request
📄 License
Distributed under the MIT License. See LICENSE for more information.
<div align="center">
<p>Made with ❤️ by ZeroHack01</p>
</div>

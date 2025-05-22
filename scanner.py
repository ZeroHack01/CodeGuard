# scanner.py
import re

def get_language(file_path):
    ext = file_path.split('.')[-1].lower()
    return {
        'py': 'python',
        'js': 'javascript',
        'php': 'php',
        'html': 'html',
        'sh': 'shell',
        'java': 'java',
        'c': 'c',
        'cpp': 'cpp'
    }.get(ext, 'unknown')

def scan_file(file_path):
    issues = []
    language = get_language(file_path)

    patterns = {
        'python': {
            "eval() - Code Injection": r"\beval\s*\(",
            "exec() - Dangerous Execution": r"\bexec\s*\(",
            "os.system() - Shell Execution": r"os\.system\s*\(",
            "subprocess call": r"subprocess\.(call|run|Popen)",
            "Hardcoded password": r"password\s*=\s*[\"'].*[\"']"
        },
        'javascript': {
            "document.write() - XSS risk": r"document\.write\s*\(",
            "eval() - Code Injection": r"\beval\s*\("
        },
        'php': {
            "eval() in PHP - Code Injection": r"\beval\s*\(",
            "Hardcoded DB password": r"\$password\s*=\s*[\"'].*[\"']"
        },
        'shell': {
            "Dangerous eval in shell": r"eval\s+\$?\(",
            "rm -rf used": r"rm\s+-rf\s+",
            "curl | bash detected": r"curl.*\|\s*bash"
        },
        'java': {
            "Runtime.exec() - Shell Execution": r"Runtime\.getRuntime\(\)\.exec\s*\(",
            "Hardcoded password": r"String\s+password\s*=\s*[\"'].*[\"']"
        },
        'c': {
            "gets() - Buffer Overflow": r"\bgets\s*\(",
            "system() - Shell Execution": r"\bsystem\s*\("
        },
        'cpp': {
            "gets() - Buffer Overflow": r"\bgets\s*\(",
            "system() - Shell Execution": r"\bsystem\s*\("
        },
        'html': {
            "Inline script": r"<script>.*</script>"
        }
    }

    try:
        with open(file_path, 'r', errors='ignore') as f:
            code = f.read()
            lines = code.splitlines()
            language_patterns = patterns.get(language, {})
            for line_num, line in enumerate(lines, start=1):
                for message, pattern in language_patterns.items():
                    if re.search(pattern, line):
                        issues.append((line_num, line.strip(), message))

            if language == "python":
                try:
                    compile(code, file_path, 'exec')
                except SyntaxError as e:
                    issues.append((e.lineno, lines[e.lineno - 1].strip(), f"Syntax Error: {str(e)}"))

    except Exception as e:
        issues.append((0, "Error", f"Failed to scan file: {str(e)}"))

    return issues

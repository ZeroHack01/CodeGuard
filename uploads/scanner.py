import re

def scan_file(file_path):
    issues = []
    try:
        with open(file_path, 'r', errors='ignore') as f:
            content = f.read()
            if "eval(" in content:
                issues.append("⚠️ Use of eval() - risky for code injection.")
            if re.search(r"SELECT\s+\*\s+FROM\s+\w+", content, re.IGNORECASE):
                issues.append("⚠️ SQL query without WHERE clause.")
            if "document.write(" in content:
                issues.append("⚠️ document.write() - potential XSS.")
            if "password" in content:
                issues.append("⚠️ Hardcoded password found.")
    except Exception as e:
        issues.append(f"Error reading file: {str(e)}")
    return issues

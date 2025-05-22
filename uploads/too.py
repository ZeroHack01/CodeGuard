import os
import subprocess

password = "secret123"  # hardcoded password

def get_user_input():
    return input("Enter command: ")

def insecure_eval():
    user_code = get_user_input()
    eval(user_code)  # eval injection

def dangerous_sql():
    query = "SELECT * FROM users"
    print("Query:", query)

def run_shell_command():
    os.system("ls -la")  # command injection
    subprocess.call("echo hello", shell=True)  # subprocess risk

def main():
    insecure_eval()
    dangerous_sql()
    run_shell_command()

main()

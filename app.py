"""
WARNING: This application contains intentionally vulnerable code for security scanning purposes.
DO NOT deploy this in a production environment.

This script is used to test security scanning tools and demonstrate common vulnerabilities.
"""

import hashlib
import logging
import pickle
import subprocess

from flask import Flask, request

app = Flask(__name__)


# SQL Injection vulnerability
@app.route("/user/<username>")
def get_user(username):
    query = (
        f"SELECT * FROM users WHERE username = '{username}'"  # No input sanitization
    )
    return f"Query executed: {query}"


# Command Injection vulnerability
@app.route("/ping")
def ping():
    target = request.args.get("target", "127.0.0.1")
    result = subprocess.check_output(
        f"ping -c 1 {target}", shell=True
    )  # User input directly in shell command
    return result.decode()


# Hardcoded API Key (Detected by secret scanning tools)
API_KEY = "sk_test_1234567890abcdef"
SLACK_TOKEN = "xoxb-1234567890-abcdefghij1234567890-xyz123456789"


# Insecure Deserialization vulnerability
@app.route("/deserialize", methods=["POST"])
def deserialize():
    data = request.data
    obj = pickle.loads(data)  # Untrusted data deserialization
    return str(obj)


# Directory Traversal vulnerability
@app.route("/readfile")
def read_file():
    filename = request.args.get("file", "default.txt")
    with open(f"/var/data/{filename}", "r") as f:  # No path validation
        return f.read()


# XSS (Cross-Site Scripting) vulnerability
@app.route("/greet")
def greet():
    name = request.args.get("name", "Guest")
    return f"<h1>Hello, {name}</h1>"  # No HTML escaping


# Insecure Random Number Generation
@app.route("/token")
def generate_token():
    import random

    token = random.randint(1, 1000)  # Weak random number generation
    return f"Your token: {token}"


# Unsafe eval() usage
@app.route("/calculate", methods=["POST"])
def calculate():
    expression = request.form.get("expr", "1+1")
    result = eval(expression)  # Dangerous execution of user input
    return f"Result: {result}"


# Weak Cryptographic Hash (MD5)
@app.route("/hash")
def hash_password():
    password = request.args.get("password", "default")
    hashed = hashlib.md5(password.encode()).hexdigest()  # Weak MD5 hash
    return f"Hashed password: {hashed}"


# Improper Logging of Sensitive Data
@app.route("/login")
def login():
    username = request.args.get("username", "anonymous")
    password = request.args.get("password", "secret")
    logging.basicConfig(filename="app.log")
    logging.info(
        f"Login attempt: {username} with password {password}"
    )  # Logging sensitive data
    return "Logged in"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

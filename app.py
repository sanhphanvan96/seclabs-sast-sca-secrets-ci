"""
WARNING: This application contains intentionally vulnerable code for security scanning purposes.
DO NOT deploy this in a production environment.

This script is used to test security scanning tools and demonstrate common vulnerabilities.
"""

from flask import Flask, request
import subprocess
import os
import pickle

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

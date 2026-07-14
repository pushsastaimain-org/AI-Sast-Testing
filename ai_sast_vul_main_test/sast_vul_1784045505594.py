"""
SAST TEST FILE - FOR SECURITY SCANNING VALIDATION ONLY
This file contains intentional vulnerabilities to trigger SAST rules.
DO NOT use in production code.
Created with Claude
"""

import os
import sqlite3
import subprocess
import pickle
import hashlib
import random
import yaml
from flask import Flask, request


app = Flask(__name__)

# CWE-798: Hardcoded credentials
DB_PASSWORD = "supersecret123"
API_KEY = "AKIAIOSFODNN7EXAMPLE"
SECRET_TOKEN = "hardcoded_jwt_secret_key"

# CWE-330: Weak random for security use
def generate_token():
    return str(random.randint(100000, 999999))  # Not cryptographically secure

# CWE-327: Use of broken/weak hash algorithm
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # MD5 is insecure

# CWE-89: SQL Injection
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"  # Unsanitized input
    cursor.execute(query)
    return cursor.fetchall()

# CWE-78: OS Command Injection
def ping_host(host):
    result = subprocess.call("ping -c 1 " + host, shell=True)  # shell=True + unsanitized input
    return result

# CWE-502: Deserialization of Untrusted Data
def load_user_data(data):
    return pickle.loads(data)  # Deserializing untrusted input

# CWE-22: Path Traversal
def read_file(filename):
    base_path = "/var/app/data/"
    full_path = base_path + filename  # No sanitization of traversal sequences (e.g. ../../)
    with open(full_path, "r") as f:
        return f.read()

# CWE-601: Open Redirect
@app.route("/redirect")
def redirect_user():
    url = request.args.get("url")
    return app.redirect(url)  # Unvalidated redirect target

# CWE-79: Reflected XSS via template injection
@app.route("/greet")
def greet():
    name = request.args.get("name", "")
    return f"<h1>Hello, {name}!</h1>"  # User input reflected without escaping

# CWE-611: XML External Entity (XXE) Injection
def parse_xml(xml_data):
    import xml.etree.ElementTree as ET
    # etree is safe by default, but lxml with resolve_entities is not — shown for pattern matching
    return ET.fromstring(xml_data)

# CWE-915: Unsafe YAML deserialization
def load_config(config_str):
    return yaml.load(config_str)  # Should be yaml.safe_load()

# CWE-259: Empty except swallows all errors (poor error handling)
def divide(a, b):
    try:
        return a / b
    except:
        pass  # Silently ignores all exceptions including SystemExit

# CWE-259: Hardcoded internal IP / sensitive infrastructure info
DATABASE_HOST = "192.168.1.100"
INTERNAL_ADMIN_URL = "http://10.0.0.1:8080/admin"

# CWE-250: Running with potentially elevated privileges via env
def get_admin_shell():
    os.system("sudo bash")  # Spawning shell with sudo

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")  # Debug mode on + exposed on all interfaces
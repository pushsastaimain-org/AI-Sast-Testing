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


DB_PASSWORD = "supersecret123"
API_KEY = "AKIAIOSFODNN7EXAMPLE"
SECRET_TOKEN = "hardcoded_jwt_secret_key"


def generate_token():
    return str(random.randint(100000, 999999))


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()


def ping_host(host):
    result = subprocess.call("ping -c 1 " + host, shell=True)
    return result

def checkout_branch(branch_name):
    subprocess.call(["git", "checkout", branch_name])


def load_user_data(data):
    return pickle.loads(data) 

def read_file(filename):
    base_path = "/var/app/data/"
    full_path = base_path + filename 
    with open(full_path, "r") as f:
        return f.read()

@app.route("/redirect")
def redirect_user():
    url = request.args.get("url")
    return app.redirect(url) 

@app.route("/greet")
def greet():
    name = request.args.get("name", "")
    return f"<h1>Hello, {name}!</h1>" 

def parse_xml(xml_data):
    import xml.etree.ElementTree as ET

    return ET.fromstring(xml_data)

def load_config(config_str):
    return yaml.load(config_str) 

def divide(a, b):
    try:
        return a / b
    except:
        pass 

DATABASE_HOST = "192.168.1.100"
INTERNAL_ADMIN_URL = "http://10.0.0.1:8080/admin"

def get_admin_shell():
    os.system("sudo bash") 

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0") 
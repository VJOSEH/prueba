from flask import Flask, request
import os
import sqlite3

app = Flask(__name__)

# ❌ Hardcoded secret
SECRET_KEY = "123456"

# ❌ SQL Injection
@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)

    result = cursor.fetchall()
    return str(result)

# ❌ Command Injection
@app.route('/ping')
def ping():
    host = request.args.get('host')
    return os.popen(f"ping -c 1 {host}").read()

# ❌ Debug mode activo (mala práctica)
if __name__ == "__main__":
    app.run(debug=True)
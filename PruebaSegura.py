import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping():
    host = request.args.get('host')
    
    response = os.popen(f"ping -c 1 {host}").read()
    
    return f"<pre>{response}</pre>"

if __name__ == "__main__":
    app.run(debug=True)
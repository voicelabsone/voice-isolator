import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ Voice isolator API is live!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5080)
@app.route("/")
def home():
    return "Voice Isolator API is live!"
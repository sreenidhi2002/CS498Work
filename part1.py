from flask import Flask, request
import subprocess
import socket

seed_val = 0
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def find_seed():
    global seed_val
    if request.method == 'POST':
        seed_val += request.json["num"]
        return "POST done"
    elif request.method == 'GET':
        return str(seed_val)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
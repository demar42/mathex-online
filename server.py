import os
from flask import Flask, render_template
from flask_socketio import SocketIO
import json

app = Flask(__name__)
sio = SocketIO(app)

@app.route('/')
def index():
    return render_template("index_2.html")

@sio.on('send_message')
def handle_source(json_data):
    text = str(json_data['message'])
    sio.emit('echo', {'echo' : 'Server Says: ' + text})
    print(text)

@sio.on('answer')
def check_answer(data):
    if data == '72':
        result = True
    else:
        result = False
    sio.emit('resp', result)

if __name__ == "__main__":
    sio.run(app, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
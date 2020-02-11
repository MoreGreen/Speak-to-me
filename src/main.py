#arquivo principal

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRETE_KEY'] ='secret3'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handlerMessage(message):
    print('Message: ' + message)
    send(message,broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
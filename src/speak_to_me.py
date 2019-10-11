from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handler_message(msg):
    print("Message: " + msg)
    send(msg,broadcast=True)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
    socketio.run(app)
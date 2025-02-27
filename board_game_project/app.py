from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('roll_dice')
def handle_roll_dice():
    dice_value = random.randint(1, 9)
    emit('dice_result', {'value': dice_value})

if __name__ == '__main__':
    socketio.run(app)
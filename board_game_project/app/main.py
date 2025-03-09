from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from app.game_logic import Game

app = Flask(__name__)
socketio = SocketIO(app)
game = Game()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('roll_dice')
def handle_roll_dice():
    dice_value = game.roll_dice()
    game.move_player(dice_value)
    square_content = game.get_current_square_content()
    emit('dice_result', {'value': dice_value, 'content': square_content, 'position': game.current_position})

@app.teardown_appcontext
def shutdown_session(exception=None):
    game.close_connection()

if __name__ == '__main__':
    socketio.run(app, debug=True)

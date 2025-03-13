import socketio
import eventlet
from flask import Flask, render_template_string
import random

# --- Constants (Matching Client) ---
TOKEN_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
TOKEN_EMOJIS = ["👾", "🤖", "👽", "👻", "💀", "🤖"]

# --- Flask and SocketIO Setup ---
sio = socketio.Server()
app = Flask(__name__)

# --- Game Data ---
tokens = [
    {'position': 0, 'emoji_index': 0, 'color_index': 0},  # Red 👾
    {'position': 0, 'emoji_index': 1, 'color_index': 1},  # Green 🤖
    {'position': 0, 'emoji_index': 2, 'color_index': 2},  # Blue 👽
    {'position': 0, 'emoji_index': 3, 'color_index': 3},  # Yellow 👻
    {'position': 0, 'emoji_index': 4, 'color_index': 4},  # Purple 💀
    {'position': 0, 'emoji_index': 5, 'color_index': 5},  # Cyan 🤖
    {'position': 0}, # This will draw the token.png
]
# --- SocketIO Event Handlers ---

@sio.event
def connect(sid, environ):
    print(f"Client connected: {sid}")
    sio.emit('game_start', {'tokens': tokens}, room=sid)

@sio.event
def disconnect(sid):
    print(f"Client disconnected: {sid}")

@sio.on('roll_dice')
def roll_dice(sid):
    print(f"Client {sid} rolled the dice")
    dice_result = random.randint(1, 6)
    new_position = dice_result
    content = f"You rolled a {dice_result}!"
    sio.emit('dice_result', {'position': new_position, 'content': content}, room=sid)

# --- Flask Routes (Optional) ---
@app.route('/')
def index():
    return render_template_string("<h1>Board Game Server</h1>")

# --- Run the Server ---
if __name__ == '__main__':
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

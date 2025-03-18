from flask import Flask, render_template
from setup_database import SimpleDatabase
import random
app = Flask(__name__)
database = SimpleDatabase()
# Initialize your database with topics and paragraphs
def setup_squares():
    for i in range(1, 65):  # 64 squares
        database.insert(f"square_{i}", {
            "color": "gray",
            "subject": f"Topic {i}",
            "paragraphs": [f"Paragraph {j} for Topic {i}" for j in range(1, 4)]
        })
setup_squares()
@app.route('/')
def home():
    return render_template('index.html', squares=database.data)
@app.route('/move/<int:player_id>')
def move_player(player_id):
    # Implement player movement logic here (you can store player state in a session or database)
    # For demonstration, we'll just return the player's new position
    dice_roll = random.randint(1, 6)
    new_position = (player_id + dice_roll) % 64  # Example of moving the player
    square_info = database.fetch(f"square_{new_position + 1}")
    return {
        "new_position": new_position + 1,
        "subject": square_info["subject"],
        "paragraphs": square_info["paragraphs"]
    }
if __name__ == '__main__':
    app.run(debug=True)
import random
from setup_database import SimpleDatabase
class GameLogic:
    def __init__(self):
        self.players = []
        self.current_turn = 0
        self.database = SimpleDatabase()
        self.setup_squares()  # Initialize squares
    def setup_squares(self):
        # Simulating square setup with topics and paragraphs
        for i in range(1, 65):  # 64 squares
            self.database.insert(f"square_{i}", {
                "color": "gray",  # Default color; customize as needed
                "subject": f"Topic {i}",
                "paragraphs": [f"Paragraph {j} for Topic {i}" for j in range(1, 4)]  # 3 paragraphs per topic
            })
    def add_player(self, player):
        self.players.append({"name": player, "position": 0})
    def roll_dice(self):
        return random.randint(1, 6)
    def move_player(self):
        current_player = self.players[self.current_turn]
        dice_roll = self.roll_dice()
        current_player['position'] = (current_player['position'] + dice_roll) % 64  # 64 squares
        square_info = self.database.fetch(f"square_{current_player['position'] + 1}")
        return square_info, dice_roll
    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)
    def get_current_player(self):
        return self.players[self.current_turn]
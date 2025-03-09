import random
from app.database import get_square_content, Session

class Game:
    def __init__(self, board_size=8):
        self.board_size = board_size
        self.current_position = 0
        self.session = Session() # Get a database session

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, steps):
        self.current_position = min(self.current_position + steps, self.board_size**2 - 1)

    def get_current_square_content(self):
        return get_square_content(self.current_position, self.session)

    def close_connection(self):
        self.session.close()

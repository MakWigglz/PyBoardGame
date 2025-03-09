import random
from app.database import get_square_content, Session

class Board:
    def __init__(self, num_squares):
        self.num_squares = num_squares

    def get_square_content(self, square_index, session):
        return get_square_content(square_index, session)

    def roll_dice(self):
        return random.randint(1, 6)

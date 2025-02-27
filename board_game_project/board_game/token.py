import sqlite3

class Token:
    def __init__(self, board):
        self.position = (0, 0)
        self.board = board

    def move(self, steps):
        current_row, current_col = self.position
        total_squares = current_row * 8 + current_col + steps
        new_row = total_squares // 8
        new_col = total_squares % 8
        self.position = (new_row, new_col)
        self.display_content()

    def display_content(self):
        row, col = self.position
        square_content = self.board.get_content(row, col)
        print(f"Content at ({row}, {col}): {square_content}")

class Board:
    def __init__(self):
        self.conn = sqlite3.connect('board_game.db')

    def get_content(self, row, col):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT paragraph FROM content
            WHERE row = ? AND col = ?
            LIMIT 1
        ''', (row, col))
        result = cursor.fetchone()
        if result:
            paragraph = result[0]
            cursor.execute('''
                DELETE FROM content
                WHERE row = ? AND col = ? AND paragraph = ?
            ''', (row, col, paragraph))
            self.conn.commit()
            return paragraph
        else:
            return "No more content"

# Example usage
board = Board()
token = Token(board)

# Simulate dice rolls and token movements
dice_rolls = [3, 5, 2, 8, 1]
for roll in dice_rolls:
    token.move(roll)
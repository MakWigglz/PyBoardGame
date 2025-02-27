class Board:
    def __init__(self):
        self.squares = [[None for _ in range(8)] for _ in range(8)]
        # Initialize squares with titles and content
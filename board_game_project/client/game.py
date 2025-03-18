# client/game.py
from app.game_logic import GameLogic
def start_game():
    game = GameLogic()
    game.add_player("Alice")
    game.add_player("Bob")
    while True:
        current_player = game.get_current_player()
        print(f"It's {current_player}'s turn.")
        # Implement player actions here
        game.next_turn()
        # Add a break condition for your game loop
if __name__ == "__main__":
    start_game()
from app.game_logic import GameLogic
def display_board(game):
    print("\nBoard:")
    for i in range(1, 65):  # 64 squares
        square_info = game.database.fetch(f"square_{i}")
        print(f"Square {i}: Color: {square_info['color']}, Subject: {square_info['subject']}")
    # Show player positions
    print("\nPlayer Positions:")
    for player in game.players:
        print(f"{player['name']} is on Square {player['position'] + 1}")
def main():
    game = GameLogic()
    
    # Add players
    game.add_player("Alice")
    game.add_player("Bob")
    max_turns = 10  # Set a limit for how many turns to play
    for turn in range(max_turns):
        display_board(game)
        current_player = game.get_current_player()
        
        square_info, dice_roll = game.move_player()
        print(f"{current_player['name']} rolled a {dice_roll}.")
        print(f"Moved to Square {current_player['position'] + 1}: {square_info['subject']}")
        print("Paragraphs:")
        for paragraph in square_info['paragraphs']:
            print(f"- {paragraph}")
        
        game.next_turn()
    print("Game Over!")
if __name__ == "__main__":
    main()
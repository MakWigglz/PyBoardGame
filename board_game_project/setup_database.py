import sqlite3
import json

DATABASE_FILE = 'board_game.db'
JSON_FILE = '/Users/amakki/Documents/Coding-Design/GitHub/PythonProject/PyBoardGame/board_game_project/data/paragraphs.json'

def setup_database():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS content (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            square_id INTEGER UNIQUE,
            paragraph TEXT
        )
    ''')

    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
            for i, item in enumerate(data):
                cursor.execute("INSERT INTO content (square_id, paragraph) VALUES (?, ?)", (i, item['content']))
    except FileNotFoundError:
        print(f"Error: JSON file '{JSON_FILE}' not found.")
        return
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    conn.commit()
    conn.close()
    print("Database setup complete.")
setup_database()

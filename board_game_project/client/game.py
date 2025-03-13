import pygame
import os
import sys
import socketio
from dotenv import load_dotenv
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

# Load environment variables
load_dotenv()

# --- Constants ---
WIDTH, HEIGHT = 640, 640  # 8x8 grid
SQUARE_SIZE = WIDTH // 8
BOARD_COLOR_1 = (200, 200, 200)  # Light gray
BOARD_COLOR_2 = (100, 100, 100)  # Dark gray
TOKEN_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
TOKEN_EMOJIS = ["👾", "🤖", "👽", "👻", "💀", "🤖"]  # we use emojis but could use images
FONT_SIZE = 30
FONT = pygame.font.Font(None, FONT_SIZE)
API_URL = os.getenv("API_URL", "http://localhost:5000")

# --- Pygame Setup ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Educational Board Game")
clock = pygame.time.Clock()

# --- SocketIO Connection ---
sio = socketio.Client()
sio.connect(API_URL)

# --- Game Variables ---
tokens_data = []
current_player_index = 0
dice_roll = 0
game_over = False
current_position = 0

def load_token(filename="token.svg"):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    try:
        drawing = svg2rlg(filepath)
        renderPM.drawToFile(drawing, "token.png", fmt="PNG")
        token = pygame.image.load("token.png")
        token = pygame.transform.scale(token, (60, 60))
        return token
    except FileNotFoundError:
        print(f"Error: Token file '{filepath}' not found.  Create a simple token.svg.")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading token: {e}")
        sys.exit(1)

def draw_board():
    """Draws the checkerboard pattern."""
    for row in range(8):
        for col in range(8):
            color = BOARD_COLOR_1 if (row + col) % 2 == 0 else BOARD_COLOR_2
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_token(token, position):
    """Draws a token at the specified position."""
    square_x = (position % 8) * SQUARE_SIZE
    square_y = (position // 8) * SQUARE_SIZE
    screen.blit(token, (square_x + 2, square_y + 2))

def draw_token_emoji(position, emoji_index, color_index):
    """Draws a token with an emoji at the specified position."""
    # Validate index
    if not (0 <= emoji_index < len(TOKEN_EMOJIS)):
        print(f"Warning: Invalid emoji_index: {emoji_index}. Using default emoji.")
        emoji = TOKEN_EMOJIS[0]
    else:
        emoji = TOKEN_EMOJIS[emoji_index]

    if not (0 <= color_index < len(TOKEN_COLORS)):
        print(f"Warning: Invalid color_index: {color_index}. Using default color.")
        color = TOKEN_COLORS[0]
    else:
        color = TOKEN_COLORS[color_index]

    square_x = (position % 8) * SQUARE_SIZE
    square_y = (position // 8) * SQUARE_SIZE
    text = FONT.render(emoji, True, color)
    text_rect = text.get_rect(center=(square_x + SQUARE_SIZE // 2, square_y + SQUARE_SIZE // 2))
    screen.blit(text, text_rect)

def display_paragraph(paragraph):
    """Displays a paragraph at the bottom of the screen."""
    text = FONT.render(paragraph, True, (0, 0, 0))
    screen.blit(text, (10, 550))

@sio.on('dice_result')
def on_dice_result(data):
    global current_position
    global tokens_data
    current_position = data['position']
    display_paragraph(data['content'])
    # Update token data when receiving dice result
    if len(tokens_data) > 0:
        tokens_data[0]['position'] = current_position

@sio.on('game_start')
def on_game_start(data):
    global tokens_data
    tokens_data = data['tokens']
    print(f"Game started with tokens: {tokens_data}")

# --- Game Loop ---
token = load_token()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sio.emit('roll_dice')

    draw_board()
    # Draw tokens based on data
    for token_data in tokens_data:
        if "emoji_index" in token_data and "color_index" in token_data:
            draw_token_emoji(token_data['position'], token_data['emoji_index'], token_data['color_index'])
        else:
            draw_token(token, token_data['position'])

    pygame.display.flip()
    clock.tick(30)

sio.disconnect()
pygame.quit()
sys.exit()

import pygame
import sys
import socketio
import json
from PIL import Image
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import os

# --- Pygame Setup ---
pygame.init()
screen = pygame.display.set_mode((64 * 8, 64 * 8))  # 8x8 board, 64x64 squares
pygame.display.set_caption("Educational Board Game")
clock = pygame.time.Clock()

# --- SocketIO Connection ---
sio = socketio.Client()
sio.connect('http://localhost:5000')  # Replace with your server address

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
    screen.fill((255, 255, 255))  # White background
    for x in range(0, 64 * 8, 64):
        for y in range(0, 64 * 8, 64):
            pygame.draw.rect(screen, (0, 0, 0), (x, y, 64, 64), 1)

def draw_token(token):
    square_x = (current_position % 8) * 64
    square_y = (current_position // 8) * 64
    screen.blit(token, (square_x + 2, square_y + 2))

def display_paragraph(paragraph):
    font = pygame.font.Font(None, 30)
    text = font.render(paragraph, True, (0, 0, 0))
    screen.blit(text, (10, 550))

@sio.on('dice_result')
def on_dice_result(data):
    global current_position
    current_position = data['position']
    display_paragraph(data['content'])


# --- Game Loop ---
token = load_token() # Load token only once
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Roll dice on spacebar
                sio.emit('roll_dice')

    draw_board()
    draw_token(token)
    pygame.display.flip()
    clock.tick(30)  # Limit frame rate

sio.disconnect()
pygame.quit()
sys.exit()

# This is a simple 2D game of Hex, whoever creates a straight line WINS!
import pygame
import sys

# Define some constants
WIDTH = 600
HEIGHT = 600
SIZE = 6
LINE_WIDTH = 2
EMPTY = 0
PLAYER1 = 1
PLAYER2 = 2
COLORS = [(255, 255, 255), (255, 0, 0), (0, 0, 255)]

# Initialize the Pygame library
pygame.init()

# Set the size of the window
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the window
pygame.display.set_caption("Hex Game")

# Create the game board as a 2D array
board = [[EMPTY for y in range(SIZE)] for x in range(SIZE)]

# Set the current player to Player 1
current_player = PLAYER1

# Draw the game board
def draw_board():
    window.fill(COLORS[0])
    for x in range(SIZE):
        for y in range(SIZE):
            color = COLORS[board[x][y]]
            pygame.draw.circle(window, color, (int(x * WIDTH / SIZE) + int(WIDTH / SIZE / 2), int(y * HEIGHT / SIZE) + int(HEIGHT / SIZE / 2)), int(WIDTH / SIZE / 2) - LINE_WIDTH)

# Check if a move is valid
def is_valid_move(x, y):
    return board[x][y] == EMPTY

# Make a move
def make_move(x, y):
    global current_player
    board[x][y] = current_player
    current_player = PLAYER2 if current_player == PLAYER1 else PLAYER1

# Check if there is a winner
def get_winner():
    for x in range(SIZE):
        if board[x][0] == PLAYER1 and board[x][SIZE - 1] == PLAYER1:
            return PLAYER1
        if board[x][0] == PLAYER2 and board[x][SIZE - 1] == PLAYER2:
            return PLAYER2
    for y in range(SIZE):
        if board[0][y] == PLAYER1 and board[SIZE - 1][y] == PLAYER1:
            return PLAYER1
        if board[0][y] == PLAYER2 and board[SIZE - 1][y] == PLAYER2:
            return PLAYER2
    return EMPTY

# Run the game loop
def game_loop():
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x = int(x * SIZE / WIDTH)
                y = int(y * SIZE / HEIGHT)
                if is_valid_move(x, y):
                    make_move(x, y)
        
        # Draw the game board
        draw_board()
        
        # Check if there is a winner
        winner = get_winner()
        if winner != EMPTY:
            print("Player", winner, "wins!")
            pygame.quit()
            sys.exit()
        
        # Update the display
        pygame.display.update()

# Start the game loop
game_loop()

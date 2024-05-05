# LEVEL CREATION
from Level import Level
import utils.GameObjects as GameObjects
import settings

level = Level([(GameObjects.zombies[0], 10)], [GameObjects.plants[0]], settings.TICKS_PER_SECOND*60, 1)

level.initialize()

level.addPlant(0, 0, 2)



# IMAGE SHOWING LOGIC

# IMAGE SHOWING LOGIC

import pygame
import time
from Level import Level
import utils.GameObjects as GameObjects
import settings

# Grid dimensions
GRID_ROWS = 5
GRID_COLS = 8
SQUARE_SIZE = 27  # Size of each grid square in pixels

# Margin parameters
TOP_MARGIN = 50
BOTTOM_MARGIN = 50
LEFT_MARGIN = 100
RIGHT_MARGIN = 100

# Colors
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREEN = (0, 128, 0)

# Calculate the size of the Pygame window
WINDOW_WIDTH = (GRID_COLS * SQUARE_SIZE) + LEFT_MARGIN + RIGHT_MARGIN
WINDOW_HEIGHT = (GRID_ROWS * SQUARE_SIZE) + TOP_MARGIN + BOTTOM_MARGIN

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Grid Example")
clock = pygame.time.Clock()

# LEVEL CREATION
level = Level([(GameObjects.zombies[0], 10)], [GameObjects.plants[0]], settings.TICKS_PER_SECOND*60, 1)
level.initialize()
level.addPlant(0, 0, 2)

def draw_grid():
    # Fill the background with black
    screen.fill(BLACK)

    # Draw the grid squares
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            x = col * SQUARE_SIZE + LEFT_MARGIN
            y = row * SQUARE_SIZE + TOP_MARGIN
            square_color = GREEN if col == 0 else BLUE
            pygame.draw.rect(screen, square_color, (x, y, SQUARE_SIZE, SQUARE_SIZE))

    # Draw the grid lines
    for row in range(GRID_ROWS + 1):
        y = row * SQUARE_SIZE + TOP_MARGIN
        pygame.draw.line(screen, WHITE, (LEFT_MARGIN, y), (WINDOW_WIDTH - RIGHT_MARGIN, y), 2)

    for col in range(GRID_COLS + 1):
        x = col * SQUARE_SIZE + LEFT_MARGIN
        pygame.draw.line(screen, WHITE, (x, TOP_MARGIN), (x, WINDOW_HEIGHT - BOTTOM_MARGIN), 2)

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the grid
    draw_grid()

    # Draw all the alive plants, suns, munitions, and zombies

    # Update the display
    pygame.display.flip()

    # Update the game every tick
    level.tick()
    time.sleep(settings.TIME_PER_TICK*1.5)

# Quit Pygame
pygame.quit()

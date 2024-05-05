import pygame

# Grid dimensions
GRID_ROWS = 6
GRID_COLS = 7
SQUARE_SIZE = 50  # Size of each grid square in pixels

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

# Initialize the black points list
black_points = []
dragging = False

def draw_grid():
    # Fill the background with black
    screen.fill(BLACK)

    # Draw the grid squares
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            x = col * SQUARE_SIZE + LEFT_MARGIN
            y = row * SQUARE_SIZE + TOP_MARGIN
            square_color = GREEN if row == 0 else BLUE
            pygame.draw.rect(screen, square_color, (x, y, SQUARE_SIZE, SQUARE_SIZE))

    # Draw the black points
    for point in black_points:
        x, y = point
        pygame.draw.circle(screen, BLACK, (x, y), SQUARE_SIZE // 4)

    # Draw the grid lines
    for row in range(GRID_ROWS + 1):
        y = row * SQUARE_SIZE + TOP_MARGIN
        pygame.draw.line(screen, WHITE, (LEFT_MARGIN, y), (WINDOW_WIDTH - RIGHT_MARGIN, y), 2)

    for col in range(GRID_COLS + 1):
        x = col * SQUARE_SIZE + LEFT_MARGIN
        pygame.draw.line(screen, WHITE, (x, TOP_MARGIN), (x, WINDOW_HEIGHT - BOTTOM_MARGIN), 2)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_x, mouse_y = event.pos
                col = (mouse_x - LEFT_MARGIN) // SQUARE_SIZE
                row = (mouse_y - TOP_MARGIN) // SQUARE_SIZE

                # Check if the click is on a green square
                if row == 0:
                    dragging = True
                    square_x = col * SQUARE_SIZE + LEFT_MARGIN
                    square_y = row * SQUARE_SIZE + TOP_MARGIN
                    pygame.draw.rect(screen, DARK_GREEN, (square_x, square_y, SQUARE_SIZE, SQUARE_SIZE))
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                if dragging:
                    dragging = False
                    mouse_x, mouse_y = event.pos
                    col = (mouse_x - LEFT_MARGIN) // SQUARE_SIZE
                    row = (mouse_y - TOP_MARGIN) // SQUARE_SIZE

                    # Check if the drop is on a blue square
                    if row > 0:
                        # Snap the black point to the center of the square
                        black_points.append((col * SQUARE_SIZE + LEFT_MARGIN + SQUARE_SIZE // 2,
                                             row * SQUARE_SIZE + TOP_MARGIN + SQUARE_SIZE // 2))

    # Draw the grid
    draw_grid()

    # Update the display
    pygame.display.flip()
    clock.tick(60)  # Limit the frame rate

# Quit Pygame
pygame.quit()
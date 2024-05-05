import pygame
pygame.init()

width, height = 256*5, 192*5
screen = pygame.display.set_mode((width, height))

background_image = pygame.image.load('assets/background.png').convert()

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background
    screen.blit(background_image, (0, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

import pygame
import sys

from Game import Game

class GUI:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((900, 1000))  # 9x5 grid, each cell is 100x100
        self.clock = pygame.time.Clock()
        
        self.game = Game(self)
        
    def start(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.screen.fill((255, 255, 255))  # Fill the screen with white color
            
            # Call the game loop here
            self.game.gameTick()
            
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()
    
    def draw_element(self, x: int, y: int, url: str) -> None:
        """Draw an element using its position

        Args:
            x (int): The X Coord
            y (int): The Y Coord
            url (str): The url to the image that will be drawn
        """
        # Load the image from the url
        image = pygame.image.load(url)
        
        # Draw the image on the screen at the specified coordinates
        self.screen.blit(image, (x, y))


g = GUI()
g.start()
g.draw_element(1,1,"old/assets/character.png")
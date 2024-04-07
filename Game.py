import random
from typing import Union
from objects.Niveau import Level
from objects.Plateau import Plateau
from objects.Player import Player
from objects.Static import Static
from objects.Zombie import Zombie


class Game:
    def __init__(self, plateau: Plateau) -> None:
        self.plateau: Plateau = plateau
        
        self.time: int = 0 # The time of the game ( to compute the random events )
        
        # Tell if the level is complete (no more zombies to spawn)
        self.completed: bool = False
        
        return
    
    def start_level(self, level: Level) -> None:
        """Create a new game with the level

        Args:
            level (Level): Level object with all the information needed
        """
        self.level = level
        # Get the center of the plateau (index from 0)
        start = 2 - (level.height // 2)
        for h in range(start, start + level.height):
            for c in range(9):
                self.plateau.setElement(c, h, Static(1, "Grass", "grass"))
        
        return
                
    def gameTick(self, player: Player) -> None:
        # Increment the time by one
        self.time += 1
        
        # Move every single zombies
        for zombie in player.zombies:
            zombie.move()
        
        # Move every single munition
        for munition in player.munitions:
            munition.move()
        
        # Spawn a new zombie
        chosen_zombie: Union[Zombie, int] =  player.zombies[random.randint(0, len(player.zombies)-1)]
        
        
        return
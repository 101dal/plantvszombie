import random
from typing import Dict, List, Union
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
                
    def gameTick(self, player: Player):
        # Increment the time by one
        self.time += 1
        
        # Move every single zombies
        for zombie in player.zombies:
            zombie.move()
        
        # Move every single munition
        for munition in player.munitions:
            munition.move()
        
        # Spawn a new zombie if possible
        zombies_size = len(self.level.zombies)
        if zombies_size > 0:
            
            # Chose a random zombie type in the list
            chosen_zombie_number = random.randint(0,zombies_size) - 1
            chosen_zombie: List[Union[Zombie, int]] = self.level.zombies[chosen_zombie_number]
            
            
            # Get a number between 1 and (level length / amount) to know if that zombie will spawn
            chosen_zombie[1] -= 1 # type: ignore
            
            if chosen_zombie[1] <= 0:
                del self.level.zombies[chosen_zombie_number]
        
        return self.level.zombies
        
        
        
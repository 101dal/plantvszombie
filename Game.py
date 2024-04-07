import random
from typing import Dict, List, Literal, Tuple, Union
import typing
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
        self.start = 2 - (level.height // 2)
        self.end = self.start + level.height
        for h in range(self.start, self.end):
            for c in range(9):
                self.plateau.setElement(c, h, Static(1, "Grass", "grass"))
                
        self.amount_of_zombies = 0
        for z in level.zombies:
            self.amount_of_zombies += z[1]
        
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
            chosen_zombie: Tuple[Zombie, int] = self.level.zombies[chosen_zombie_number]
            
            
            # Get a number between 0 and (level length / (amount of zombies to spawn)) to know if that zombie will spawn
            if random.randint(0, round((self.level.time) // self.amount_of_zombies)) == 0:
                player.zombies.append( chosen_zombie[0].spawn(8, random.randint(self.start, self.end)))
                self.level.zombies[chosen_zombie_number] = (chosen_zombie[0], chosen_zombie[1] - 1)
            
            if chosen_zombie[1] <= 0: # type: ignore
                del self.level.zombies[chosen_zombie_number]
            
            if len(self.level.zombies) == 0:
                self.completed = True
        
        return self.level.zombies
        
        
        
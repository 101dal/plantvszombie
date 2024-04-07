import random
from typing import Tuple
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
            
        self.precomputeRandom()
        
        return
    
    def precomputeRandom(self):
        """Function to precompute all the random generation so that the game happens fluently
        """
        # Compute the Zombies generation
        self.zombies_spawn = []
        for _ in range(self.amount_of_zombies):
            # Define the start
            r = random.randint(0, self.level.time)
            while r in self.zombies_spawn:
                r = random.randint(0, self.level.time)
                
            self.zombies_spawn.append(r)
            
        # Compute the Suns generation (there will be 1 Sun every 5 seconds on average)
        self.suns_spawn = []
        for _ in range(round((self.level.time / 20)/5)):
            self.suns_spawn.append(random.randint(0, self.level.time))
            
        # Sort them to be sure the list is ordered
        self.zombies_spawn.sort()
        self.suns_spawn.sort()
        
        return
                
    def gameTick(self, player: Player):
        """Compute one tick in the game

        Args:
            player (Player): The player object of the game
        """
        # Increment the time by one
        self.time += 1
        
        self.moveObjects(player)
        
        self.spawnZombie(player)
    
        return self.level.zombies
    
    def moveObjects(self, player: Player) -> None:
        """Function to move every existing object on the scene

        Args:
            player (Player): The player object of the game
        """
        # Move every single zombies
        for zombie in player.zombies:
            zombie.move()
        
        # Move every single munition
        for munition in player.munitions:
            munition.move()
            
        return
    
    def spawnZombie(self, player: Player) -> None:
        """Function to compute the spawn of new zombies.

        Args:
            player (Player): The player object of the game
        """
        # Spawn a new zombie if possible
        zombies_size = len(self.level.zombies)
        if zombies_size > 0:
            

            # Chose a random zombie type in the list
            chosen_zombie_number = random.randint(0,zombies_size) - 1
            chosen_zombie: Tuple[Zombie, int] = self.level.zombies[chosen_zombie_number]
            
            
            # If the tick corresponds to the first one computed in the precomputeRandom function then the Zombie will be spawned
            if (len(self.level.zombies) == 0) or (len(self.zombies_spawn) == 0):
                self.completed = True
                return
            
            if self.time == self.zombies_spawn[0]:
                player.zombies.append( chosen_zombie[0].spawn(8, random.randint(self.start, self.end)))
                self.level.zombies[chosen_zombie_number] = (chosen_zombie[0], chosen_zombie[1] - 1)
                
                del self.zombies_spawn[0]
            
            if chosen_zombie[1] <= 0: # type: ignore
                del self.level.zombies[chosen_zombie_number]
            
            
                
        return
    
    def spawnSun(self, player: Player) -> None:
        """Generate a sun every 5 to 10 seconds (can generate none but not possible statistically)

        Args:
            player (Player): The player object of the game
        """
    
        
        
        
        return
        
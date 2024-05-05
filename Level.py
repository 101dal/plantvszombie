import random
from typing import List, Tuple

from creatures.Munition import Munition
from creatures.Plant import Plant
from creatures.Zombie import Zombie
from creatures.Sun import Sun
from utils.AnimationFrame import AnimationFrame
from utils.TexturedObject import TexturedObject

import settings


class Level:
    def __init__(self, zombies: List[Tuple[Zombie, int]], plants: List[Plant], duration: int, height: int) -> None:
        """New level class

        Args:
            zombies (List[Tuple[Zombie, int]]): A list with the type of Zombie and the amount there should be in the level
            plants (List[Plant]): A list of all the possible plants (lower or equal to 6)
            duration (int): The time (in ticks) the level should take to spawn every mobs
            height (int): Height of the level (an odd number)
        """
        assert len(plants) <= 6, "There should not be more than 6 plants"
        assert height%2 == 1, "The height of the level should be odd"
        assert 0<len(plants)<=7, "The number of plants should be between 1 and 7"
        
        self.all_zombies = zombies
        self.plants = plants
        
        self.duration = duration
        self.start = 2 - height//2
        self.end = self.start + height - 1
        
        # Define the amount of currencies
        self.suns: int = 0
        self.score: int = 0
        
        
        # The tick of the level
        self.time = 0
        
        self.alive_zombies: List[Zombie] = []
        self.alive_suns: List[Sun] = []
        self.alive_plants: List[Plant] = []
        self.alive_munitions: List[Munition] = []
        
        return
    
    
    
    def initialize(self) -> None:
        self.initialize_suns()
        self.initialize_zombies()
        
        return
    
    def initialize_suns(self) -> None:
        """Initialize the distribution of all the Suns during the timespawn with a somewhat random distribution
        """
        # There will be by default 1 sun for every 10 seconds
        self.suns_spawn_times: List[int] = []
        total_suns: int = int(self.duration / (settings.GAME_TICK * 10))
        for _ in range(total_suns):
            self.suns_spawn_times.append(random.randint(0, self.duration))
        
        # Sort the spawn times to ensure they're in order
        self.suns_spawn_times.sort()
        
    def initialize_zombies(self) -> None:
        """Initialize the distribution of all the Zombies during the timespawn with a somewhat random distribution
        """
        self.zombie_spawn_times: List[Tuple[int, Zombie]] = []
        total_zombies = sum(amount for _, amount in self.all_zombies)
        time_per_zombie = self.duration / total_zombies
        min_time_between_zombies = time_per_zombie / 2
        max_time_between_zombies = time_per_zombie * 2

        current_time = 0
        for zombie_type, amount in self.all_zombies:
            for _ in range(amount):
                time_to_spawn = current_time + random.uniform(min_time_between_zombies, max_time_between_zombies)
                self.zombie_spawn_times.append((int(time_to_spawn), zombie_type))
                current_time = time_to_spawn

        # Sort the spawn times to ensure they're in order
        self.zombie_spawn_times.sort()
        
        
    def tick(self) -> None:
        self.time += 1
        
        if len(self.suns_spawn_times) > 0:
            self.spawnSuns()
        if len(self.zombie_spawn_times) > 0:
            self.spawnZombies()    
        self.tickEntities()    
            
    def spawnZombies(self) -> None:
        firstZombie = self.zombie_spawn_times[0]
        if firstZombie[0] == self.time:
            spawned: Zombie = firstZombie[1].spawn(7, random.randint(self.start, self.end))
            self.alive_zombies.append(spawned)
            self.zombie_spawn_times.pop(0)
            if settings.DEBUG:
                print(f"Zombie spawned at {self.time} in X: {spawned.x} ; Y: {spawned.y}")
            
        return
    
    def spawnSuns(self) -> None:
        firstSuns = self.suns_spawn_times[0]
        if firstSuns == self.time:
            
            spawned: Sun = Sun(50, TexturedObject([AnimationFrame(["assets/background.png"])])).spawn(random.randint(0,7), 5)
            
            self.alive_suns.append(spawned)
            self.suns_spawn_times.pop(0)
            if settings.DEBUG:
                print(f"Sun spawned at {self.time} in X: {spawned.x} ; Y: {spawned.y}")
        
        return
    
    def addPlant(self, plant: Plant, x: int, y: int) -> None:
        spawned: Plant = plant.spawn(x, y)
        
        self.alive_plants.append(spawned)
        
        if settings.DEBUG:
            print(f"Plant spawned at {self.time} in X: {spawned.x} ; Y: {spawned.y}")
        
        return
    
    def tickEntities(self) -> None:        
            
        # Perform all the Munitions' actions
        for munition in self.alive_munitions:
            possible_touched = munition.move()
            
            if possible_touched:
                # If the munition has touched a zombie Check every zombie to see if it is in the radius of the explosion
                for zombie in self.alive_zombies:
                    if zombie.isInRadius(munition):
                        zombie.takeDamage(munition.damage)
                        
                        if settings.DEBUG:
                            print(f"Zombie damaged with {munition.damage} health ({zombie.health} left) at {self.time} in X: {zombie.x} ; Y: {zombie.y}")
                self.alive_munitions.remove(munition)
            
        # Perform all the Zombies' actions
        for zombie in self.alive_zombies:
            zombie.move()
            if zombie.health <= 0:
                self.increase_score(zombie.score)
                
                self.alive_zombies.remove(zombie)
                
                
                if settings.DEBUG:
                    print(f"Zombie killed at {self.time} in X: {zombie.x} ; Y: {zombie.y}")
            
        # Perform all the Plants' actions
        for plant in self.alive_plants:
            possible_munition: Munition | None = plant.spawn_munition(self.time, self.alive_zombies)
            
            if possible_munition:
                self.alive_munitions.append(possible_munition)
        
        
        return

    def increase_suns(self, amount: int) -> None:
        self.suns += amount
        
        return
    
    def increase_score(self, amount: int) -> None:
        self.score += amount
        
        return
import random
from typing import List, Tuple

from creatures.Plant import Plant
from creatures.Zombie import Zombie


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
        
        self.zombies = zombies
        self.plants = plants
        
        self.duration = duration
        self.start = 3 - height//2
        self.end = self.start + height
        
        # Define the amount of suns at the beginning of the level as 0
        self.suns = 0
        
        # The tick of the level
        self.time = 0
        
        self.alive_zombies: List[Zombie] = []
        
    def initialize(self):
        """Initialize the distribution of all the Zombies during the timespawn with a somewhat random distribution"""
        self.zombie_spawn_times: List[Tuple[int, Zombie]] = []
        total_zombies = sum(amount for _, amount in self.zombies)
        time_per_zombie = self.duration / total_zombies
        min_time_between_zombies = time_per_zombie / 2
        max_time_between_zombies = time_per_zombie * 2

        current_time = 0
        for zombie_type, amount in self.zombies:
            for _ in range(amount):
                time_to_spawn = current_time + random.uniform(min_time_between_zombies, max_time_between_zombies)
                self.zombie_spawn_times.append((int(time_to_spawn), zombie_type))
                current_time = time_to_spawn

        # Sort the spawn times to ensure they're in order
        self.zombie_spawn_times.sort()
        
    def tick(self) -> None:
        self.time += 1
        firstZombie = self.zombie_spawn_times[0]
        if firstZombie[0] == self.time:
            spawned: Zombie = firstZombie[1].spawn(7, random.randint(self.start, self.end))
            self.alive_zombies.append(spawned)
            self.zombie_spawn_times.pop(0)
            print(f"Zombie spawned at {self.time}")
from typing import List, Tuple

from creatures.Munition import Munition
from creatures.Zombie import Zombie

from utils.Spawnable import Spawnable
from utils.TexturedObject import TexturedObject

import settings

class Plant(Spawnable):
    def __init__(self, name: str, texture: TexturedObject, hitbox: Tuple[int, int], munition: Munition | None, speed: int, health: int, cost: int, detection_radius: int = 7) -> None:
        """Class to create a plant

        Args:
            name (str): The name of the plant
            texture (TexturedObject): The animation of the Plant
            hitbox (Tuple[int, int]): A tuple with the size (height, width) of the hitbox
            munition (Munition | None): The type of munition it has
            munition (Munition | None): The type of munition it has
            speed (int): The interval of the munition
            health (int): The amount of health of the Plant
            cost (int): The cost of the Plant (in Suns)
            detection_radius (int, optional): The radius of detection of the Zombies. Defaults to 7.
        """
        super().__init__()
        
        self.name = name
        self.texture = texture
        # Pass the parent to the child
        self.texture.element = self
        
        self.hitbox = hitbox
        self.munition = munition
        self.speed = speed
        self.health = health
        self.cost = cost
        
        self.time = 0
        
        return
    
    def spawn_munition(self, time: int, zombies: List[Zombie]) -> Munition | None:
        spawned: Munition
        if self.munition:
            if time%self.speed == 0:
                # Check if there is a Zombie in the row
                can_be_spawned: bool = False
                possible_zombies: List[Zombie] = []
                for zombie in zombies:
                    if zombie.y - 0.5 <= self.y <= zombie.y + 0.5:
                        can_be_spawned = True
                        possible_zombies.append(zombie)
                
                # If there is one then spawn the munition and return it
                if can_be_spawned:
                    spawned = self.munition.spawn(self.x, self.y)
                    
                    spawned.zombies = possible_zombies.copy()
                    
                    if settings.DEBUG:
                        print(f"Munition spawned at {time} in X: {self.x} ; Y: {self.y}")
                
                    return spawned
            
        return
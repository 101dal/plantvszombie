from typing import List, Tuple

from creatures.Munition import Munition
from utils.Spawnable import Spawnable


class Plant(Spawnable):
    def __init__(self, name: str, sprites: List[str], hitbox: Tuple[int, int], munition: Munition | None, speed: int, health: int) -> None:
        """Class to create a plant

        Args:
            name (str): The name of the plant
            sprites (List[str]): The animation of the Plant
            hitbox (Tuple[int, int]): A tuple with the size (height, width) of the hitbox
            munition (Munition | None): The type of munition it has
            speed (int): The interval of the munition
            health (int): The amount of health of the Plant
        """
        super().__init__()
        
        self.name = name
        self.sprites = sprites
        self.hitbox = hitbox
        self.munition = munition
        self.speed = speed
        self.health = health
        
        return
    
    def spawn_munition(self) -> None:
        if self.munition:
            self.munition.spawn(self.x, self.y)
            
        return
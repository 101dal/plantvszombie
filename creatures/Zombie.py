from typing import List, Tuple

from creatures.Munition import Munition
from utils.Spawnable import Spawnable
from utils.mathematics import distance


class Zombie(Spawnable):
    def __init__(self, name: str, sprites: Tuple[List[str], int], hitbox: Tuple[int, int], speed: float, health: int, damage: int) -> None:
        """Class to create a Zombie

        Args:
            name (str): The name of the Zombie
            sprites (Tuple[List[str], int]): The urls to the sprite and when they will be turned on (at which amount of health)
            hitbox (Tuple[int, int]): A tuple with the size (height, width) of the hitbox
            speed (float): The speed of the zombie
            health (int): The amound of health the Zombie has
            damage (int): The amount of damage the Zombie deals
        """
        
        super().__init__()
        
        self.name = name
        self.sprites = sprites
        self.hitbox = hitbox
        
        self.speed = speed
        
        self.health = health
        self.damage = damage

        return
    
    def move(self):
        self.x -= self.speed
    
    def isInHitbox(self, munition: Munition):
        x1 = munition.x
        y1 = munition.y
        x2 = self.x
        y2 = self.y
        if not (x1>=0 and x2>=0 and y1>=0 and y2>=0):
            return False
        if distance(x1,y1,x2,y2) <= munition.radius:
            return True
        return False
from typing import List, Tuple

from creatures.Munition import Munition
from utils.Spawnable import Spawnable
from utils.mathematics import distance
from utils.TexturedObject import TexturedObject


class Zombie(Spawnable):
    def __init__(self, name: str, texture: TexturedObject, hitbox: Tuple[int, int], speed: float, health: int, damage: int) -> None:
        """Class to create a Zombie

        Args:
            name (str): The name of the Zombie
            texture (TexturedObject): The urls to the sprite and when they will be turned on (at which amount of health)
            hitbox (Tuple[int, int]): A tuple with the size (height, width) of the hitbox
            speed (float): The speed of the zombie
            health (int): The amound of health the Zombie has
            damage (int): The amount of damage the Zombie deals
        """
        
        super().__init__()
        
        self.name = name
        self.texture = texture
        self.hitbox = hitbox
        
        self.speed = speed
        
        self.health = health
        self.damage = damage

        return    
    
    def move(self) -> None:
        self.x -= self.speed
        
        return
    
    def isInHitbox(self, munition: Munition) -> bool:
        hitbox_start_x = self.x - self.hitbox[0] / 2
        hitbox_end_x = self.x + self.hitbox[0] / 2
        hitbox_start_y = self.y - self.hitbox[1] / 2
        hitbox_end_y = self.y + self.hitbox[1] / 2

        
        if ( hitbox_start_x <= munition.x <= hitbox_end_x ) and ( hitbox_start_y <= munition.y <= hitbox_end_y ):
            return True       
        
        
        return False
    
    def isInRadius(self, munition: Munition) -> bool:
        if distance(munition.x, munition.y, self.x, self.y) <= munition.radius:
            return True
        return False
    
    def takeDamage(self, damage: int) -> None:
        self.health -= damage
        
        return
from typing import List
from utils.Spawnable import Spawnable
from utils.TexturedObject import TexturedObject

import settings

class Munition(Spawnable):
    def __init__(self, name: str, texture: TexturedObject, speed: float, damage: int, radius: float = 0) -> None:
        """Munition object

        Args:
            name (str): Name of the munition
            texture (TexturedObject): The texture of the object
            speed (float): The speed of the munition
            damage (int): The damage inflicted by the munition
            radius (float): The radius of impact of the munition. Defaults to 0 (no radius)
        """
        super().__init__()
        
        self.name = name
        self.texture = texture
        # Pass the parent to the child
        self.texture.element = self
        
        self.speed = speed
        self.damage = damage
        self.radius = radius
        
        return
    
    def move(self) -> bool:
        self.x += self.speed
        
        return self.checkZombies()
        
    def checkZombies(self) -> bool:
        for zombie in self.zombies:
            if zombie.isInHitbox(self):
                if settings.DEBUG:
                    print(f"A Munition has touched a Zombie at X: {self.x} ; Y: {self.y}")
                return True
        return False
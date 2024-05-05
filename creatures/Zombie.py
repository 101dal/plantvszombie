from typing import List, Tuple

from creatures.Munition import Munition
from utils.Spawnable import Spawnable
from utils.mathematics import distance
from utils.TexturedObject import TexturedObject

import settings


class Zombie(Spawnable):
    def __init__(self, name: str, texture: TexturedObject, hitbox: Tuple[int, int], speed: float, health: int, damage: int, attack_speed: int,  score: int) -> None:
        """Class to create a Zombie

        Args:
            name (str): The name of the Zombie
            texture (TexturedObject): The urls to the sprite and when they will be turned on (at which amount of health)
            hitbox (Tuple[int, int]): A tuple with the size (height, width) of the hitbox
            speed (float): The speed of the zombie
            health (int): The amound of health the Zombie has
            damage (int): The amount of damage the Zombie deals
            attack_speed (int): Teh number of ticks it waits before attacking again
            score (int): The score the Zombie gives on death
        """
        
        super().__init__()
        
        self.name = name
        self.texture = texture
        # Pass the parent to the child
        self.texture.element = self
        
        self.hitbox = hitbox
        
        self.speed = speed
        
        self.health = health
        self.damage = damage
        self.attack_speed = attack_speed
        
        self.score = score
        
        self.eating: bool = False

        return    
    
    def move(self) -> None:
        if not self.eating:
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
    
    def is_colliding_with_plant(self, plant) -> bool:
        zombie_center_y = self.y
        plant_top = plant.y - plant.hitbox[1] / 2
        plant_bottom = plant.y + plant.hitbox[1] / 2

        if (plant_top <= zombie_center_y <= plant_bottom) and (abs(self.x - plant.x) <= 1):
            self.eating = True
            return True
        return False
    
    def isInRadius(self, munition: Munition) -> bool:
        # Calculate the distance between the center of the zombie and the center of the munition
        dist = distance(self.x, self.y, munition.x, munition.y)

        # Check if the distance is less than or equal to the radius of the munition plus half the width of the zombie's hitbox
        if dist <= munition.radius + self.hitbox[0] / 2:
            return True

        return False
    
    def takeDamage(self, damage: int) -> None:
        self.health -= damage
        
        return
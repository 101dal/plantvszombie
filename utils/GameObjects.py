###
# This file is used for storing all the possible game objects: Plants, Zombies, Suns, Static objects...
###

from creatures.Munition import Munition
from creatures.Plant import Plant
from creatures.Sun import Sun
from creatures.Zombie import Zombie
from utils.AnimationFrame import AnimationFrame
from utils.TexturedObject import TexturedObject

import settings

suns = [
    Sun(
        value=50,
        texture=TexturedObject(
            animations=[
                AnimationFrame(["sun/1.png", "sun/2.png"])
            ]
        )
    )
]


plants = [
    Plant(
        name="Peashooter",
        texture=TexturedObject(
            animations= [
                AnimationFrame(frames_urls=[f"peashooter/{x}.png" for x in range(1, 9)])
                ]
        ),
        hitbox=[1,1],
        munition= Munition(
            name="Peashooter Munition",
            texture=TexturedObject(
                animations=[
                    AnimationFrame(frames_urls=["peashooter/munition.png"])
                    ]
            ),
            speed=settings.TIME_PER_TICK*1.5, # 1.5 blocks per second,
            damage=20,
            radius=0
            
        ),
        speed=settings.TICKS_PER_SECOND*1.5, # Fires every 1.5 second
        health=300,
        cost=100)
    
    
    
]

def basic_zombie_conditionner(self) -> int:
    """Conditionner for basic Zombie
    """
    zombie: Zombie = self.element
    
    if zombie.health < 200:
        return 1
    else:
        return 0
    
    

zombies = [
    Zombie(
        name="Basic Zombie",
        texture=TexturedObject(
            animations=[
                AnimationFrame(frames_urls=[f"basic zombie/{x}.png" for x in range(1,8)]),
                AnimationFrame(frames_urls=[f"basic zombie/{x}_low.png" for x in range(8,15)]),
                AnimationFrame(frames_urls=[f"basic zombie/{x}_eating.png" for x in range(15,22)]),
                AnimationFrame(frames_urls=[f"basic zombie/{x}_eating_low.png" for x in range(22,26)]),
                ],
            conditionner=basic_zombie_conditionner,
            base_animation_index=0
        ),
        hitbox=(1,1),
        speed=settings.TIME_PER_TICK/2, # 0.5 block per second
        health=200,
        damage=15,
        attack_speed=settings.TICKS_PER_SECOND, # 1 attack per second
        score=10
    ),
]
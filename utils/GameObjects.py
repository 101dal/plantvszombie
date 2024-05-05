###
# This file is used for storing all the possible game objects: Plants, Zombies, Suns, Static objects...
###

from creatures.Munition import Munition
from creatures.Plant import Plant
from creatures.Zombie import Zombie
from utils.AnimationFrame import AnimationFrame
from utils.TexturedObject import TexturedObject

import settings


plants = [
    Plant(
        name="Peashooter",
        texture=TexturedObject(
            animations= [ AnimationFrame (
                frames_urls=[f"peashooter/{x}.png" for x in range(1, 9)]
            )]
        ),
        hitbox=[1,1],
        munition= Munition(
            name="Peashooter Munition",
            texture=TexturedObject(
                animations=AnimationFrame(
                    frames_urls=["munition.png"]
                )
            ),
            speed=settings.TIME_PER_TICK*1.5, # 1.5 blocks per second,
            damage=20,
            radius=0
            
        ),
        speed=settings.TICKS_PER_SECOND*1.5, # Fires every 1.5 second
        health=300,
        cost=100)
    
    
    
]

zombies = [
    Zombie(
        name="Basic Zombie",
        texture=
    )
]
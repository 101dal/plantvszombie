import time
from Level import Level
from creatures.Zombie import Zombie
from creatures.Plant import Plant
from creatures.Munition import Munition
from utils.AnimationFrame import AnimationFrame
from utils.TexturedObject import TexturedObject

import settings


# Define all the different textures
animationFrame1 = AnimationFrame(["assets/background.png"])
animationFrame2 = AnimationFrame(["assets/background.png"])
animationFrame3 = AnimationFrame(["assets/background.png"])
animationFrame4 = AnimationFrame(["assets/background.png"])

def conditionner(data):
    return 0

texture1 = TexturedObject([animationFrame1], conditionner=conditionner, base_animation_index=0)
texture2 = TexturedObject([animationFrame2], conditionner=conditionner, base_animation_index=0)
texture3 = TexturedObject([animationFrame3], conditionner=conditionner, base_animation_index=0)
texture4 = TexturedObject([animationFrame4], conditionner=conditionner, base_animation_index=0)

# Define the zombies
zombie1 = Zombie(
    name="Zombie1",
    texture=texture1,
    hitbox=(2, 2),
    speed=0.1,
    health=20, 
    damage=10,
    score=10)

zombie2 = Zombie(
    name="Zombie2",
    texture=texture2,
    hitbox=(2, 2),
    speed=0.1,
    health=20, 
    damage=10,
    score=10)

# Define the plants
plant1 = Plant(
    name="Plant1",
    texture=texture3,
    hitbox=(2, 2),
    munition=Munition("Munition1", 10, 0.1, 5, 5),
    speed=10,
    health=2,
    cost=2)
plant2 = Plant(
    name="Plant2",
    texture=texture4,
    hitbox=(2, 2),
    munition=Munition("Munition2", 10, 0.1, 5, 5),
    speed=10,
    health=50,
    cost=50)

# Create the level
level = Level([(zombie1, 10), (zombie2, 20)], [plant1, plant2], settings.TICKS_PER_SECOND*60, 1)

# Initialize the level
level.initialize()

level.addPlant(plant1, 0, 2)

print(level.start)
print(level.end)

for t in level.zombie_spawn_times:
    print(t)

time.sleep(1)
    
while True:
    level.tick()
    if len(level.zombie_spawn_times) == 0:
        break
    #time.sleep(1/settings.GAME_TICK)
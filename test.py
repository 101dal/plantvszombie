import time
from Level import Level
from creatures.Zombie import Zombie
from creatures.Plant import Plant
from creatures.Munition import Munition

# Define the zombies
zombie1 = Zombie("Zombie1", (["zombie1_sprite1", "zombie1_sprite2"], 50), (50, 50), 2.0, 100, 10)
zombie2 = Zombie("Zombie2", (["zombie2_sprite1", "zombie2_sprite2"], 50), (50, 50), 3.0, 150, 20)

# Define the plants
plant1 = Plant("Plant1", ["plant1_sprite1", "plant1_sprite2"], (50, 50), Munition("Munition1", 10, 20, 5, 5), 100, 50)
plant2 = Plant("Plant2", ["plant2_sprite1", "plant2_sprite2"], (50, 50), Munition("Munition2", 20, 30, 5, 5), 50, 75)

# Create the level
level = Level([(zombie1, 10), (zombie2, 20)], [plant1, plant2], 600, 3)

# Initialize the level
level.initialize()

for t in level.zombie_spawn_times:
    print(t)

time.sleep(1)
    
while True:
    level.tick()
    if len(level.zombie_spawn_times) == 0:
        break
    time.sleep(1/50)
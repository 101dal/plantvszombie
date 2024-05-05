import time
from Level import Level


import settings

import utils.GameObjects as GameObjects


# Create the level
level = Level([(GameObjects.zombies[0], 10)], [GameObjects.plants[0]], settings.TICKS_PER_SECOND*60, 1)

# Initialize the level
level.initialize()

level.addPlant(0, 0, 2)

print(level.start)
print(level.end)

for t in level.zombie_spawn_times:
    print(t)

time.sleep(1)
    
e = 0
while True:
    level.tick()
    if len(level.zombie_spawn_times) == 0:
        break
    e+=1
    #time.sleep(settings.TIME_PER_TICK)
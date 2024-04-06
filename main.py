# Toutes les plantes sont placées ici

from Game import Game
from objects.GameObjects import GameObjects
from objects.Niveau import Level
from objects.Plateau import Plateau
from objects.Player import Player
from objects.Static import Static


go = GameObjects()
plants = go.plants
zombies = go.zombies

player = Player()

plateau = Plateau()




level = Level(1, [zombies[0]], [plants[0]], 1)

game = Game(plateau)

# Here are all the test relative to the Plants and their ammo
plant1 = plants[0].plant(0,0)
plant2 = plants[0].plant(0,1)

print(f"Plant1: x={plant1.x} ; y={plant1.y}")
print(f"Plant2: x={plant2.x} ; y={plant2.y}")


ammo1 = plant1.spawnAmmo()
ammo2 = plant1.spawnAmmo()

ammo1.move()
ammo2.move()
ammo2.move()
ammo2.move()
ammo2.move()
ammo2.move()



print(f"Munition: x={ammo1.x} ; y={ammo1.y}")
print(f"Munition: x={ammo2.x} ; y={ammo2.y}")


game.start_level(level)

game.plateau.setElement(1,2, Static(2, "rock", "rock"))


# for l in game.plateau.plateau:
#     for c in l:
#         try:
#             print(c.id, end=" ")
#         except:
#             print(c, end=" ")
#     print()
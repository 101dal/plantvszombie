# Toutes les plantes sont placées ici

from Game import Game
from objects.GameObjects import GameObjects
from objects.Niveau import Level
from objects.Plateau import Plateau
from objects.Static import Static


go = GameObjects()
plants = go.plants
zombies = go.zombies

plateau = Plateau()




level = Level(1, [zombies[0]], [plants[0]], 1)

game = Game(plateau)

game.start_level(level)

game.plateau.setElement(1,2, Static(2, "rock", "rock"))

for l in game.plateau.plateau:
    for c in l:
        try:
            print(c.id, end=" ")
        except:
            print(c, end=" ")
    print()
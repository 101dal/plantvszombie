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




level = Level(height=1, zombies=[(zombies[0], 5)], plants=[plants[0]], waves=1, time=20*30)

game = Game(plateau)


game.start_level(level)

game.plateau.setElement(1,2, Static(2, "rock", "rock"))


index = 0
while not game.completed:
    print(game.gameTick(player))
    index+=1
    print(index)

print(player.zombies)


for l in game.plateau.plateau:
    for c in l:
        try:
            print(c.id, end=" ")
        except:
            print(c, end=" ")
    print()
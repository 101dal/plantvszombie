# Toutes les plantes sont placées ici
from objects.Munition import Munition
from objects.Plant import Plant
from objects.Plateau import Plateau


plantes = [
    Plant(0, 1.5, Munition(0, 1, 20, "test"), 1, 1, "Peashooter", "none")
]

plateau = Plateau()

plateau.setElement(0, 0, plantes[0])
plateau.setElement(0, 0, plantes[0])

for l in plateau.plateau:
    for c in l:
        try:
            print(c.name, end=" ")
        except:
            print(c, end=" ")
    print()
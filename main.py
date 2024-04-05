# Toutes les élément pas fixes sont ici
munitions = []


class Munition:
    def __init__(self, id: int, speed: float, damage: float, costume: str) -> None:
        self.id = id

        self.speed = speed
        self.damage = damage
        self.costume = costume

        return

    def setElement(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

        return


class Plante:
    def __init__(self, id: int,  delais: float, munition, vie: int, type: int, name: str, costume: str) -> None:
        self.id = id

        self.delais = delais
        self.munition = munition

        self.vie = vie

        self.type = type
        self.name = name

        self.costume = costume

        return

    def spawnAmmo():
        # Fixes ici pour le debug
        x = 0
        y = 0


class Zombie:
    def __init__(self, id: int) -> None:
        self.id = id
        return


class Plateau:
    # Tous les zombies sont stockés ici
    zombies = []

    def __init__(self) -> None:
        self.plateau = [[None for _ in range(7)] for _ in range(5)]
        return

    def getElement(self, x: int, y: int):
        return self.plateau[y][x]

    def setElement(self, x: int, y: int, element) -> None:
        self.plateau[y][x] = element
        return


# Toutes les plantes sont placées ici
plante = [
    Plante(0, 1.5, Munition(0, 1, 20, "test"), 1, 1, "Peashooter", "none")
]

plateau = Plateau()

plateau.setElement(0, 0, plante[0])

for l in plateau.plateau:
    for c in l:
        try:
            print(c.name, end=" ")
        except:
            print(c, end=" ")

    print()

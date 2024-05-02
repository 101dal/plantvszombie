from objects.Static import Static


class Plateau:
    def __init__(self) -> None:
        self.plateau = [[Static(0, "ground", "ground") for _ in range(9)] for _ in range(5)]
        return

    def getElement(self, x: int, y: int):
        return self.plateau[y][x]

    def setElement(self, x: int, y: int, element) -> None:
        self.plateau[y][x] = element
        return
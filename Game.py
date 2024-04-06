from objects.Niveau import Level
from objects.Plateau import Plateau
from objects.Static import Static


class Game:
    def __init__(self, plateau: Plateau) -> None:
        self.plateau = plateau
        pass
    
    def start_level(self, level: Level):
        # Get the center of the plateau (index from 0)
        start = 2 - (level.height // 2)
        for h in range(start, start + level.height):
            for c in range(9):
                self.plateau.setElement(c, h, Static(1, "Grass", "grass"))
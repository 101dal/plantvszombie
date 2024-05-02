from utils.Spawnable import Spawnable


class Munition(Spawnable):
    def __init__(self, name: str, sprite: str, speed: float, damage: int, radius: float) -> None:
        super().__init__()
        
        self.name = name
        self.sprite = sprite
        self.speed = speed
        self.damage = damage
        self.radius = radius
        
        return
        
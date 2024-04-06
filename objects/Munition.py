class Munition:
    def __init__(self, id: int, speed: float, damage: float, sprite: str) -> None:
        self.id = id

        self.speed = speed
        self.damage = damage
        self.sprite = sprite

        return

    def create(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        
    def move(self):
        self.x -= self.speed
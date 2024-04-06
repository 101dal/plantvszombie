class Munition:
    def __init__(self, id: int, speed: float, damage: float, sprite: str) -> None:
        self.id = id

        self.speed = speed
        self.damage = damage
        self.sprite = sprite

        self.x = None
        self.y = None

    def create(self, x: float, y: float):
        new_munition = Munition(id=self.id, speed=self.speed, damage=self.damage, sprite=self.sprite)
        
        new_munition.x = x
        new_munition.y = y
        
        return new_munition
        
    def move(self):
        assert (self.x is not None), "This object has not been initialized"
        self.x += self.speed
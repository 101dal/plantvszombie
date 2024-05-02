from objects.TexturedObject import TexturedObject


class Munition(TexturedObject):
    def __init__(self, id: int, speed: float, damage: float, sprite: str) -> None:
        super().__init__(sprite=sprite)
        
        self.id: int = id

        self.speed: float = speed
        self.damage: float = damage

        self.x: float | None = None
        self.y: float | None = None

    def create(self, x: float, y: float):
        new_munition: Munition = Munition(id=self.id, speed=self.speed, damage=self.damage, sprite=self.sprite)
        
        new_munition.x = x
        new_munition.y = y
        
        return new_munition
        
    def move(self):
        assert (self.x is not None), "This object has not been initialized"
        self.x += self.speed
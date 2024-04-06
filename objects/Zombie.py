class Zombie:
    def __init__(self, id: int, health: int, speed: float, type: str, sprite: str) -> None:
        self.id = id
        
        self.health = health
        self.speed = speed
        self.type = type
        
        self.sprite = sprite
    
    def spawn(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def move(self):
        self.x -= self.speed
class Zombie:
    def __init__(self, id: int, health: int, speed: float, name: str, sprite: str, cost: int) -> None:
        self.id = id
        
        self.health = health
        self.speed = speed
        self.type = type
        
        self.name = name
        self.sprite = sprite
        
        self.cost = cost
    
    def spawn(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def move(self):
        self.x -= self.speed
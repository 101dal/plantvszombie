class Zombie:

    def __init__(self, id: int, health: int, speed: float, name: str, sprite: str, cost: int) -> None:
        self.id = id
        
        self.health = health
        self.speed = speed
        
        self.name = name
        
        self.sprite = sprite
        
        self.cost = cost
        
        # Dummy positions
        self.x = None
        self.y = None

    def spawn(self, x: float, y: float):
        # Create a new zombie with the same properties as self
        new_zombie = Zombie(id=self.id, health=self.health, speed=self.speed,
                            name=self.name, sprite=self.sprite, cost=self.cost)

        # Set the spawn position of the new zombie
        new_zombie.x = x
        new_zombie.y = y

        return new_zombie

    def move(self):
        assert (self.x is not None), "This object has not been initialized"
        self.x -= self.speed

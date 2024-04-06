from objects.Munition import Munition

class Plant:
    """Generate a Plant element"""

    def __init__(self, id: int, delais: float, munition: Munition, vie: int, name: str, sprite: str) -> None:
        self.id = id

        self.delais = delais
        self.munition = munition

        self.vie = vie

        self.name = name

        self.sprite = sprite

        # Initialize x and y with default values
        self.x = None
        self.y = None

    def plant(self, x: int, y: int):
        # Create a new plant with the same properties as self
        new_plant = Plant(id=self.id, delais=self.delais, munition=self.munition,
                          vie=self.vie, name=self.name, sprite=self.sprite)

        # Set the position of the new plant
        new_plant.x = x
        new_plant.y = y

        return new_plant

    def spawnAmmo(self):
        assert (self.x is not None) and (self.y is not None), "This object has not be initialized"
        munition = self.munition.create(self.x, self.y)

        # Set the position of the munition
        munition.x = self.x
        munition.y = self.y
        
        return munition
        

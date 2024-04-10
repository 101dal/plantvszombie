from objects.Munition import Munition
from objects.TexturedObject import TexturedObject

class Plant(TexturedObject):
    """Generate a Plant element"""

    def __init__(self, id: int, delais: float, munition: Munition, vie: int, name: str, sprite: str) -> None:
        super().__init__(sprite=sprite)
        
        
        self.id: int = id

        self.delais: float = delais
        self.munition: Munition = munition

        self.vie: int = vie

        self.name: str = name

        # Initialize x and y with default values
        self.x: int | None = None
        self.y: int | None = None

    def plant(self, x: int, y: int):
        # Create a new plant with the same properties as self
        new_plant: Plant = Plant(id=self.id, delais=self.delais, munition=self.munition,
                          vie=self.vie, name=self.name, sprite=self.sprite)

        # Set the position of the new plant
        new_plant.x = x
        new_plant.y = y

        return new_plant

    def spawnAmmo(self):
        assert (self.x is not None) and (self.y is not None), "This object has not be initialized"
        munition: Munition = self.munition.create(self.x, self.y)

        # Set the position of the munition
        munition.x = self.x
        munition.y = self.y
        
        return munition
        

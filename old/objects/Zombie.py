from typing import Tuple
from PIL import Image
import dotenv

from objects.TexturedObject import TexturedObject

class Zombie(TexturedObject):
    def __init__(self, id: int, health: int, speed: float, name: str, cost: int, sprite: str) -> None:
        super().__init__(sprite=sprite)
        
        self.id: int = id
        
        self.health: int = health
        self.speed: float = speed
        
        self.name: str = name
        
        self.cost: int = cost
        
        # Dummy positions
        self.x: float | None = None
        self.y: float | None = None

        return

    def spawn(self, x: float, y: float):
        """Create a copy of the zombie with additional coordinate information

        Args:
            x (float | int): X Coord
            y (float | int): Y Coord

        Returns:
            Zombie: The new Zombie with all the information needed
        """
        # Create a new zombie with the same properties as self
        new_zombie: Zombie = Zombie(id=self.id, health=self.health, speed=self.speed,
                            name=self.name, cost=self.cost, sprite=self.sprite)

        # Set the spawn position of the new zombie
        new_zombie.x = x
        new_zombie.y = y

        return new_zombie

    def move(self) -> None:
        """Move the Zombie if it exist
        """
        assert (self.x is not None), "This object has not been initialized"
        self.x -= self.speed

        return

    def getDrawPosition(self) -> Tuple[float,float]:
        """Get the position to draw the drawing to using the size of the image
        """

        return (1,2)

        
from objects.Plant import Plant
from objects.Zombie import Zombie


class Niveau:
    def __init__(self, height: int, zombies: list[Zombie], plants: list[Plant], waves: int ) -> None:
        """A class to generate a new level

        Args:
            height (int): Heigh of the level (an odd number)
            zombies (list[Zombie]): The list of all possible Zombies in the level
            plants (list[Plant]): The list of all possible Plants in the level
            waves (int): The number of waves
        """
        self.height = height
        self.zombies = zombies
        self.plants = plants
        self.waves = waves
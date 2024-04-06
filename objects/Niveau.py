from objects.Plant import Plant
from objects.Zombie import Zombie


class Level:
    def __init__(self, height: int, zombies: list[Zombie], plants: list[Plant], waves: int ) -> None:
        """A class to generate a new level

        Args:
            height (int): Heigh of the level (an odd number)
            zombies (list[Zombie]): The list of all possible Zombies in the level
            plants (list[Plant]): The list of all possible Plants in the level
            waves (int): The number of waves
        """
        assert (height % 2 == 1) and (height > 0) and (height < 5), "Heigh has to be an odd number between 1 and 5"
        
        self.height = height
        self.zombies = zombies
        self.plants = plants
        self.waves = waves
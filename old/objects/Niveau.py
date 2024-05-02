from typing import Dict, List, Tuple, Union
from objects.Plant import Plant
from objects.Zombie import Zombie


class Level:
    def __init__(self, height: int, zombies: List[Tuple[Zombie, int]], plants: List[Plant], waves: int, time: int ) -> None:
        """A class to generate a new level

        Args:
            height (int): Heigh of the level (an odd number)
            zombies (List[Zombie]): The List of all possible Zombies in the level
            plants (List[Plant]): The List of all possible Plants in the level
            waves (int): The number of waves (each wave there are 2 more zombies that spawn during it)
            time (int): The time of the level (in game tick with 20 ticks / second)
        """
        assert (height % 2 == 1) and (height > 0) and (height < 5), "Heigh has to be an odd number between 1 and 5"
        
        self.height: int = height
        self.zombies: List[Tuple[Zombie, int]] = zombies
        self.plants: List[Plant] = plants
        self.waves: int = waves
        self.time: int = time
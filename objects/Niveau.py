from typing import Dict, List, Union
from objects.Plant import Plant
from objects.Zombie import Zombie


class Level:
    def __init__(self, height: int, zombies: List[List[Union[Zombie, int]]], plants: List[Plant], waves: int ) -> None:
        """A class to generate a new level

        Args:
            height (int): Heigh of the level (an odd number)
            zombies (List[Zombie]): The List of all possible Zombies in the level
            plants (List[Plant]): The List of all possible Plants in the level
            waves (int): The number of waves (each wave there are 2 more zombies that spawn during it)
        """
        assert (height % 2 == 1) and (height > 0) and (height < 5), "Heigh has to be an odd number between 1 and 5"
        
        self.height: int = height
        self.zombies: List[List[Union[Zombie, int]]] = zombies
        self.plants: List[Plant] = plants
        self.waves: int = waves
from typing import List
from objects.Munition import Munition
from objects.Plant import Plant
from objects.Zombie import Zombie


class GameObjects:
    def __init__(self) -> None:
        """Create a GameObjects object with all the Zombies, Munitions and Plants possible to find in the game
        """
        zombies = [
            Zombie(id=0, health=10, speed=1, name="Zombie", sprite="zombie", cost=50)
        ]
        
        munitions = [
            Munition(id=0, speed=1, damage=20, sprite="zombie")
        ]
        
        plants = [
            Plant(id=0, delais=1.5, munition=munitions[0], vie=1, name="Peashooter", sprite="zombie")
        ]
        
        self.zombies: List[Zombie] = zombies
        self.munitions: List[Munition] = munitions
        self.plants: List[Plant] = plants
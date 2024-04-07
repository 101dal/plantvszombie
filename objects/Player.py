from typing import List
from objects.Munition import Munition
from objects.Plant import Plant
from objects.Sun import Sun
from objects.Zombie import Zombie


class Player:
    def __init__(self) -> None:
        self.score: int = 0
        self.money: int = 0
        self.suns: List[Sun] = []
        self.plants: List[Plant] = []
        self.zombies: List[Zombie] = []
        self.munitions: List[Munition] = []
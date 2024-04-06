class Plant:
    """Generate a Plant element
    """
    def __init__(self, id: int,  delais: float, munition, vie: int, type: int, name: str, sprite: str) -> None:
        self.id = id

        self.delais = delais
        self.munition = munition

        self.vie = vie

        self.type = type
        self.name = name

        self.sprite = sprite
    
    def plant(self, x: int, y: int):
        self.x = x
        self.y = y

    def spawnAmmo(self):        
        munition = self.munition
        
        munition.x = self.x
        munition.y = self.y
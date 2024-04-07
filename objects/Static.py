class Static:
    """Generate a static element (rock, air...) that cannot be interacted with
    """
    def __init__(self, id: int, name:str, sprite: str) -> None:
        self.id: int = id
        
        self.name: str = name
        
        self.sprite: str = sprite
        
        return
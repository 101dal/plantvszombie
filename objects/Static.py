class Static:
    """Generate a static element (rock, air...) that cannot be interacted with nor stepped on
    """
    def __init__(self, id: int, name:str, sprite: str) -> None:
        self.id = id
        
        self.name = name
        
        self.sprite = sprite
        
        return
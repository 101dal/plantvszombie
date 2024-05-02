from objects.TexturedObject import TexturedObject


class Static(TexturedObject):
    """Generate a static element (rock, air...) that cannot be interacted with
    """
    def __init__(self, id: int, name:str, sprite: str) -> None:
        super().__init__(sprite=sprite)
        
        self.id: int = id
        
        self.name: str = name
        
        return
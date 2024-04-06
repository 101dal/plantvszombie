class Sun:
    def __init__(self, id: int, value: int) -> None:
        self.id = id
        self.value = value
        
        self.x = None
        self.y = None
    
    def spawn(self, x: float, y: float):
        new_sun = Sun(id=self.id, value=self.value)
        new_sun.x = x
        new_sun.y = y
        
        return new_sun
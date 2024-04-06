class Sun:
    def __init__(self, id: int, value: int) -> None:
        self.id = id
        self.value = value
    
    def spawn(self, x: float, y: float):
        self.x = x
        self.y = y
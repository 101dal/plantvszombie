class Sun:
    def __init__(self, id: int, value: int) -> None:
        self.id: int = id
        self.value: int = value
        
        self.x: float | None = None
        self.y: float | None = None
    
    def spawn(self, x: float, y: float):
        """Create a new Sun

        Args:
            x (float): C Coord
            y (float): Y Coord

        Returns:
            Sun: The new Sun created
        """
        new_sun: Sun = Sun(id=self.id, value=self.value)
        new_sun.x = x
        new_sun.y = y
        
        return new_sun
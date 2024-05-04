class Spawnable:
    def __init__(self, x: float=-1, y: float=-1) -> None:
        """Class template for every entity that can be spawned
        """
        
        self.x = x
        self.y = y
    
    def spawn(self, x:float, y:float):
        """Create a copy of itself with the x and y coords information

        Args:
            x (float): X Coord
            y (float): Y Coord
        """
        arguments = {}
        for k in self.__dict__:
            k = str(k)
            if k=='x' or k=='y' or k=='time':
                continue
            arguments[k] = self.__dict__.get(k)
        new_spawnable = self.__class__(**arguments)  # Create a new instance of the same class with the same arguments
        new_spawnable.x = x
        new_spawnable.y = y
        return new_spawnable
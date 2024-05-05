from utils.Spawnable import Spawnable
from utils.TexturedObject import TexturedObject

class Sun(Spawnable):
    def __init__(self, value: int, texture: TexturedObject) -> None:
        super().__init__()
        
        self.value = value
        self.texture = texture
        # Pass the parent to the child
        self.texture.element = self
        
        return
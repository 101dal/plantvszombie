from PIL import Image

class TexturedObject:
    def __init__(self, sprite: str) -> None:
        self.sprite = sprite
        
        self.image = Image.open(f'./assets/{sprite}.png')
        
        return
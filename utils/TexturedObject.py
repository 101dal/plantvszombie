from typing import List 
from PIL import Image

class TexturedObject:
    def __init__(self, textures_urls: List[str], animation_length: int = 1, texture_start: int = 0) -> None:
        """Class template for every textured object

        Args:
            textures_urls (List[str]): All the textures
            animation_length (int, optional): The length of the animation (in frames). Defaults to 1.
            texture_start (int, optional): The frame to which the animation has to start. Defaults to 0.
        """
        # Map all the textures in a tuple by opening them with PIL
        assert len(textures_urls) > 0, "There cannot be no texture"
        assert animation_length > 0, "The animation has to be minimum 1 frame"
        self.textures = tuple(map(Image.open, textures_urls))
        
        self.animation_length = animation_length
        
        self.texture_start = texture_start
        self.index = self.texture_start
        self.current_texure = self.textures[self.index]
        return
    
    def next_texture(self) -> None:
        self.index += 1
        if self.index > self.texture_start + self.animation_length:
            self.index = self.texture_start
        self.current_texure = self.textures[self.index]
        
        return
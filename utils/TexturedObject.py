import os
from typing import Callable, List
import pygame

from utils.AnimationFrame import AnimationFrame


class TexturedObject:
    def __init__(self, animations: List[AnimationFrame], conditionner: Callable[[any], int] | None = None, base_animation_index: int = 0) -> None:
        """Class template for every textured object

        Args:
            animations (List[AnimationFrame]): A Tuple of all the possible animations. Defaults to None
            conditionner: (Callable[[any], int] | None): A function that takes in input a data and the return a value which is the current animation that is supposed to be playing
            base_animation_index (int, optional): The index of the base animation (every times an animation finished it returns to that one if no condition is provided). Defaults to 0.
        """
        assert len(animations) > 0, "There is to be at minimum 1 animation"
        
        self.animations = animations
        self.base_animation_index = base_animation_index
        
        self.current_animation = self.animations[0]
        self.current_animation_index = base_animation_index
        
        # Define the conditionner
        self.conditionner = conditionner
        
        return
    
    def next_frame(self) -> bool:
        """Function to go to the next frame of the animation

        Returns:
            bool: Return True if the animation just ended and False otherwise
        """
        # Check the current animation
        should_be_current = self.check_current_animation()
        
        if should_be_current != self.current_animation_index:
            self.current_animation.reset()
            self.current_animation_index = should_be_current
            self.current_animation = self.animations[self.current_animation_index]
        
            
        result = self.current_animation.next_frame()
        
        # If it is the end of the previous animation then restart to the base animation
        if result:
            self.current_animation.reset()
            self.current_animation = self.animations[self.base_animation_index]
            
            return True
        
        return False
    
    def check_current_animation(self) -> int:
        """Check what animation should be playing right no

        Args:
            function (Callable): The function used to check for the animation
        """
        
        # If there is no function then return the base animation
        if (self.conditionner == None):
            return self.base_animation_index
        # Return the result of the function
        result = self.conditionner(self)
        
        # Check if the result of the animation enters the bounds of the possible animations
        if (result < 0) or (result > len(self.animations)-1):
            raise "The animation function passed is not correct"
        
        return result
        
class TexturedObject2:
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
        self.textures = tuple(pygame.image.load(os.path.join(texture_url)) for texture_url in textures_urls)
        
        self.animation_length = animation_length
        
        self.texture_start = texture_start
        self.index = self.texture_start
        self.current_texture = self.textures[self.index]
        return
    
    def next_texture(self) -> None:
        self.index += 1
        if self.index > self.texture_start + self.animation_length:
            self.index = self.texture_start
        self.current_texture = self.textures[self.index]
        
        return
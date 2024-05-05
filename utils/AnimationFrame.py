import os
from typing import List

import pygame


class AnimationFrame:
    def __init__(self, frames_urls: List[str]) -> None:
        """An animation frame object used to define a new animation for a texture

        Args:
            frames_urls (List[str]): The list to all the images in the order of the animation
        """
        assert len(frames_urls) > 0, "There is to be minimum 1 frame in the animation"
        
        self.frames = [tuple(pygame.image.load(os.path.join("assets", texture_url)) for texture_url in frames_urls)]
        
        self.duration = len(self.frames)
        self.time = 0
        
        self.current_frame = self.frames[0]
        
        return

    def next_frame(self) -> bool:
        """A function to go to the next frame of the animation.

        Returns:
            bool: Return True if the animation is finished and False otherwise
        """
        self.time += 1
        
        if self.time >= self.duration:
            return True
        
        self.current_frame = self.frames[self.time]
        
        return False
    
    def reset(self) -> None:
        """Reset the current animation to the first frame
        """
        self.time = 0
        
        self.current_frame = self.frames[self.time]
        
        return
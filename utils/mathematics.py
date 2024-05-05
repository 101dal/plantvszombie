import math
from typing import Tuple

def distance(x1: float, y1: float, x2: float, y2:float):
    return math.sqrt((x2-x1)**2 + (y2 - y1)**2)

def getCenter(x: float,y: float, height: float, width: float) -> Tuple[float, float]:
    """Function that allows to get the coordinates of the center of a rectangle

    Args:
        x (float): X Coord of the top left corner
        y (float): Y Coord of the top left corner
        height (float): Height of the rectangle
        width (float): Width of the rectangle
    """
    
    return (x+width/2, y+height/2)
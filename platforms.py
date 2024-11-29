# Platforms.py
import pyray as rl


def ground(xPos: float, yPos:float, width: float, height:float, color : rl.Color):
    ground1 = rl.Rectangle(xPos, yPos, width, height)
    return {"rect" : ground1, "color" : color}
    
    
def wall(xPos: float, yPos: float, width: float, height: float, color: rl.Color):
    """
    Creates a wall platform (vertical).
    """
    wall1 = rl.Rectangle(xPos, yPos, width, height)
    return {"rect": wall1, "color": color}
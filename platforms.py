# Platforms.py
import pyray as rl


def ground(xPos: float, yPos:float, width: float, height:float, color : rl.Color):
    ground1 = rl.Rectangle(xPos, yPos, width, height)
    return {"rect" : ground1, "color" : color, "damage": 0}
    
def damage_ground(xPos: float, yPos:float, width: float, height:float):
    ground1 = rl.Rectangle(xPos, yPos, width, height)
    return {"rect" : ground1, "color" : rl.RED, "damage" : -0.1}
    

    
def wall(xPos: float, yPos: float, width: float, height: float, color: rl.Color):
    """
    Creates a wall platform (vertical).
    """
    wall1 = rl.Rectangle(xPos, yPos, width, height)
    return {"rect": wall1, "color": color, "damage": 0}
    
    
def moving_horizontal(xPos: float, yPos: float, width: float, height: float, color: rl.Color, speed: float, move_range: float):
    """
    Creates a horizontally moving platform that moves left to right.
    It will move back and forth until it collides with another platform.
    """
    # Track movement direction
    direction = 1  # 1 means moving right, -1 means moving left
    x_velocity = speed
    initial_pos = xPos
    current_pos = xPos

    def update():
        nonlocal current_pos, direction
        current_pos += direction * x_velocity
        # Reverse direction when reaching the move range limits
        if current_pos - initial_pos >= move_range or current_pos - initial_pos <= 0:
            direction *= -1
        return ground(xPos=current_pos, yPos=yPos, width=width, height=height, color=color)
    
    return update

# Vertical Moving Platform
def moving_vertical(xPos: float, yPos: float, width: float, height: float, color: rl.Color, speed: float, move_range: float):
    """
    Creates a vertically moving platform that moves up and down.
    """
    direction = 1  # 1 means moving up, -1 means moving down
    y_velocity = speed
    initial_pos = yPos
    current_pos = yPos

    def update():
        nonlocal current_pos, direction
        current_pos += direction * y_velocity
        # Reverse direction when reaching the move range limits
        if current_pos - initial_pos >= move_range or current_pos - initial_pos <= 0:
            direction *= -1
        return ground(xPos=xPos, yPos=current_pos, width=width, height=height, color=color)
    
    return update

# Short Horizontal Moving Platform
def moving_short_horizontal(xPos: float, yPos: float, width: float, height: float, color: rl.Color, speed: float, move_pixels: float):
    """
    Creates a short horizontal moving platform that moves a fixed distance back and forth.
    """
    direction = 1  # 1 means moving right, -1 means moving left
    x_velocity = speed
    initial_pos = xPos
    current_pos = xPos

    def update():
        nonlocal current_pos, direction
        current_pos += direction * x_velocity
        if abs(current_pos - initial_pos) >= move_pixels:
            direction *= -1
        return ground(xPos=current_pos, yPos=yPos, width=width, height=height, color=color)
    
    return update
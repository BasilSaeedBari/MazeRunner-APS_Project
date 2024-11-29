# Player Data.py
import pyray as rl

def Character(
    Name: str,
    xPos : float,
    yPos : float,
    width : float,
    height: float,
    health : float,
    stamina : float,
    color
    ):
    properties = {
    "name" : Name,
    "walk_speed" : 10,
    "sprint_speed" : 30,
    "jump_strength" : 5,
    "health" : health,
    "stamina" : stamina,
    "xPos" : xPos,
    "yPos" : yPos,
    "width" : width,
    "height" : height,
    "color" : color,
    "on_ground" : True,
    "xVelocity": 0,
    "yVelocity": 0,
    }
    
    return properties
    
    
def update(character : dict, platform_list: list):
    """
    Updates the character's state, including movement, jumping, and collisions.
    Handles gravity and on-ground logic in one place.
    """
    # Handle movement
    move(character)

    # Create a rectangle for the character
    character_rect = rl.Rectangle(
        character["xPos"], character["yPos"], character["width"], character["height"]
    )

    # Check for collisions with platforms
    character["on_ground"] = False  # Assume the character is not on the ground
    for platform in platform_list:
        platform_rect = platform["rect"]
        
        # Check if collision occurs
        if rl.check_collision_recs(character_rect, platform_rect):
            # Determine collision directions by calculating overlap
            overlap_left = (character_rect.x + character_rect.width) - platform_rect.x
            overlap_right = (platform_rect.x + platform_rect.width) - character_rect.x
            overlap_top = (character_rect.y + character_rect.height) - platform_rect.y
            overlap_bottom = (platform_rect.y + platform_rect.height) - character_rect.y

            # Find the minimum overlap to determine collision side
            min_overlap = min(
                abs(overlap_left), 
                abs(overlap_right), 
                abs(overlap_top), 
                abs(overlap_bottom)
            )

            # Vertical (Ground/Ceiling) Collision
            if min_overlap == abs(overlap_top) or min_overlap == abs(overlap_bottom):
                # Ground collision
                if character["yVelocity"] > 0 and min_overlap == abs(overlap_top):
                    character["yPos"] = platform_rect.y - character["height"]
                    character["yVelocity"] = 0
                    character["on_ground"] = True
                
                # Ceiling collision
                elif character["yVelocity"] < 0 and min_overlap == abs(overlap_bottom):
                    character["yPos"] = platform_rect.y + platform_rect.height
                    character["yVelocity"] = 0

            # Horizontal (Wall) Collision
            elif min_overlap == abs(overlap_left) or min_overlap == abs(overlap_right):
                # Left wall collision
                if character["xVelocity"] > 0 and min_overlap == abs(overlap_left):
                    character["xPos"] = platform_rect.x - character["width"]
                    character["xVelocity"] = 0
                
                # Right wall collision
                elif character["xVelocity"] < 0 and min_overlap == abs(overlap_right):
                    character["xPos"] = platform_rect.x + platform_rect.width
                    character["xVelocity"] = 0

    # Apply gravity if not on ground
    if not character["on_ground"]:
        apply_gravity(character)
        
    
def draw(character : dict):
    rl.draw_rectangle(
        int(character["xPos"]), 
        int(character["yPos"]), 
        int(character["width"]), 
        int(character["height"]), 
        character["color"]
    )
    
def jump(character : dict):
    if character["on_ground"] and (rl.is_key_down(rl.KEY_W) or rl.is_key_down(rl.KEY_SPACE)):
        # Set an initial negative vertical velocity to simulate jumping up
        character["yVelocity"] = -character["jump_strength"]
        character["on_ground"] = False  # Character is now in the air
    
def move(character : dict):
    """
    Handles horizontal movement and jumping.
    """
    if rl.is_key_down(rl.KEY_LEFT_SHIFT):
        speed = character["sprint_speed"]
    else:
        speed = character["walk_speed"]

    # Adjust horizontal velocity
    if rl.is_key_down(rl.KEY_A) or rl.is_key_down(rl.KEY_LEFT):
        character["xVelocity"] = -speed
    elif rl.is_key_down(rl.KEY_D) or rl.is_key_down(rl.KEY_RIGHT):
        character["xVelocity"] = speed
    else:
        # Apply easing deceleration to horizontal velocity
        character["xVelocity"] = easing_exponential_deceleration(
            character["xVelocity"], target_speed=0, factor=0.2
        )

    # Handle jumping
    jump(character)

    # Update position based on velocity
    character["xPos"] += character["xVelocity"]
    character["yPos"] += character["yVelocity"]
    
    
    
def walking(character: dict):
    if rl.is_key_down(rl.KEY_A) or rl.is_key_down(rl.KEY_LEFT):  # Move left
        character["xPos"] -= character["walk_speed"]
    elif rl.is_key_down(rl.KEY_D) or rl.is_key_down(rl.KEY_RIGHT):  # Move right
        character["xPos"] += character["walk_speed"]
    
def sprinting(character: dict):
    if rl.is_key_down(rl.KEY_LEFT_SHIFT):  # Hold shift to sprint
        if rl.is_key_down(rl.KEY_A) or rl.is_key_down(rl.KEY_LEFT):  # Sprint left
            character["xPos"] -= character["sprint_speed"]
        elif rl.is_key_down(rl.KEY_D) or rl.is_key_down(rl.KEY_RIGHT):  # Sprint right
            character["xPos"] += character["sprint_speed"]
    
def easing_exponential_deceleration(current_speed, target_speed, factor=0.1):
    """
    Exponential decay for smooth stopping.
    current_speed: current speed of the character.
    target_speed: the speed to ease towards (usually 0 for stopping).
    factor: the rate of decay (higher = faster stop).
    """
    return current_speed + (target_speed - current_speed) * factor
    
def easing_jump(character: dict, factor=0.1):
    """
    Handles the easing deceleration for the jump landing.
    """
    if character["on_ground"]:
        character["yPos"] = easing_exponential_deceleration(
            character["yPos"], target_speed=0, factor=factor
        )  

  
def apply_gravity(character: dict, gravity=0.5, terminal_velocity=20):
    """
    Applies gravity to the character when they're not on the ground.
    """
    if not character["on_ground"]:
        character["yVelocity"] += gravity
        character["yVelocity"] = min(character["yVelocity"], terminal_velocity)
    else:
        character["yVelocity"] = 0

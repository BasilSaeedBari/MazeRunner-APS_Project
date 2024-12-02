# level 1


import platforms
import pyray as rl 
import coins


def make_level_1():
    map = {}
    
    # Base floor and walls
    floor = platforms.ground(xPos=0, yPos=640, width=1280, height=80, color=rl.BROWN)
    left_wall = platforms.wall(xPos=0, yPos=0, width=50, height=640, color=rl.DARKGRAY)
    right_wall = platforms.wall(xPos=1230, yPos=0, width=50, height=640, color=rl.DARKGRAY)
    
    # Platforms left side
    platform_1 = platforms.ground(xPos=280, yPos=560, width=200, height=30, color=rl.BLACK)
    platform_2 = platforms.ground(xPos=123, yPos=335, width=150, height=30, color=rl.BLACK)
    platform_3 = platforms.ground(xPos=438, yPos=450, width=230, height=30, color=rl.BLACK)
    
    # Bad platform left side
    platform_4 = platforms.ground(xPos=368, yPos=240, width=200, height=30, color=rl.RED)
    
    # Middle walls
    middle_wall1 = platforms.ground(xPos=700, yPos=350, width=30, height=640, color=rl.DARKGRAY)
    middle_wall2 = platforms.ground(xPos=700, yPos=0, width=30, height=300, color=rl.DARKGRAY)

    # platform right side
    platform_5 = platforms.ground(xPos=780, yPos=560, width=200, height=30, color=rl.BLACK)
    platform_6 = platforms.ground(xPos=1003, yPos=335, width=150, height=30, color=rl.RED)
    platform_7 = platforms.ground(xPos=838, yPos=450, width=230, height=30, color=rl.BLACK)
    platform_8 = platforms.ground(xPos=775, yPos=300, width=150, height=30, color=rl.BLACK)
    # End
    end_platform = platforms.ground(xPos = 900, yPos= 200, width=200, height=30 , color=rl.GREEN)
    # Hazard platforms
    #damage_platform_1 = platforms.damage_ground(xPos=350, yPos=550, width=100, height=20)
    #damage_platform_2 = platforms.damage_ground(xPos=900, yPos=550, width=100, height=20)
    
    # Coins
    coins_list = [
        coins.coin(xPos=225, yPos=460, radius=20, color=rl.GOLD),
        coins.coin(xPos=500, yPos=410, radius=20, color=rl.GOLD),
        coins.coin(xPos=775, yPos=260, radius=20, color=rl.GOLD),
        coins.coin(xPos=1025, yPos=400, radius=20, color=rl.GOLD),
    ]
    
    # Player position
    player_x = 100
    player_y = 540
    
    # Assemble the map
    platform_list = [ 
                    platform_1, 
                    platform_2, 
                    platform_3, 
                    platform_4, 
                    #damage_platform_1, 
                    #damage_platform_2,
                    middle_wall1,
                    middle_wall2,
                    platform_5,
                    platform_6,
                    platform_7,
                    platform_8,
                    end_platform,
                    floor, 
                    left_wall, 
                    right_wall]
    map["platforms"] = platform_list
    map["xPos_Player"] = player_x
    map["yPos_Player"] = player_y
    map["state"] = 0
    map["score"] = 0
    map["coins"] = coins_list
    
    return map
    
    
def make_level_2():
    map = {}
    map["score"] = 0
    # Define the player starting position
    map["xPos_Player"] = 100.0
    map["yPos_Player"] = 580.0
    map["state"] = 0
    # Define ground and walls
    floor = platforms.ground(xPos=0, yPos=640, width=1280, height=80, color=rl.BROWN)
    left_wall = platforms.wall(xPos=0, yPos=0, width=50, height=640, color=rl.DARKGRAY)
    right_wall = platforms.wall(xPos=1230, yPos=0, width=50, height=640, color=rl.DARKGRAY)

    # Define platforms for the maze
    platform1 = platforms.ground(xPos=100, yPos=540, width=200, height=20, color=rl.GRAY)
    platform2 = platforms.ground(xPos=400, yPos=460, width=150, height=20, color=rl.GRAY)
    platform3 = platforms.ground(xPos=700, yPos=380, width=200, height=20, color=rl.GRAY)
    platform4 = platforms.ground(xPos=500, yPos=300, width=150, height=20, color=rl.GRAY)
    platform5 = platforms.ground(xPos=200, yPos=220, width=150, height=20, color=rl.GRAY)
    platform6 = platforms.ground(xPos=50, yPos=140, width=200, height=20, color=rl.GRAY)

    # Define the top platform where the player reaches the goal
    goal_platform = platforms.ground(xPos=500, yPos=40, width=300, height=20, color=rl.GREEN)

    # Add all platforms to the map
    platform_list = [
        floor,
        left_wall,
        right_wall,
        platform1,
        platform2,
        platform3,
        platform4,
        platform5,
        platform6,
        goal_platform,
    ]
    map["platforms"] = platform_list

    return map


def make_level_3():
    map = {}
    map["state"] = 0
    # Define the player starting position
    map["xPos_Player"] = 100.0
    map["yPos_Player"] = 580.0
    map["score"] = 0
    # Define the ground and walls
    floor = platforms.ground(xPos=0, yPos=640, width=1280, height=80, color=rl.BROWN)
    left_wall = platforms.wall(xPos=0, yPos=0, width=50, height=640, color=rl.DARKGRAY)
    right_wall = platforms.wall(xPos=1230, yPos=0, width=50, height=640, color=rl.DARKGRAY)

    # Core branching platforms
    platform1 = platforms.ground(xPos=100, yPos=540, width=150, height=20, color=rl.GRAY)
    platform2 = platforms.ground(xPos=400, yPos=500, width=120, height=20, color=rl.GRAY)
    platform3 = platforms.ground(xPos=600, yPos=520, width=120, height=20, color=rl.GRAY)
    platform4 = platforms.ground(xPos=800, yPos=460, width=120, height=20, color=rl.GRAY)
    platform5 = platforms.ground(xPos=1050, yPos=400, width=150, height=20, color=rl.GRAY)

    # Adding dead ends
    dead_end1 = platforms.ground(xPos=500, yPos=600, width=150, height=20, color=rl.RED)
    dead_end2 = platforms.ground(xPos=900, yPos=480, width=80, height=20, color=rl.RED)

    # Vertical precision jumps
    platform6 = platforms.ground(xPos=700, yPos=360, width=150, height=20, color=rl.GRAY)
    platform7 = platforms.ground(xPos=500, yPos=320, width=120, height=20, color=rl.GRAY)
    platform8 = platforms.ground(xPos=300, yPos=280, width=150, height=20, color=rl.GRAY)

    # Tight sequence
    tight1 = platforms.ground(xPos=200, yPos=200, width=80, height=20, color=rl.GRAY)
    tight2 = platforms.ground(xPos=400, yPos=180, width=80, height=20, color=rl.GRAY)
    tight3 = platforms.ground(xPos=600, yPos=140, width=80, height=20, color=rl.GRAY)

    # Climbing maze to the top
    climb1 = platforms.ground(xPos=100, yPos=100, width=200, height=20, color=rl.GRAY)
    climb2 = platforms.ground(xPos=400, yPos=80, width=150, height=20, color=rl.GRAY)
    climb3 = platforms.ground(xPos=700, yPos=60, width=200, height=20, color=rl.GRAY)

    # Final goal platform
    goal_platform = platforms.ground(xPos=1000, yPos=40, width=250, height=20, color=rl.GREEN)

    # Add all platforms to the map
    platform_list = [
        floor,
        left_wall,
        right_wall,
        platform1,
        platform2,
        platform3,
        platform4,
        platform5,
        platform6,
        platform7,
        platform8,
        tight1,
        tight2,
        tight3,
        dead_end1,
        dead_end2,
        climb1,
        climb2,
        climb3,
        goal_platform,
    ]
    map["platforms"] = platform_list
    return map


def make_level_4():
    map = {}
    map["state"] = 0
    # Player starting position
    map["xPos_Player"] = 100.0
    map["yPos_Player"] = 640.0  # Start near the bottom
    map["score"] = 0
    # Ground and boundary walls
    floor = platforms.ground(xPos=0, yPos=640, width=1280, height=80, color=rl.BROWN)
    left_wall = platforms.wall(xPos=0, yPos=0, width=50, height=640, color=rl.DARKGRAY)
    right_wall = platforms.wall(xPos=1230, yPos=0, width=50, height=640, color=rl.DARKGRAY)

    # Bottom Layer Platforms (Main Navigation)
    bottom_platforms = [
        platforms.ground(xPos=100, yPos=560, width=200, height=20, color=rl.GRAY),
        platforms.ground(xPos=400, yPos=520, width=150, height=20, color=rl.GRAY),
        platforms.ground(xPos=600, yPos=480, width=180, height=20, color=rl.GRAY),
        platforms.ground(xPos=900, yPos=440, width=200, height=20, color=rl.GRAY)
    ]

    # Tricky Intermediate Platforms (Requires Precision Jumping)
    mid_platforms = [
        platforms.ground(xPos=250, yPos=400, width=100, height=20, color=rl.LIGHTGRAY),
        platforms.ground(xPos=500, yPos=360, width=120, height=20, color=rl.LIGHTGRAY),
        platforms.ground(xPos=750, yPos=320, width=90, height=20, color=rl.LIGHTGRAY),
        platforms.ground(xPos=1000, yPos=280, width=100, height=20, color=rl.LIGHTGRAY)
    ]

    # Narrow Platforms (Extreme Difficulty)
    narrow_platforms = [
        platforms.ground(xPos=150, yPos=240, width=60, height=20, color=rl.RED),
        platforms.ground(xPos=350, yPos=200, width=50, height=20, color=rl.RED),
        platforms.ground(xPos=550, yPos=160, width=40, height=20, color=rl.RED),
        platforms.ground(xPos=750, yPos=120, width=60, height=20, color=rl.RED)
    ]

    # Vertical Challenge Platforms
    vertical_challenge = [
        platforms.ground(xPos=200, yPos=100, width=100, height=20, color=rl.BLUE),
        platforms.ground(xPos=450, yPos=80, width=120, height=20, color=rl.BLUE),
        platforms.ground(xPos=700, yPos=60, width=150, height=20, color=rl.BLUE)
    ]

    # Dead-End Traps (Punish Incorrect Paths)
    dead_ends = [
        platforms.ground(xPos=300, yPos=520, width=80, height=20, color=rl.RED),
        platforms.ground(xPos=650, yPos=400, width=70, height=20, color=rl.RED),
        platforms.ground(xPos=950, yPos=200, width=60, height=20, color=rl.RED)
    ]

    # Goal Platform
    goal_platform = platforms.ground(xPos=1000, yPos=40, width=230, height=20, color=rl.GREEN)

    # Combine all platforms
    platform_list = (
        [floor, left_wall, right_wall, goal_platform] + 
        bottom_platforms + 
        mid_platforms + 
        narrow_platforms + 
        vertical_challenge + 
        dead_ends
    )

    map["platforms"] = platform_list

    return map
   
def make_level_5():
    map = {}
    map["state"] = 0
    # Initial player position (trapped between walls at the bottom)
    map["xPos_Player"] = 640.0
    map["yPos_Player"] = 580.0
    map["score"] = 0

    # Base floor and walls
    floor = platforms.ground(xPos=0, yPos=640, width=1280, height=80, color=rl.BROWN)
    left_wall = platforms.wall(xPos=0, yPos=0, width=50, height=640, color=rl.DARKGRAY)
    right_wall = platforms.wall(xPos=1230, yPos=0, width=50, height=640, color=rl.DARKGRAY)

    # Horizontal moving platforms (stacked vertically to climb)
    moving_platform_1 = platforms.moving_horizontal(xPos=100, yPos=550, width=150, height=20, color=rl.BLACK, speed=3, move_range=700-100)
    moving_platform_2 = platforms.moving_horizontal(xPos=200, yPos=450, width=150, height=20, color=rl.BLACK, speed=2.5, move_range=700-200)
    moving_platform_3 = platforms.moving_horizontal(xPos=300, yPos=350, width=150, height=20, color=rl.BLACK, speed=2, move_range=700-300)
    moving_platform_4 = platforms.moving_horizontal(xPos=400, yPos=250, width=150, height=20, color=rl.BLACK, speed=1.5, move_range=700-400)
    moving_platform_5 = platforms.moving_horizontal(xPos=500, yPos=150, width=150, height=20, color=rl.BLACK, speed=1, move_range=700-500)

    # Goal platform at the top
    goal_platform = platforms.ground(xPos=550, yPos=50, width=200, height=20, color=rl.GREEN)

    # Player position
    player_x = 100
    player_y = 580

    # Assemble the map
    platform_list = [
        floor,
        left_wall,
        right_wall,
        moving_platform_1,
        moving_platform_2,
        moving_platform_3,
        moving_platform_4,
        moving_platform_5,
        goal_platform,
    ]
    map["platforms"] = platform_list

    return map

def make_level_6():
    map = {}
    map["state"] = 0
    # Initial player position
    map["xPos_Player"] = 100.0
    map["yPos_Player"] = 540.0
    map["score"] = 0
    # Define ground and walls
    floor = platforms.ground(xPos=0, yPos=640, width=1280, height=80, color=rl.BROWN)
    left_wall = platforms.wall(xPos=0, yPos=0, width=50, height=640, color=rl.DARKGRAY)
    right_wall = platforms.wall(xPos=1230, yPos=0, width=50, height=640, color=rl.DARKGRAY)

    # Horizontal moving platform (left to right)
    horizontal_platform = platforms.moving_horizontal(xPos=200, yPos=500, width=150, height=20, color=rl.DARKBLUE, speed=1, move_range=300)

    # Vertical moving platform (up and down)
    vertical_platform = platforms.moving_vertical(xPos=600, yPos=400, width=150, height=20, color=rl.DARKGREEN, speed=1, move_range=200)

    # Short horizontal moving platform (small movement range)
    short_horizontal_platform = platforms.moving_short_horizontal(xPos=800, yPos=300, width=120, height=20, color=rl.RED, speed=1, move_pixels=200)

    # Add all platforms to the list
    platform_list = [
        floor,
        left_wall,
        right_wall,
        horizontal_platform,
        vertical_platform,
        short_horizontal_platform,
    ]
    
    # For the moving platforms, we need to update their position during each game loop
    map["platforms"] = platform_list

    return map



   
def select_level(map, current_level):
    
    changed = False
    current = current_level
    if rl.is_key_pressed(rl.KEY_ONE):
        map = make_level_1()
        changed = True
        current = 1
    elif rl.is_key_pressed(rl.KEY_TWO):
        map = make_level_2()
        changed = True
        current = 2
    elif rl.is_key_pressed(rl.KEY_THREE):
        map = make_level_3()
        changed = True
        current = 3
    elif rl.is_key_pressed(rl.KEY_FOUR):
        map = make_level_4()
        changed = True
        current = 4
    elif rl.is_key_pressed(rl.KEY_FIVE):
        map = make_level_5()
        changed = True
        current = 5
    elif rl.is_key_pressed(rl.KEY_SIX):
        map = make_level_6()
        changed = True
        current = 6
        
        
    return map, changed, current
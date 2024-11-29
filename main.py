# Main.py

import pyray as rl
import player
import platforms
import map

def main():
    # Screen settings
    screen_width = 1280
    screen_height = 720
    rl.init_window(screen_width, screen_height, "Super Mario Clone")
    rl.set_target_fps(60)

    # Initialize game objects
    MazeRunner = player.Character(Name = "Humna", xPos=100.0, yPos=540., width=30., height=50., health = 100., stamina = 100, color=rl.GREEN)
    
    floor = platforms.ground(xPos=0, yPos=640, width=1280, height=80, color=rl.BROWN)
    left_wall = platforms.wall(xPos=0, yPos=0, width=50, height=640, color=rl.DARKGRAY)

    score = 0
    print("I was here")
    # Game loop
    platform_list = [floor, left_wall]
    maps = {}
    maps["platforms"] = platform_list
    
    
    
    while not rl.window_should_close():
        print(rl.get_fps())
        rl.begin_drawing()
        rl.clear_background(rl.RAYWHITE)

 
        
        # Draw the Mazerunner
        player.update(MazeRunner, maps["platforms"])
        player.draw(MazeRunner)
        
        # Drawing the map elements
        map.render_map(maps)
        

       # Display FPS and Score
        rl.draw_text(f"FPS: {rl.get_fps()}", 10, 10, 20, rl.BLACK)
        rl.draw_text(f"Score: {score}", 10, 40, 20, rl.BLACK)
        
        
        rl.end_drawing()
    rl.close_window()



main()
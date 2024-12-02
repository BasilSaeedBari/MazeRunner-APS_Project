# Main.py

import pyray as rl
import player
import map
import levels

def main():
    # Screen settings
    screen_width = 1280
    screen_height = 720
    rl.init_window(screen_width, screen_height, "Super Mario Clone")
    rl.set_target_fps(60)
    
    maps = levels.make_level_1()
    current_level = 1
    # Initialize game objects

    MazeRunner = player.Character(Name = "Humna", xPos= maps["xPos_Player"], yPos= maps["yPos_Player"], width=30., height=50., health = 100., stamina = 100, color=rl.GREEN)

    score = maps["score"]

    # Game loop    
    while not rl.window_should_close():
        score = maps["score"]


        rl.begin_drawing()
        rl.clear_background(rl.DARKBLUE)

 
        
        # Draw the Mazerunner
        player.update(MazeRunner, maps)
        player.draw(MazeRunner)
        
        # Drawing the map elements
        map.render_map(maps)
        
        # Selecting levels
        maps, changed, current_level = levels.select_level(maps, current_level)
        if changed:
            MazeRunner["xPos"] = maps["xPos_Player"]
            MazeRunner["yPos"] = maps["yPos_Player"]

       # Display FPS and Score
        rl.draw_text(f"FPS: {rl.get_fps()}", 1000, 10, 20, rl.BLACK)
        rl.draw_text(f"Score: {score}", 1000, 40, 20, rl.BLACK)
        rl.draw_text(f"Level : {current_level}", 1000, 60, 20, rl.BLACK)
        
        # Draw health
        rl.draw_text(f"Health : {(MazeRunner["health"]):.02f}", 10+50, 10, 20, rl.BLACK)
        rl.draw_rectangle(10+50, 30, int(MazeRunner["health"])*2, 20, rl.DARKPURPLE)

        if maps["state"] == 1:
            rl.draw_text("WON", 1280//2 - 60, 720//2 - 60, 60, rl.GREEN)
            rl.draw_text("go to next level", 1280//2 - (60*4), 720//2 , 60, rl.GREEN)

        rl.end_drawing()

    rl.close_window()



main()
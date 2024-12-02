# Map.py
import pyray as rl


# def render_map1(map):

#     for platform in map["platforms"]:
#         if callable(platform):
#             # Call the update function for moving platforms
#             platform_instance = platform()
#             rl.draw_rectangle_rec(platform_instance["rect"], platform_instance["color"])
#         else:
#             # Static platform
#             rl.draw_rectangle_rec(platform["rect"], platform["color"])

#     try:    
#         for coins in map["coins"]:
#             if coins["state"] == 1:
#                 circles = coins["circle"]
#                 rl.draw_circle(circles["xPos"], circles["yPos"], circles["radius"], coins["color"])
#     except:
#         print("No coins")


def render_map1_recursive(map, key=None, index=0):
    if key is None:  # Initial call
        # Process platforms first
        render_map1_recursive(map, "platforms")
        # Then process coins
        render_map1_recursive(map, "coins")
        return

    # Base case: If the list for the current key is exhausted
    if index >= len(map.get(key, [])):
        return

    if key == "platforms":
        platform = map["platforms"][index]
        if callable(platform):
            # Call the update function for moving platforms
            platform_instance = platform()
            rl.draw_rectangle_rec(platform_instance["rect"], platform_instance["color"])
        else:
            # Static platform
            rl.draw_rectangle_rec(platform["rect"], platform["color"])
    elif key == "coins":
        try:
            coin = map["coins"][index]
            if coin["state"] == 1:
                circles = coin["circle"]
                rl.draw_circle(circles["xPos"], circles["yPos"], circles["radius"], coin["color"])
        except Exception:
            print("No coins")
            return

    # Recursive step: Process the next item in the list
    render_map1_recursive(map, key, index + 1)


# Testing code
def process_platforms(platforms, index=0):
    if index >= len(platforms):
        return  # Base case: all platforms processed

    platform = platforms[index]
    if callable(platform):
        # Call the update function for moving platforms
        platform_instance = platform()
        rl.draw_rectangle_rec(platform_instance["rect"], platform_instance["color"])
    else:
        # Static platform
        rl.draw_rectangle_rec(platform["rect"], platform["color"])

    # Recursive call for the next platform
    process_platforms(platforms, index + 1)

# Example invocation
def render_map(map):
    render_map1_recursive(map)


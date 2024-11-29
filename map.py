# Map.py
import pyray as rl


def render_map(map):
    for platforms in map["platforms"]:
        rl.draw_rectangle_rec(platforms["rect"], platforms["color"])


def coin(xPos, yPos, radius, color):
    state = 1
    circle = {}
    circle["xPos"] = xPos
    circle["yPos"] = yPos
    circle["radius"] = radius

    return {"circle" : circle, "color": color, "state" : state}
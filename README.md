# 2D Platformer Game Project

## Overview

This is a 2D platformer game prototype developed using Pyray (a Python binding for Raylib), featuring basic character movement, physics, and platform interaction mechanics. The project demonstrates core game development concepts including character control, collision detection, and simple game loop implementation.

## Features

- **Character Mechanics**
  - Smooth horizontal movement with walking and sprinting
  - Jump mechanics with gravity simulation
  - Collision detection with platforms
  - Velocity-based movement with easing deceleration

- **Physics System**
  - Realistic gravity implementation
  - Collision resolution for ground, ceiling, and wall interactions
  - Exponential velocity decay for natural movement

- **Rendering**
  - Simple rectangular character and platform rendering
  - Basic game state tracking (FPS, score)
  - Configurable screen dimensions

## Technical Details

### Dependencies
- Pyray (Raylib Python binding)
- Python 3.x

### Key Components
- `Player.py`: Character creation, movement, and physics
- `Main.py`: Game loop and initialization
- `Platforms.py`: Platform object creation
- `Map.py`: Map rendering and management

## Installation

Just Install the file and run

## Current Limitations
- Basic rectangular graphics
- Single character and limited platform types
- No advanced game mechanics (enemies, scoring, levels)

## Future Roadmap
- Enhanced graphics and character design
- More complex platform interactions
- Level progression system

## Contributing
Contributions are welcome. Please open an issue or submit a pull request.

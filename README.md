# Aim Trainer

Aim Trainer is a simple game built with Python and Pygame that helps you improve your aiming skills by clicking on targets that appear and grow on the screen. The game tracks your performance including the number of targets hit, missed, and your accuracy.

## Features

- **Dynamic Targets:** Targets grow and shrink, adding a challenge to hit them accurately.
- **Score Tracking:** Tracks your hits, misses, speed, and accuracy.
- **End Screen:** Displays your performance stats at the end of the game.

## Game Mechanics
- **Targets:** Randomly appear on the screen and grow to a maximum size before shrinking back down.
- **Collisions:** Click on the targets to "hit" them. Missing the targets will count against your lives.
- **Lives:** You start with 3 lives. Missing too many targets ends the game.
- **Score Display:** Your hits, speed (targets per second), and remaining lives are displayed at the top of the screen.

## Controls
- **Mouse Click:** Click to hit the targets.
- **Quit:** Close the window or press any key during the end screen to quit.


## Installation


2. **Install the required dependencies:**
    Ensure you have Python installed. Then install the dependencies using pip:
    ```bash
    pip install pygame
    ```

## Usage

To run the game, execute the following command:
```bash
python aim_trainer.py

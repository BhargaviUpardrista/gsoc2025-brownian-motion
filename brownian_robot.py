# brownian_robot.py

import numpy as np
import random

class BrownianRobot:
    def __init__(self, x, y, speed, arena_size):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = random.uniform(0, 2 * np.pi)  # angle in radians
        self.arena_size = arena_size

    def move(self):
        self.x += self.speed * np.cos(self.direction)
        self.y += self.speed * np.sin(self.direction)

        if self.check_collision():
            self.bounce()

    def check_collision(self):
        return (
            self.x <= 0 or self.x >= self.arena_size or
            self.y <= 0 or self.y >= self.arena_size
        )

    def bounce(self):
        # Rotate randomly between 90° and 270°
        turn_angle = np.radians(random.uniform(90, 270))
        self.direction = (self.direction + turn_angle) % (2 * np.pi)
        # Move slightly away from wall to prevent sticking
        self.x = max(1, min(self.x, self.arena_size - 1))
        self.y = max(1, min(self.y, self.arena_size - 1))

    def get_position(self):
        return int(self.x), int(self.y)

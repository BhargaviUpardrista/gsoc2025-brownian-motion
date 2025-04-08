# simulate.py

import pygame
import sys
from brownian_robot import BrownianRobot

# Initialize Pygame
pygame.init()

# Arena settings
arena_size = 500
win = pygame.display.set_mode((arena_size, arena_size))
pygame.display.set_caption("Brownian Motion Robot")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Robot settings
robot_radius = 5
robot = BrownianRobot(x=arena_size / 2, y=arena_size / 2, speed=2, arena_size=arena_size)

# Clock for FPS
clock = pygame.time.Clock()

# Main loop
while True:
    clock.tick(60)  # 60 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    robot.move()
    x, y = robot.get_position()

    win.fill(WHITE)
    pygame.draw.circle(win, RED, (x, y), robot_radius)
    pygame.display.update()

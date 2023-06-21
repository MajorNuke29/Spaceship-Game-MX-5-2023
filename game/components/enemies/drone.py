from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2, SCREEN_WIDTH, SCREEN_HEIGHT, LEFT, RIGHT, UP, DOWN
import pygame
import random

class Drone(Enemy):

    WIDTH = 40
    HEIGHT = 50
    SPEED_X = 7
    SPEED_Y = 5
    INTERVAL = 6

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
        self.mov_x = random.choice(self.MOVES_X)
        self.mov_y = random.choice(self.MOVES_Y)
        self.bounces = 0

    def update(self):
        if self.bounces >= self.INTERVAL:
            self.outbounds_move()
        else:
            self.move()

        if self.rect.y  > SCREEN_HEIGHT:
            self.is_out_of_bounds = True

    def move(self):
        if self.mov_x == LEFT:
            self.rect.x -= self.SPEED_X

            if self.rect.left <= 0:
                self.mov_x = RIGHT
                self.mov_y = random.choice(self.MOVES_Y)
                self.bounces += 1
        else:
            self.rect.x += self.SPEED_X

            if self.rect.right >= SCREEN_WIDTH:
                self.mov_x = LEFT
                self.mov_y = random.choice(self.MOVES_Y)
                self.bounces += 1

        if self.mov_y == UP:
            self.rect.y -= self.SPEED_Y

            if self.rect.top <= 0:
                self.mov_y = DOWN
                self.mov_x = random.choice(self.MOVES_X)
                self.bounces += 1
        else:
            self.rect.y += self.SPEED_Y

            if self.rect.bottom >= SCREEN_HEIGHT:
                self.mov_y = UP
                self.mov_x = random.choice(self.MOVES_X)
                self.bounces += 1

    def outbounds_move(self):
        self.rect.y += (self.SPEED_Y + 4)
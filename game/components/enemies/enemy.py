from abc import abstractmethod
from game.utils.constants import SCREEN_WIDTH, LEFT, RIGHT, UP, DOWN, BULLET_ENEMY_TYPE
import pygame
import random


class Enemy(pygame.sprite.Sprite):

    X_POS_LIST = [loc for loc in range(0, (SCREEN_WIDTH + 1), 40)]
    Y_POS = -50
    SPEED_Y = 5
    SPEED_X = 3
    MOVES_X = [LEFT, RIGHT]
    MOVES_Y = [UP, DOWN]
    INTERVAL = 0
    BULLET_TYPE = BULLET_ENEMY_TYPE

    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.mov_x = random.choice(self.MOVES_X)
        self.on_screen = False

    def update(self):
        self.move()

    def shoot(self, bullet_handler):
        bullet_handler.add_bullet(self.BULLET_TYPE, self.rect.center)

    def update_on_screen(self):
        self.on_screen =  self.rect.y > 0

    @abstractmethod
    def move(self):
        "Implementation of movement behavior"


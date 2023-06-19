from abc import abstractmethod
from game.utils.constants import SCREEN_WIDTH, LEFT, RIGHT, UP, DOWN
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

    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.mov_x = random.choice(self.MOVES_X)

    # def draw(self, surface):
    #     surface.blit(self.image, self.rect)

    @abstractmethod
    def move(self):
        "Implementation of movement behavior"

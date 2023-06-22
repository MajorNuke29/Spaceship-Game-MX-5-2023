from abc import abstractmethod
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, LEFT, RIGHT, UP, DOWN, BULLET_ENEMY_TYPE
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

    def __init__(self, image, score):
        super().__init__()
        self.image = image
        self.score = score
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.mov_x = random.choice(self.MOVES_X)
        self.is_distroyed = False
        self.is_out_of_bounds = False
        self.has_entered_screen = False

    def update(self):
        if not self.has_entered_screen:
            self.update_on_screen()

    def shoot(self, bullet_handler):
        bullet_handler.add_bullet(self.BULLET_TYPE, self.rect.center)

    def get_score(self):
        return self.score

    def destroy(self):
        self.is_distroyed = True

    def was_destroyed(self):
        return self.is_distroyed
    
    def update_on_screen(self):
        self.has_entered_screen =  self.rect.y > 0

    def is_out_of_screen(self):
        return self.rect.bottom < 0 or self.rect.y > SCREEN_HEIGHT or self.rect.right < 0 or self.rect.x > SCREEN_WIDTH

    @abstractmethod
    def move(self):
        "Implementation of movement behavior"


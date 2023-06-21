import pygame

from game.components.bullets import Bullet
from game.utils.constants import BULLET

class BulletPlayer(Bullet):

    WIDTH = 20
    HEIGHT = 40
    SPEED = 15

    def __init__(self, origin):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        super().__init__(self.image, origin)

    def update(self):
        self.move()

        if self.rect.bottom < 0:
            self.kill()

    def move(self):
        self.rect.y -= self.SPEED
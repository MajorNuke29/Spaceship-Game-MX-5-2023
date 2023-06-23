import pygame

from game.utils.constants import SCREEN_HEIGHT

class PowerUp:

    SPEED = 10

    def __init__(self, image, size, location, duration, type):
        self.location = location
        self.size = size
        self.duration = duration
        self.type = type
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.is_active = True
        self.is_alive = True

    def update(self):
        self.rect.y += self.SPEED
        
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False

    def draw (self, screen):
        screen.blit(self.image, self.rect)
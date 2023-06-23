import pygame, random

from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class PowerUp:

    SIZE = (30, 30)
    POS_Y = 0
    SPEED = 10
    DURATION = 5000

    def __init__(self, image):
        self.image = image
        self.image = pygame.transform.scale(self.image, self.SIZE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(120, SCREEN_WIDTH - 120)
        self.is_alive = True

    def update(self, player):
        self.rect.y += self.SPEED
        
        if self.rect.y >= SCREEN_HEIGHT or self.rect.colliderect(player.rect):
            self.is_alive = False


    def draw (self, screen):
        screen.blit(self.image, self.rect)
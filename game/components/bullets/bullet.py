from game.utils.constants import SCREEN_HEIGHT
import pygame

class Bullet(pygame.sprite.Sprite):

    SPEED = 0

    def __init__(self, image, center):
        super().__init__()
        self.image = image
        self.rect = image.get_rect()
        self.rect.center = center
        self.is_alive = False

    def update(self):
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
import pygame

from game.utils.constants import SPACESHIP_WEAPON

class Weapon(pygame.sprite.Sprite):

    WIDTH = 15
    HEIGHT = 15

    def __init__(self, player, radius):
        super().__init__()
        self.player = player
        self.radius = radius
        self.image = SPACESHIP_WEAPON
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.player.rect.centerx - (self.WIDTH // 2)
        self.rect.centery = self.player.rect.centery - (80 + (self.HEIGHT // 2))

    def update(self):
        pass

    def draw(self, screen):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        vector_mouse = pygame.math.Vector2((mouse_x - self.player.rect.centerx), (mouse_y - self.player.rect.centery))

        vector_mouse.scale_to_length(self.radius)

        self.rect.center = (self.player.rect.centerx + vector_mouse.x, self.player.rect.centery + vector_mouse.y)

        screen.blit(self.image, self.rect)

    def move(self):
        pass
from game.utils.constants import BULLET_ENEMY_TYPE
from game.components.bullets.bullet_enemy import BulletEnemy
import pygame

class BulletHandler:
    def __init__(self):
        self.bullets = pygame.sprite.Group()

    def update(self, player):
        for bullet in self.bullets:
            bullet.update()

            if pygame.sprite.collide_rect(bullet, player):
                player.start_blink()

            if not bullet.alive():
                self.remove_bullet(bullet)

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
            self.bullets.add(BulletEnemy(center))

    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)
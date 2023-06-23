import pygame

from game.components.bullets import BulletEnemy, BulletPlayer
from game.components import ExplosionHandler

class BulletHandler:
    def __init__(self, bullet_factory):
        self.bullets = pygame.sprite.Group()
        self.bullet_factory = bullet_factory
        self.explosion_handler = ExplosionHandler()

    def update(self, player, enemies):
        for bullet in self.bullets:
            bullet.update()

            if type(bullet) == BulletEnemy:
                self.check_player_collition(bullet, player)
            elif type(bullet) == BulletPlayer:
                self.check_enemies_collition(bullet, enemies)

        self.explosion_handler.update()

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

        self.explosion_handler.draw(screen)

    def check_player_collition(self, bullet, player):
        if pygame.sprite.collide_rect(bullet, player) and not player.is_blinking:
            player.start_blink()
            player.reduce_lifes()

    def check_enemies_collition(self, bullet, enemies):
        enemies_collided = pygame.sprite.spritecollide(bullet, enemies, False)

        if len(enemies_collided) > 0:
            bullet.kill()
            for enemy in enemies_collided:
                enemy.destroy()
                self.explosion_handler.add_explosion(enemy.rect.center)


    def add_bullet(self, bullet_type, origin):
            bullet = self.bullet_factory.get_bullet(bullet_type, origin)
            self.bullets.add(bullet)

    def reset(self):
        self.bullets.empty()
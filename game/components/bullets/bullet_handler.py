import pygame

from game.components.bullets import BulletEnemy, BulletPlayer, MisileBullet
from game.utils.constants import ENEMY_EXPLOSION, MISILE_EXPLOSION

class BulletHandler:
    def __init__(self, bullet_factory):
        self.bullets = pygame.sprite.Group()
        self.bullet_factory = bullet_factory

    def update(self, player, enemies, powerup_handler, explosion_handler):
        for bullet in self.bullets:
            bullet.update()

            if type(bullet) == BulletEnemy:
                self.check_player_collition(bullet, player)
            elif type(bullet) == BulletPlayer:
                self.check_enemies_collition(bullet, enemies, powerup_handler, explosion_handler)
            elif type(bullet) == MisileBullet:
                self.check_enemies_collition(bullet, enemies, powerup_handler, explosion_handler, bullet_has_explotion = True)

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def check_player_collition(self, bullet, player):
        if pygame.sprite.collide_rect(bullet, player) and not player.is_blinking:
            if not player.is_invincible:
                player.start_blink()
                player.reduce_lifes()
                bullet.kill()


    def check_enemies_collition(self, bullet, enemies, powerup_handler, explosion_handler, bullet_has_explotion = False):
        enemies_collided = pygame.sprite.spritecollide(bullet, enemies, False)

        if len(enemies_collided) > 0:
            bullet.kill()

            if bullet_has_explotion:
                explosion_handler.add_explosion(MISILE_EXPLOSION, enemies_collided[0].rect.center)

            for enemy in enemies_collided:
                enemy.destroy()
                powerup_handler.add_powerup(enemy.rect.center)
                explosion_handler.add_explosion(ENEMY_EXPLOSION, enemy.rect.center)


    def add_bullet(self, bullet_type, origin):
            bullet = self.bullet_factory.get_bullet(bullet_type, origin)
            self.bullets.add(bullet)

    def reset(self):
        self.bullets.empty()
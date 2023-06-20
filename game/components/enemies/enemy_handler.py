from game.components.enemies import Enemyfactory
from game.components.enemies import Follower
import pygame

class EnemyHandler:

    MAX_ENEMIES = 5
    ENEMY_FACTORY = Enemyfactory()

    def __init__(self):
        self.enemies = pygame.sprite.Group()

    def update(self, player):
        for enemy in self.enemies:
            if type(enemy) == Follower:
                enemy.update(player.rect.x, player.rect.y)
            else:
                enemy.update()

            if not enemy.alive():
                self.remove_enemy(enemy)

    def draw(self, screen, player):
        self.enemies.draw(screen)
        
        for enemy in self.get_player_collisions(player):
            pygame.draw.rect(screen, (255, 14, 14), enemy.rect, 1)

    def shoot(self, bullet_handler):
        for enemy in self.enemies:
            enemy.shoot(bullet_handler)

    def add_enemy(self):
        if len(self.enemies) < self.MAX_ENEMIES:
            new_enemy = self.ENEMY_FACTORY.get_rand_enemy()
            self.enemies.add(new_enemy)

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def get_player_collisions(self, player):
        return pygame.sprite.spritecollide(player, self.enemies, False)

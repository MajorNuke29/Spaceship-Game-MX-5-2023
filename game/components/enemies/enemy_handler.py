from game.components.enemies import Enemyfactory
from game.components.enemies import Follower
import pygame

class EnemyHandler:

    MAX_ENEMIES = 5
    ENEMY_FACTORY = Enemyfactory()

    def __init__(self, player):
        self.enemies = pygame.sprite.Group()
        self.player = player

    def update(self):
        for enemy in self.enemies:
            if type(enemy) == Follower:
                enemy.update(self.player.rect.x, self.player.rect.y)
            else:
                enemy.update()

            if not enemy.alive():
                self.remove_enemy(enemy)

    def draw(self, screen):
        self.enemies.draw(surface = screen)
        
        for enemy in self.get_player_collisions():
            pygame.draw.rect(screen, (255, 14, 14), enemy.rect, 1)

    def add_enemy(self):
        if len(self.enemies) < self.MAX_ENEMIES:
            new_enemy = self.ENEMY_FACTORY.get_rand_enemy()
            self.enemies.add(new_enemy)

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def get_player_collisions(self):
        return pygame.sprite.spritecollide(self.player, self.enemies, False)

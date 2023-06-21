import pygame

from game.components.enemies import Follower

class EnemyHandler:

    def __init__(self, enemy_factory):
        self.enemies = pygame.sprite.Group()
        self.enemy_factory = enemy_factory

    def update(self, player):
        for enemy in self.enemies:
            if type(enemy) == Follower:
                enemy.update(player.rect.x, player.rect.y)
            else:
                enemy.update()

            if not enemy.alive():
                self.remove_enemy(enemy)

        if pygame.sprite.spritecollideany(player, self.enemies) and not player.is_blinking:
            player.start_blink()
            player.reduce_lifes()

    def draw(self, screen):
        self.enemies.draw(screen)

    def shoot(self, bullet_handler):
        for enemy in self.enemies:
            enemy.shoot(bullet_handler)

    def add_enemy(self):
        new_enemy = self.enemy_factory.get_enemy()
        
        if new_enemy != None:
            self.enemies.add(new_enemy)

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
        self.enemy_factory.reduce_instance_count()

    def get_enemies(self):
        return self.enemies

    def get_player_collisions(self, player):
        return pygame.sprite.spritecollide(player, self.enemies, False)

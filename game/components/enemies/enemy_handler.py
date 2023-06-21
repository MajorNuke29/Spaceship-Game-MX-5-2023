import pygame

from game.components.enemies import Follower

class EnemyHandler:

    def __init__(self, enemy_factory):
        self.enemies = pygame.sprite.Group()
        self.enemy_factory = enemy_factory
        self.destroyed_enemies = 0
        self.total_score = 0

    def update(self, player):
        for enemy in self.enemies:
            if type(enemy) == Follower:
                enemy.update(player.rect.x, player.rect.y)
            else:
                enemy.update()
            
            if enemy.was_destroyed():
                enemy.kill()
                self.enemy_factory.reduce_instance_count()
                self.destroyed_enemies += 1

            if enemy.is_out_of_bounds:
                enemy.kill()
                self.enemy_factory.reduce_instance_count()

        for enemy in pygame.sprite.spritecollide(player, self.enemies, False):
            if not player.is_blinking:
                player.start_blink()
                player.reduce_lifes()
                enemy.kill()
                self.enemy_factory.reduce_instance_count()

    def draw(self, screen):
        self.enemies.draw(screen)

    def shoot(self, bullet_handler):
        for enemy in self.enemies:
            enemy.shoot(bullet_handler)

    def add_enemy(self):
        new_enemy = self.enemy_factory.get_enemy()
        
        if new_enemy != None:
            self.enemies.add(new_enemy)

    def get_enemies(self):
        return self.enemies
    
    def get_destroyed_enemies_count(self):
        return self.destroyed_enemies

    def get_player_collisions(self, player):
        return pygame.sprite.spritecollide(player, self.enemies, False)
    
    def reset(self):
        self.enemies.empty()
        self.enemy_factory.instance_count = 0
        self.destroyed_enemies = 0
        self.total_score = 0

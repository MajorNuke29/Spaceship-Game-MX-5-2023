from game.components.enemies import Drone, Ship, Enemyfactory
import random

class EnemyHandler:

    MAX_ENEMIES = 10
    ENEMY_FACTORY = Enemyfactory()

    def __init__(self):
        self.enemies = []

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update()
            if not enemy.is_alive:
                self.remove_enemy(enemy)
            

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < self.MAX_ENEMIES:
            index = 0
            in_same_pos = True
            new_enemy = self.ENEMY_FACTORY.get_rand_enemy()
            len_enemies = len(self.enemies)

            while in_same_pos and index < len_enemies:
                in_same_pos = new_enemy.rect.x == self.enemies[index].rect.x

                if in_same_pos:
                    new_enemy.new_x_pos()
                    index = -1

                index += 1
            

            self.enemies.append(new_enemy)

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
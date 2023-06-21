from game.utils.constants import ENEMY_DRONE_TYPE, ENEMY_SHIP_TYPE, ENEMY_FOLLOWER_TYPE, EASY_LEVEL_MAX_ENEMIES
from game.components.enemies import Drone, Ship, Follower

class Enemyfactory:

    def __init__(self, max_enemies = EASY_LEVEL_MAX_ENEMIES):
        self.max_enemies = max_enemies
        self.instance_count = 0

    def get_enemy(self, enemy_type):
        enemy = None

        if self.instance_count < self.max_enemies:
            enemy = self.__instance_enemy(enemy_type)

        return enemy
    
    def __instance_enemy(self, enemy_type):
        enemy = None

        if enemy_type == ENEMY_DRONE_TYPE:
            enemy = Drone()
            self.instance_count += 1

        elif enemy_type == ENEMY_SHIP_TYPE:
            enemy = Ship()
            self.instance_count += 1

        elif enemy_type == ENEMY_FOLLOWER_TYPE:
            enemy = Follower()
            self.instance_count += 1

        return enemy
    
    def reduce_instance_count(self):
        self.instance_count -= 1
    
    def get_max_enemies(self):
        return self.max_enemiess
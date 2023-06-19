from game.utils.constants import DRONE, SHIP, FOLLOWER
from game.components.enemies import Drone, Ship, Follower
import random


class Enemyfactory:

    ENEMIES = [DRONE, SHIP, FOLLOWER]

    def get_enemy(self, enemy_name):
        enemy = None

        if enemy_name == DRONE:
            enemy = Drone()

        elif enemy_name == SHIP:
            enemy = Ship()

        elif enemy_name == FOLLOWER:
            enemy = Follower()

        return enemy

    def get_rand_enemy(self):
        enemy = random.choice(self.ENEMIES)
        return self.get_enemy(enemy)

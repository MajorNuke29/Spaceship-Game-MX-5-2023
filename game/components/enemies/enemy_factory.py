from game.utils.constants import DRONE, SHIP
from game.components.enemies import Drone, Ship
import random

class Enemyfactory:

    ENEMIES = [DRONE, SHIP]

    def get_enemy(self, name):
        enemy = None

        if name == DRONE:
            enemy = Drone()
        elif name == SHIP:
            enemy = Ship()

        return enemy
    
    def get_rand_enemy(self):
        enemy = random.choice(self.ENEMIES)
        return self.get_enemy(enemy)

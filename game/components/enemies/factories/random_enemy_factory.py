import random

from game.components.enemies.factories import Enemyfactory
from game.utils.constants import MEDIUM_LEVEL_MAX_ENEMIES, ENEMIES_TYPES

class RandomEnemyFactory(Enemyfactory):
        
    def __init__(self):
        super().__init__(MEDIUM_LEVEL_MAX_ENEMIES) 

    def get_enemy(self):
        enemy = random.choice(ENEMIES_TYPES)
        return super().get_enemy(enemy)
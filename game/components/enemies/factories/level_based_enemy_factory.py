import random

from game.components.enemies.factories import Enemyfactory
from game.utils.constants import ENEMIES_TYPES

class LevelBasedEnemyFactory(Enemyfactory):

    def __init__(self, spawn_probabilities, max_enemies):
        super().__init__(max_enemies)
        self.spawn_probabilities = spawn_probabilities

    def get_enemy(self):
        enemy_type = random.choices(ENEMIES_TYPES, weights=self.spawn_probabilities, k=1)
        return super().get_enemy(enemy_type[0])
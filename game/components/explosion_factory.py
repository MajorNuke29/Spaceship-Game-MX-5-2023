from game.components import EnemyExplosion, MisileExplosion
from game.utils.constants import ENEMY_EXPLOSION, MISILE_EXPLOSION

class ExplosionFactory:
    def get_explosion(self, type, location):
        explosion = None

        if type == ENEMY_EXPLOSION:
            explosion = EnemyExplosion(location)
        elif type == MISILE_EXPLOSION:
            explosion = MisileExplosion(location)

        return explosion

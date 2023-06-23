from game.components import AnimatedSprite
from game.utils.constants import EXPLOSION_1_SPRITES

class EnemyExplosion(AnimatedSprite):

    SIZE = (100, 100)
    DURATION = 0.8

    def __init__(self, location):
        super().__init__(location, self.SIZE, EXPLOSION_1_SPRITES, self.DURATION)
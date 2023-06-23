from game.components import AnimatedSprite
from game.utils.constants import EXPLOSION_2_SPRITES

class MisileExplosion(AnimatedSprite):

    DURATION = 1
    SIZE = (250, 250)

    def __init__(self, location):
        super().__init__(location, self.SIZE, EXPLOSION_2_SPRITES, self.DURATION)
        self.rect = self.sprites_rects[0]
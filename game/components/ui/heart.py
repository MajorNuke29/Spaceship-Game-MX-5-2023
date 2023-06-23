import pygame

from game.components import AnimatedSprite
from game.utils.constants import HEART_SPRITES, FPS

class Heart(AnimatedSprite):

    HEART_SIZE = (25, 25)
    ANIM_DURATION_SECS = .9

    def __init__(self, location):
        super().__init__(location, self.HEART_SIZE, HEART_SPRITES, self.ANIM_DURATION_SECS)

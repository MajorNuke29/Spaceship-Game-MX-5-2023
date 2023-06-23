import pygame

from game.components.bullets import BulletPlayer
from game.utils.constants import MISILE

class MisileBullet(BulletPlayer):

    def __init__(self, origin):
        super().__init__(origin, MISILE)
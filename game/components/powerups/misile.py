import pygame

from game.components.powerups import PowerUp
from game.utils.constants import MISILE, MISILE_TYPE

class Misile(PowerUp):

    SIZE = (40, 40)
    DURATION = 10000

    def __init__(self, location):
        self.image = pygame.transform.scale(MISILE, self.SIZE)
        super().__init__(self.image, self.SIZE, location, self.DURATION, MISILE_TYPE)
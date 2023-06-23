import pygame

from game.components.powerups import PowerUp
from game.utils.constants import HEART_SPRITES, HEART_TYPE

class HealUp(PowerUp):

    SIZE = (40, 40)

    def __init__(self, location):
        self.image = pygame.transform.scale(HEART_SPRITES[0], self.SIZE)
        super().__init__(self.image, self.SIZE, location, 0, HEART_TYPE)
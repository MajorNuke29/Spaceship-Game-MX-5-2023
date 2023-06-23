import pygame 

from game.components.powerups.powerup import PowerUp
from game.utils.constants import SHIELD, SHIELD_TYPE

class Shield(PowerUp):

    SIZE = (40, 40)
    DURATION = 5000

    def __init__(self, location):
        self.image = pygame.transform.scale(SHIELD, self.SIZE)
        super().__init__(self.image, self.SIZE, location, self.DURATION, SHIELD_TYPE)
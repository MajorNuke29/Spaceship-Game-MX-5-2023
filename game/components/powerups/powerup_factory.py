import random

from game.utils.constants import SHIELD_TYPE, HEART_TYPE, MISILE_TYPE, POWERUPS_DROPS
from game.components.powerups import Shield, Misile, HealUp

class PowerupFactory:

    def __init__(self, drop_probabilities):
        self.drop_probabilities = drop_probabilities

    def __instantite_powerup(self, type, location):
        powerup = None

        if type == SHIELD_TYPE:
            powerup = Shield(location)
        elif type == HEART_TYPE:
            powerup = HealUp(location)
        elif type == MISILE_TYPE:
            powerup = Misile(location)

        return powerup

    def get_powerup(self, location):
        type = random.choices(POWERUPS_DROPS, weights=self.drop_probabilities, k=1)[0]
        return self.__instantite_powerup(type, location)
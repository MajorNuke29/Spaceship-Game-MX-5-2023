from game.components.powerups.shield import Shield

class PoweUpHandler:

    INTERVAL_TIME = 90

    def __init__(self):
        self.powerups = []
        self.cycles = 0

    def update(self, player):
        self.cycles += 1

        if self.cycles % self.INTERVAL_TIME == 0:
            self.add_powerup()
            self.cycles = 0

        for powerup in self.powerups:
            powerup.update(player)

            if not powerup.is_alive:
                self.remove_powerup(powerup)

    def draw(self, screen):
        for powerup in self.powerups:
            powerup.draw(screen)

    def add_powerup(self):
        self.powerups.append(Shield())

    def remove_powerup(self, powerup):
        self.powerups.remove(powerup)

    def reset(self):
        for powerup in self.powerups:
            powerup.reset()
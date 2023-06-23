class PoweUpHandler:

    def __init__(self, powerup_factory):
        self.powerups = []
        self.powerup_factory = powerup_factory

    def update(self, player):
        for powerup in self.powerups:
            if powerup.rect.colliderect(player.rect):
                if not player.has_powerup():
                    player.add_powerup(powerup)
                
                powerup.is_alive = False

            if not powerup.is_alive:
                self.remove_powerup(powerup)
            
            powerup.update()

    def draw(self, screen):
        for powerup in self.powerups:
            powerup.draw(screen)

    def add_powerup(self, location):
        powerup = self.powerup_factory.get_powerup(location)

        if powerup != None:
            self.powerups.append(powerup)

    def remove_powerup(self, powerup):
        self.powerups.remove(powerup)

    def reset(self):
        self.powerups = []
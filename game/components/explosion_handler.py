from game.utils.constants import EXPLOSION_1_SPRITES
from game.components import AnimatedSprite

class ExplosionHandler:

    EXPLOSION_SIZE = (100, 100)

    def __init__(self):
        self.explosions = []

    def update(self):
        for explosion in self.explosions:
            if not explosion.animation_has_started:
                explosion.start_animation()
                
            if explosion.animation_has_ended:
                self.remove_explosion(explosion)

            explosion.update()

    def draw(self, screen):
        for explosion in self.explosions:
            explosion.draw(screen)

    def add_explosion(self, location):
        explosion = AnimatedSprite(location, self.EXPLOSION_SIZE, EXPLOSION_1_SPRITES, .8)
        self.explosions.append(explosion)

    def remove_explosion(self, explosion):
        self.explosions.remove(explosion)
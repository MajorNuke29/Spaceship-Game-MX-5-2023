import pygame

from game.components import MisileExplosion
from game.utils.constants import ENEMY_EXPLOSION

class ExplosionHandler:

    def __init__(self, explosion_factory):
        self.explosions = []
        self.explosion_factory = explosion_factory

    def update(self, enemies):
        for explosion in self.explosions:

            if type(explosion) == MisileExplosion:
                enemies_collided = pygame.sprite.spritecollide(explosion, enemies, False)

                if len(enemies_collided) > 0:
                    for enemy in enemies_collided:
                        enemy.destroy()
                        self.add_explosion(ENEMY_EXPLOSION, enemy.rect.center)

            if not explosion.animation_has_started:
                explosion.start_animation()
                
            if explosion.animation_has_ended:
                self.remove_explosion(explosion)

            explosion.update()

    def draw(self, screen):
        for explosion in self.explosions:
            explosion.draw(screen)

    def add_explosion(self, type, location):
        explosion = self.explosion_factory.get_explosion(type, location)
        self.explosions.append(explosion)

    def remove_explosion(self, explosion):
        self.explosions.remove(explosion)

    def reset(self):
        self.explosions = []
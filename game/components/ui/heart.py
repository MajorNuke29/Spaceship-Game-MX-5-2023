import pygame

from game.utils.constants import HEART_SPRITES, FPS

class Heart:

    HEART_SIZE = (25, 25)
    ANIM_DURATION_SECS = 1
    ANIM_DURATION_CYCLES = ANIM_DURATION_SECS * FPS

    def __init__(self, location):
        self.location = location
        self.sprites = self.__gen_sprites()
        self.current_sprite_index = 0
        self.cycles = self.ANIM_DURATION_CYCLES
        self.interval = self.ANIM_DURATION_CYCLES // len(self.sprites)

    def update(self):
        if self.cycles <= self.ANIM_DURATION_CYCLES:
            self.cycles += 1
        
        if self.cycles % self.interval == 0 and self.cycles < self.ANIM_DURATION_CYCLES:
            self.current_sprite_index += 1

    def draw(self, screen):
        screen.blit(self.sprites[self.current_sprite_index], self.location)

    def start_animation(self):
        self.cycles = 1

    def __gen_sprites(self):
        sprites = []

        for sprite in HEART_SPRITES:
            sprite = pygame.transform.scale(sprite, self.HEART_SIZE)
            sprite.get_rect().center = self.location
            sprites.append(sprite)

        return sprites
    
    def reset(self):
        self.current_sprite_index = 0
        self.cycles = self.ANIM_DURATION_CYCLES

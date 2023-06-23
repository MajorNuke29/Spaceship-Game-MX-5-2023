import pygame

from game.utils.constants import FPS

class AnimatedSprite:

    def __init__(self, location, size, sprites_list, animation_duration):
        self.location = location
        self.size = size
        self.anim_duration_cycles = animation_duration * FPS
        self.sprites, self.sprites_rects = self.__gen_sprites(sprites_list)
        self.sprite_cuantity = len(self.sprites)
        self.current_sprite_index = 0
        self.cycles = self.anim_duration_cycles
        self.interval = self.anim_duration_cycles // len(self.sprites)
        self.next_frame = self.interval
        self.animation_has_started = False
        self.animation_has_ended = False

    def update(self):
        if self.cycles < self.anim_duration_cycles:
            self.cycles += 1

        if self.current_sprite_index  >= self.sprite_cuantity - 1:
            self.animation_has_ended = True
        
        if self.cycles == self.next_frame and not self.animation_has_ended:
            self.current_sprite_index += 1
            self.next_frame += self.interval

    def draw(self, screen):
        screen.blit(self.sprites[self.current_sprite_index], self.sprites_rects[self.current_sprite_index])

    def start_animation(self):
        self.animation_has_started = True
        self.cycles = 0

    def __gen_sprites(self, sprites_list):
        sprites = []
        sprites_rects = []

        for sprite in sprites_list:
            sprite = pygame.transform.scale(sprite, self.size)
            sprite_rect = sprite.get_rect()
            sprite_rect.center = self.location

            sprites_rects.append(sprite_rect)
            sprites.append(sprite)

        return sprites, sprites_rects
    
    def reset(self):
        self.current_sprite_index = 0
        self.cycles = self.anim_duration_cycles
        self.animation_has_ended = False
        self.animation_has_started = False
        self.next_frame = self.interval
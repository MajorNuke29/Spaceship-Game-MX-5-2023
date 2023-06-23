import pygame

from game.components.ui import Heart
from game.utils.constants import SCREEN_WIDTH, FONT_SIZE, WHITE_COLOR
from game.utils import text_utils as txt

class PlayerStats:

    def __init__(self, lifes):
        self.life_sprites, self.is_life_active = self.__gen_heart_sprites(lifes)
        self.len_lifes = len(self.life_sprites)
        self.active_lifes_count = self.len_lifes
        self.score, self.score_rect = self.__gen_score_sprite(0)

    def update (self, lifes, score):
        index = self.len_lifes - lifes - 1

        if index >= 0 and self.is_life_active[index]:
            self.life_sprites[index].start_animation()
            self.is_life_active[index] = False
            self.active_lifes_count -= 1

        if self.active_lifes_count < lifes:
            sprite = self.life_sprites[index+1]
            sprite.reset()
            self.is_life_active[index+1] = True
            self.active_lifes_count = lifes

        for life in self.life_sprites:
            life.update()

        self.score, self.score_rect = self.__gen_score_sprite(score)

    def draw(self, screen):
        for life in self.life_sprites:
            life.draw(screen)
        
        screen.blit(self.score, self.score_rect)

    def set_lifes(self, lifes):
        if self.len_lifes != lifes:
            self.life_sprites, self.is_life_active = self.__gen_heart_sprites(lifes)
            self.len_lifes = len(self.life_sprites)

    def reset(self):
        for life in self.life_sprites:
            life.reset()

        self.active_lifes_count = self.len_lifes
        self.is_life_active = [True for _ in self.life_sprites]
        self.score, self.score_rect = self.__gen_score_sprite(0)

    def __gen_score_sprite(self, score):
        score_text = "SCORE: " + str(score)
        return txt.get_text_surface(score_text, FONT_SIZE, WHITE_COLOR, (30, 30))

    def __gen_heart_sprites(self, lifes):
        hearts = []
        active_hearts = []

        heart_width, heart_height = Heart.HEART_SIZE
        next_x = SCREEN_WIDTH - (heart_width * 3)
        pos_y =  heart_height * 1.5

        for _ in range(lifes):
            hearts.append(Heart((next_x, pos_y)))
            active_hearts.append(True)
            next_x -= (heart_width * 2)

        return hearts, active_hearts
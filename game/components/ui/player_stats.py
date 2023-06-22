import pygame

from game.components.ui import Heart
from game.utils.constants import SCREEN_WIDTH, FONT_SIZE, WHITE_COLOR
from game.utils import text_utils as txt

class PlayerStats:

    def __init__(self, lifes):
        self.life_sprites, self.is_life_active = self.__gen_heart_sprites(lifes)
        self.len_lifes = len(self.life_sprites)
        self.score, self.score_rect = self.__gen_score_sprite(0)

    def update (self, lifes, score):
        index = self.len_lifes - lifes - 1

        if index >= 0 and self.is_life_active[index]:
            self.life_sprites[index].start_animation()
            self.is_life_active[index] = False

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

        self.score, self.score_rect = self.__gen_score_sprite(0)

    def __gen_score_sprite(self, score):
        score_text = "SCORE: " + str(score)
        return txt.get_text_surface(score_text, FONT_SIZE, WHITE_COLOR, (20, 20))

    def __gen_heart_sprites(self, lifes):
        hearts = []
        active_hearts = []

        heart_width, heart_height = Heart.HEART_SIZE
        next_x = SCREEN_WIDTH - (heart_width * 3)
        pos_y =  heart_height 

        for _ in range(lifes):
            hearts.append(Heart((next_x, pos_y)))
            active_hearts.append(True)
            next_x -= (heart_width * 2)

        return hearts, active_hearts
import pygame

from functools import reduce
from game.utils import text_utils as txt
from game.utils.constants import EMPTY_BUTTON, WHITE_COLOR, SCREEN_HEIGHT, SCREEN_WIDTH

class MenuButtons():

    TEXT_SIZE = 30
    BUTTON_MIN_WIDTH = 200

    def __init__(self, buttons_captions: list):
        self.buttons = self.__get_buttons(buttons_captions)

    def update(self, pos):
        pass

    def __get_buttons(self, messages):
        buttons = []
        text_offset = 50

        for message in messages:

            button_text, button_text_rect  = txt.get_text_surface(message, self.TEXT_SIZE, WHITE_COLOR)

            width = button_text_rect.width + text_offset

            button = pygame.transform.scale(EMPTY_BUTTON, (self.BUTTON_MIN_WIDTH if width < self.BUTTON_MIN_WIDTH else width, button_text_rect.height + text_offset))
            button_rect = button.get_rect()

            button.blit(button_text, (button_rect.centerx - (button_text_rect.width // 2) , button_rect.centery - (button_text_rect.height // 2) - 5) )

            buttons.append(button)

        return buttons
    
    def calc_surface(self):
        len_buttons = len(self.buttons)
        space = 25
        button_height = self.buttons[0].get_rect().height

        surf_height = ((space * (len_buttons - 1)) + (len_buttons * button_height))
        surf_widt = reduce(self.buttons, lambda a, b: a if a.get_rect().width > b.get_rect().width else b)

        return surf_widt, surf_height

    def draw(self, screen):
        len_buttons = len(self.buttons)
        button_height = self.buttons[0].get_rect().height
        space = 25
        next_y = (SCREEN_HEIGHT - ((space * (len_buttons - 1)) + (len_buttons * button_height))) // 2

        for button in self.buttons:
            button_rect = button.get_rect()
            pos_x = (SCREEN_WIDTH // 2) - (button_rect.width // 2)

            screen.blit(button, (pos_x, next_y))

            next_y += (space + button_height)


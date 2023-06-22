import pygame

from functools import reduce
from game.utils import text_utils as txt
from game.utils.constants import EMPTY_BUTTON, WHITE_COLOR, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu():

    TEXT_SIZE = 30
    BUTTON_MIN_WIDTH = 200

    def __init__(self, buttons_captions):
        self.buttons, self.hover_buttons = self.__get_buttons(buttons_captions)
        self.hover = False
        self.hover_button_index = 0



import pygame

from game.components.ui import Button

class SymbolButton(Button):

    BUTTON_WIDTH = 60
    BUTTON_HEIGHT = 60

    def __init__(self, image, action, x, y):
        super().__init__(image, action, x, y)
        self.__reescale_button

    def __reescale_button(self):
        self.image = pygame.transform.scale(self.image, (self.BUTTON_WIDTH, self.BUTTON_HEIGHT))
        self.image_hover = pygame.transform.scale_by(self.image, 1.2)

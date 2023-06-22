import pygame

from game.utils import text_utils as txt
from game.utils.constants import WHITE_COLOR, FONT_SIZE

class Button:

    TEXT_PADDING = 50
    BUTTON_MIN_WIDTH = 200
    BUTTON_MIN_HEIGHT = FONT_SIZE + 30

    def __init__(self, image, action, x, y, caption):
        self.image, self.image_hover = self.gen_button(image, caption)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
        self.action = action

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse):
            screen.blit(self.image_hover, self.rect)
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
        else:
            screen.blit(self.image, self.rect)

    def gen_button(self, image, caption):
        button_text, button_text_rect  = txt.get_text_surface(caption, FONT_SIZE, WHITE_COLOR)

        width = button_text_rect.width + self.TEXT_PADDING

        button = pygame.transform.scale(image, (self.BUTTON_MIN_WIDTH if width < self.BUTTON_MIN_WIDTH else width, self.BUTTON_MIN_HEIGHT))
        button_rect = button.get_rect()

        button.blit(button_text, (button_rect.centerx - (button_text_rect.width // 2) , button_rect.centery - (button_text_rect.height // 2) - 5) )
        hover_button = pygame.transform.scale_by(button, 1.2)

        return button, hover_button
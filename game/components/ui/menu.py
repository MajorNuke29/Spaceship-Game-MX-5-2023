from game.components.ui import ButtonList
from game.utils import text_utils as txt
from game.utils.constants import WHITE_COLOR, TITLE_FONT_SIZE, SCREEN_WIDTH

class Menu:
    def __init__(self, title, buttons_captions, buttons_actions, title_location = None, buttons_location = None):
        self.title, self.title_rect = txt.get_text_surface(title, TITLE_FONT_SIZE, WHITE_COLOR, location = title_location if title_location != None else (SCREEN_WIDTH // 2, TITLE_FONT_SIZE))
        self.buttons_actions = buttons_actions
        self.buttons = ButtonList(buttons_captions, buttons_actions, location = buttons_location)
        self.play = False

    def draw(self, screen):
        screen.blit(self.title, self.title_rect)
        self.buttons.draw(screen)
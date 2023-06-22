from game.components.ui import ButtonList
from game.utils import text_utils as txt
from game.utils.constants import WHITE_COLOR, TITLE_FONT_SIZE
class Menu:
    def __init__(self, title, buttons_captions, buttons_actions, title_location = None, buttons_location = None):
        self.title, self.title_rect = txt.get_text_surface(title, TITLE_FONT_SIZE, WHITE_COLOR, location = title_location)
        self.buttons_actions = buttons_actions
        self.buttons = ButtonList(buttons_captions, buttons_actions, location = buttons_location)
        self.play = False

    def draw(self, screen):
        screen.blit(self.title, self.title_rect)
        return self.buttons.draw(screen)
    
    def reset(self):
        self.buttons.reset()
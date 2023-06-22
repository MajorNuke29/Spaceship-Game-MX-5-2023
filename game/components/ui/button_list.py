from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game.components.ui import Button, ButtonFactory

class ButtonList:

    MARGIN = 25

    def __init__(self, buttons_captions, buttons_actions, location = None):
        self.button_factory = ButtonFactory()
        self.location = location
        self.buttons = self.__get_buttons(buttons_captions, buttons_actions)

    def __get_buttons(self, buttons_captions, buttons_actions):
        buttons = []
        len_buttons = len(buttons_captions)
        button_height = Button.BUTTON_MIN_HEIGHT
        button_width = Button.BUTTON_MIN_WIDTH

        if self.location != None:
            pos_x = self.location[0]
            next_y = self.location[1]
        else:
            pos_x = (SCREEN_WIDTH - button_width) // 2
            next_y = (SCREEN_HEIGHT - ((self.MARGIN * (len_buttons - 1)) + (len_buttons * button_height))) // 2

        for index, caption in enumerate(buttons_captions):
            
            button = self.button_factory.get_button(buttons_actions[index], pos_x, next_y, caption = caption)
            buttons.append(button)

            next_y += (self.MARGIN + button_height)
        
        return buttons

    def draw(self, screen):
        for button in self.buttons:
            button.draw(screen)


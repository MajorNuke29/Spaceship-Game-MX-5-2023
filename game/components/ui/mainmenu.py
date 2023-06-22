from game.components.ui import Button
from game.utils.constants import EMPTY_BUTTON, SCREEN_HEIGHT, SCREEN_WIDTH, MENU_PLAY

class MainMenu:
    def __init__(self):
        self.buttons = [Button(EMPTY_BUTTON, MENU_PLAY, caption = "Play"), Button(EMPTY_BUTTON, False, caption = "Controls")]
        self.play = False

    def draw(self, screen):
        len_buttons = len(self.buttons)
        button_height = self.buttons[0].rect.height
        space = 25
        next_y = (SCREEN_HEIGHT - ((space * (len_buttons - 1)) + (len_buttons * button_height))) // 2

        for button in self.buttons:
            button_rect = button.rect
            pos_x = (SCREEN_WIDTH - button_rect.width) // 2

            button.draw(screen, (pos_x, next_y))

            next_y += (space + button_height)

        self.play = self.buttons[0].clicked
from game.components.ui import Button, SymbolButton
from game.utils.constants import EMPTY_BUTTON, BACKWARD_BUTTON

class ButtonFactory:
    def get_button(self, action, x, y, image = None, caption = None):
        button = None

        if caption != None:
            button = Button(EMPTY_BUTTON, action, x, y, caption)
        elif image != None:
            button = SymbolButton(image, action, x, y)
        else:
            button = SymbolButton(BACKWARD_BUTTON, action, x, y)

        return button


from pygame.font import Font
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

def get_message(message, size, color, x = SCREEN_WIDTH//2, y = SCREEN_HEIGHT//2):
    font = Font(FONT_STYLE, size)
    text = font.render(message, True, color)
    text_rect = text.get_rect()
    text_rect.center = (x, y)

    return text, text_rect
from pygame.font import Font
from game.utils.constants import FONT_STYLE, SCREEN_WIDTH

def get_text_surface(message, size, color, location = None):
    font = Font(FONT_STYLE, size)
    text = font.render(message, True, color)
    text_rect = text.get_rect()
    if location != None:
        text_rect.x, text_rect.y = location
    else:
        text_rect.center = (SCREEN_WIDTH//2, size + 20)

    return text, text_rect
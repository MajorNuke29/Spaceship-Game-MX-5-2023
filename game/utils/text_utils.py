from pygame.font import Font
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

def get_text_surface(message, size, color, location = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)):
    font = Font(FONT_STYLE, size)
    text = font.render(message, True, color)
    text_rect = text.get_rect()
    text_rect.x, text_rect.y = location

    return text, text_rect
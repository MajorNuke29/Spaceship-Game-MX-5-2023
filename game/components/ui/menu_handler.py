from game.components.ui import Menu
from game.utils.constants import MENU_PLAY, MENU_TRY_AGAIN, MENU_EXIT, MENU_CHANGE, MENU_OPTION_EASY, MENU_OPTION_MEDIUM, MENU_OPTION_HARD, FONT_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH

class MenuHandler:

    def __init__(self):
        self.main_menu = Menu("SPACESHIP", ["Play", "Controls"], [MENU_PLAY, MENU_CHANGE])
        self.dificult_selection_menu = Menu("SELECT DIFICULTY", ["EASY", "MEDIUM", "HARD"], [MENU_OPTION_EASY, MENU_OPTION_MEDIUM, MENU_OPTION_HARD], title_location = ((SCREEN_WIDTH//4) - 80, (SCREEN_HEIGHT - FONT_SIZE)//2), buttons_location = (700, 190))
        self.game_over_menu = Menu("GAME OVER", ["Try again", "Change dificulty", "End game"], [MENU_TRY_AGAIN, MENU_CHANGE, MENU_EXIT])
        self.current_menu = self.main_menu

    def draw(self, screen):
        action = self.current_menu.draw(screen)

        if action == MENU_PLAY or action == MENU_CHANGE:
            self.current_menu = self.dificult_selection_menu
        if action == MENU_OPTION_EASY or action == MENU_OPTION_MEDIUM or action == MENU_OPTION_HARD:
            self.current_menu = self.game_over_menu

        return action
    
    def reset(self):
        self.dificult_selection_menu.reset()
        self.game_over_menu.reset()

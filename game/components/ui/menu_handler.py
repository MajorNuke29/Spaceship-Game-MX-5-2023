from game.components.ui import Menu
from game.utils.constants import MENU_PLAY, MENU_TRY_AGAIN, MENU_EXIT, MENU_CHANGE, MENU_OPTION_EASY, MENU_OPTION_MEDIUM, MENU_OPTION_HARD

class MenuHandler:



    def __init__(self):
        self.main_menu = Menu("SPACESHIP", ["Play", "Controls"], [MENU_PLAY, MENU_CHANGE])
        self.dificult_selection_menu = Menu("SELECT DIFICULTY", ["EASY", "MEDIUM", "HARD"], [MENU_OPTION_EASY, MENU_OPTION_MEDIUM, MENU_OPTION_HARD])
        self.game_over_menu = Menu("GAME OVER", ["Try again", "End game"], [MENU_TRY_AGAIN, MENU_EXIT])
        self.current_menu = self.main_menu

    def draw(self, screen):
        action = self.current_menu.draw(screen)

        if action == MENU_PLAY:
            self.current_menu = self.dificult_selection_menu
        if action == MENU_OPTION_EASY or action == MENU_OPTION_MEDIUM or action == MENU_OPTION_HARD:
            self.current_menu = self.game_over_menu

        print(action)
        return action
    
    def reset(self):
        self.game_over_menu.reset()

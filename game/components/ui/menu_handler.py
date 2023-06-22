from game.components.ui import Menu, MenuWithGameStats
from game.utils.constants import MENU_PLAY, MENU_TRY_AGAIN, MENU_EXIT, MENU_CHANGE_DIFICULTY, MENU_OPTION_EASY, MENU_OPTION_MEDIUM, MENU_OPTION_HARD, FONT_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH

class MenuHandler:

    def __init__(self):
        self.main_menu = Menu("SPACESHIP", ["Play", "Controls"], [MENU_PLAY, MENU_CHANGE_DIFICULTY])

        self.dificult_selection_menu = Menu("SELECT DIFICULTY", ["EASY", "MEDIUM", "HARD"], [MENU_OPTION_EASY, MENU_OPTION_MEDIUM, MENU_OPTION_HARD], title_location = ((SCREEN_WIDTH//4) - 80, (SCREEN_HEIGHT - FONT_SIZE)//2), buttons_location = (700, 190))

        self.game_over_menu = Menu("GAME OVER", ["Try again", "Change dificulty", "End game"], [MENU_TRY_AGAIN, MENU_CHANGE_DIFICULTY, MENU_EXIT], buttons_location =  (150, 190), title_location = (640, FONT_SIZE + 20))
        self.game_over_menu = MenuWithGameStats(self.game_over_menu, stats_location = (650, 190))

        self.current_menu = self.main_menu

    def update(self, score, max_score, enemies_destroyed, death_count):
        score = "CURRENT SCORE: " + str(score)
        max_score =  "MAX SCORE: " + str(max_score)
        enemies_destroyed = "ENEMIES DESTROYED: " + str(enemies_destroyed)
        death_count = "DEATHS: " + str(death_count)

        self.game_over_menu.update([score, max_score, enemies_destroyed, death_count])

    def draw(self, screen):
        action = self.current_menu.draw(screen)

        if action == MENU_PLAY or action == MENU_CHANGE_DIFICULTY:
            self.current_menu = self.dificult_selection_menu
        if action == MENU_OPTION_EASY or action == MENU_OPTION_MEDIUM or action == MENU_OPTION_HARD:
            self.current_menu = self.game_over_menu

        return action
    
    def reset(self):
        self.dificult_selection_menu.reset()
        self.game_over_menu.reset()

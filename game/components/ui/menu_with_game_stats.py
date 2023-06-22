from game.utils import text_utils as txt
from game.utils.constants import FONT_SIZE, WHITE_COLOR, SCREEN_HEIGHT, SCREEN_WIDTH

class MenuWithGameStats:

    MARGIN = 30

    def __init__(self, menu, stats = ["stat", "stat", "stat"], stats_location = None):
        self.menu = menu
        self.stats_location = stats_location
        self.stats, self.stats_rect = self.__gen_stats_banner(stats)

    def update(self, stats):
        self.stats, self.stats_rect = self.__gen_stats_banner(stats)

    def draw(self, screen):
        action = self.menu.draw(screen)
        
        for index, stat in enumerate(self.stats):
            screen.blit(stat, self.stats_rect[index])
        
        return action
    
    def __gen_stats_banner(self, stats_str):
        stats = []
        stats_rect = []
        len_stats = len(stats_str)

        if self.stats_location != None:
            pos_x, next_y = self.stats_location
        else:
            pos_x = SCREEN_WIDTH//2
            next_y = (SCREEN_HEIGHT - ((self.MARGIN * (len_stats - 1)) + (len_stats * FONT_SIZE))) // 2
            pass

        for stat in stats_str:
            stat_text, stat_rect = txt.get_text_surface(stat, FONT_SIZE, WHITE_COLOR, location = (pos_x, next_y))
            stats.append(stat_text)
            stats_rect.append(stat_rect)

            next_y += (FONT_SIZE + self.MARGIN)

        return stats, stats_rect
    
    def reset(self):
        self.menu.reset()
from game.components.enemies import Enemy
from game.utils.constants import ENEMY_2, FPS, SCREEN_WIDTH, SCREEN_HEIGHT, LEFT, RIGHT, UP, DOWN
import pygame


class Follower(Enemy):

    WIDTH = 40
    HEIGHT = 40
    SPEED_X = 4
    SPEED_Y = 4
    INTERVAL = FPS * 5

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(
            self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
        self.mov_x = LEFT
        self.mov_y = DOWN
        self.moves = 0

    def update(self, player_x, player_y):
        if self.moves < self.INTERVAL:
            self.move(player_x, player_y)
            self.moves += 1
        else:
            self.move_out_bounds()

        if self.is_not_on_screen():
            self.kill()

    def move(self, player_x, player_y):
        self_x = self.rect.x
        self_y = self.rect.y

        if self_x > player_x:
            self.rect.x -= self.SPEED_X
            self.move_x = LEFT
        elif self_x < player_x:
            self.rect.x += self.SPEED_X
            self.move_x = RIGHT

        if self_y > player_y:
            self.rect.y -= self.SPEED_Y
            self.move_y = UP
        elif self_y < player_y:
            self.rect.y += self.SPEED_Y
            self.move_y = DOWN

        # dif_x = self_x - player_x
        # dif_y = self_y - player_y
        # m = None

        # if dif_x != 0:
        #     m = dif_y // dif_x
        # else:
        #     if self_y > player_y:
        #         self.rect.x -= self.SPEED_Y
        #     elif self_y < player_y:
        #         self.rect.x += self.SPEED_Y

        # if m != None:
        #     if m == 0:
        #         pass
        #     elif m > 0:
        #         pass
        #     else:
        #         pass

    def move_out_bounds(self):
        if self.mov_x == RIGHT:
            self.rect.x += (self.SPEED_X + 4)
        elif self.mov_x == LEFT:
            self.rect.x -= (self.SPEED_X + 4)

        if self.move_y == UP:
            self.rect.y -= (self.SPEED_Y + 4)
        elif self.mov_y == DOWN:
            self.rect.y += (self.SPEED_Y + 4)
    
    def is_not_on_screen(self):
        not_on_screen = False

        if self.mov_x == RIGHT and self.mov_y == UP:
            not_on_screen = self.rect.x > SCREEN_WIDTH or self.rect.bottom < 0

        elif self.mov_x == RIGHT and self.mov_y == DOWN:
            not_on_screen = self.rect.x > SCREEN_WIDTH or self.rect.y > SCREEN_HEIGHT

        elif self.mov_x == LEFT and self.mov_y == DOWN:
            not_on_screen = self.rect.right < 0 or self.rect.y > SCREEN_HEIGHT

        elif self.mov_x == LEFT and self.mov_y == UP:
            not_on_screen = self.rect.right < 0 or self.rect.bottom < 0

        return not_on_screen

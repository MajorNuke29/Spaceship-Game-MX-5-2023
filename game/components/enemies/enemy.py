from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, LEFT, RIGHT, UP, DOWN
import random

class Enemy:

    X_POS_LIST = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]
    Y_POS = -50
    SPEED_Y = 5
    SPEED_X = 3
    MOVES_X = [LEFT, RIGHT]
    MOVES_Y = [UP, DOWN]
    INTERVAL = 0

    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.mov_x = random.choice(self.MOVES_X)
        self.is_alive = True

    def update(self):
        self.move()

        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.y += self.SPEED_Y

    def new_x_pos(self):
        self.rect.x = random.choice(self.X_POS_LIST)
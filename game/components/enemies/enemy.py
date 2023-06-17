from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, LEFT, RIGHT
import random

class Enemy:

    X_POS_LIST = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]
    Y_POS = 0
    SPEED_Y = 5
    SPEED_X = 3
    MOV_X = [LEFT, RIGHT]
    INTERVAL = 100

    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.mov_x = random.choice(self.MOV_X)
        self.is_alive = True
        self.index = 0

    def update(self):
        self.move()

    def draw(self, screen):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.y += self.SPEED_Y
        
        if self.mov_x == LEFT:
            self.rect.x -= self.SPEED_X

            if self.index > self.INTERVAL or self.rect.left <= 0:
                self.mov_x = RIGHT
                self.index = 0
        else:
            self.rect.x += self.SPEED_X

            if self.index > self.INTERVAL or self.rect.right >= SCREEN_WIDTH:
                self.mov_x = LEFT
                self.index = 0

        self.index += 1
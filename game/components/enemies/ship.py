from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, SCREEN_HEIGHT, SCREEN_WIDTH, LEFT, RIGHT
import pygame

class Ship(Enemy):

    WIDTH = 35
    HEIGHT = 40
    INTERVAL = 60
    SPEED_X = 6

    def __init__(self):
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
        self.index = 0

    def update(self):
        self.move()
        
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()

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
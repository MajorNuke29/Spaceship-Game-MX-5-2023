import pygame, random

from game.components.enemies import Enemy
from game.utils.constants import ENEMY_2, FPS


class Follower(Enemy):

    WIDTH = 40
    HEIGHT = 40
    SPEED = 7
    INTERVAL = FPS * 5

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(
            self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image,score = 60)
        self.moves = 0
        self.dir_vector = None

    def update(self, player_x, player_y):
        super().update()

        if self.moves < self.INTERVAL:
            self.move(player_x, player_y)
            self.moves += 1
        else:
            self.move_out_bounds()

        if self.is_out_of_screen() and self.has_entered_screen:
            self.is_out_of_bounds = True

    def move(self, player_x, player_y):
        
        dir_vector = pygame.math.Vector2((player_x - self.rect.x), (player_y - self.rect.y))
        
        if dir_vector.length() != 0:
            dir_vector.normalize()
            dir_vector.scale_to_length(self.SPEED)

        self.dir_vector = dir_vector

        self.rect.move_ip(dir_vector)

    def move_out_bounds(self):
        if self.dir_vector.length() == 0:
            values = [-5, 5]
            x = random.choice(values)
            y = random.choice(values)

            dir_vector = pygame.math.Vector2(x , y)
            dir_vector.normalize()
            dir_vector.scale_to_length(self.SPEED)

            self.dir_vector = dir_vector

        self.rect.move_ip(self.dir_vector)

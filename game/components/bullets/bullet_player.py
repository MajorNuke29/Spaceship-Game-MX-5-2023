import pygame

from game.components.bullets import Bullet
from game.utils.constants import BULLET, BULLET_PLAYER_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT

class BulletPlayer(Bullet):

    WIDTH = 20
    HEIGHT = 40
    SPEED = 17

    def __init__(self, origin):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.dir_vect = pygame.math.Vector2((mouse_x - origin[0]), (mouse_y - origin[1]))
        self.dir_vect.scale_to_length(self.SPEED)
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.image = pygame.transform.rotate(self.image, self.__get_rotation_angle(origin))
        self.rect = self.image.get_rect()
        super().__init__(self.image, origin)

    def update(self):
        self.move()

        if self.out_of_bounds():
            self.kill()

    def __get_rotation_angle(self, origin):
        base_vect = pygame.math.Vector2(0, (0 - origin[1]))
        return self.dir_vect.angle_to(base_vect)
    
    def out_of_bounds(self):
        return self.rect.bottom < 0 or self.rect.y > SCREEN_HEIGHT or self.rect.right < 0 or self.rect.x > SCREEN_WIDTH

    def move(self):
        self.rect.move_ip(self.dir_vect)

import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BULLET_PLAYER_TYPE

class SpaceShip:

    WIDTH = 40
    HEIGTH = 60
    X_POS = (SCREEN_WIDTH // 2) - WIDTH
    Y_POS = 500
    BLINK_DURATION_SECS = 2
    BLINK_DURATION_CYCLES = BLINK_DURATION_SECS * FPS
    ALPHA_INTERVAL = (255 // (FPS // 2))
    SPEED = 12

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.lifes = 3
        self.is_blinking = False
        self.is_visible = True
        self.cycles = self.BLINK_DURATION_CYCLES
        self.alpha_value = 255

    def update(self, user_input):
        self.move(user_input)

        if self.is_blinking:
            self.__blink()

        if self.lifes <= 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def kill(self):
        self.is_alive = False

    def reduce_lifes(self):
        self.lifes -= 1

    def __blink(self):
        if self.cycles < self.BLINK_DURATION_CYCLES:
            new_alpha = self.alpha_value - self.ALPHA_INTERVAL

            if new_alpha < 0:
                self.is_visible = False
            
            if self.alpha_value == 255:
                self.is_visible = True

            if self.is_visible:
                self.alpha_value = new_alpha
            else:
                self.alpha_value += self.ALPHA_INTERVAL

            self.image.set_alpha(self.alpha_value)
            self.cycles += 1
        else:
            self.is_blinking = False
            self.is_visible = True
            self.image.set_alpha(255)
            self.alpha_value = 255

    def start_blink(self):
        self.is_blinking = True
        self.cycles = 0

    def shoot(self, bullet_handler):
        bullet_handler.add_bullet(BULLET_PLAYER_TYPE, self.rect.center)


    def move(self, user_input):
        if user_input[pygame.K_LEFT] or user_input[pygame.K_a]:
            self.move_left()

        elif user_input[pygame.K_RIGHT] or user_input[pygame.K_d]:
            self.move_right()

        elif user_input[pygame.K_UP] or user_input[pygame.K_w]:
            self.move_up()

        elif user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
            self.move_down()

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= self.SPEED

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.SPEED

    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= self.SPEED

    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.SPEED

    def reset(self):
        self.is_alive = True
        self.lifes = 3
        self.is_blinking = False
        self.is_visible = True
        self.cycles = self.BLINK_DURATION_CYCLES
        self.alpha_value = 255
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
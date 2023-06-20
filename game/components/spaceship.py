
import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLINK

class SpaceShip:

    WIDTH = 40
    HEIGTH = 60
    X_POS = (SCREEN_WIDTH // 2) - WIDTH
    Y_POS = 500
    BLINK_DURATION_SECS = 2
    BLINK_DURATION_CYCLES = BLINK_DURATION_SECS * FPS

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.is_blinking = False
        self.is_visible = True
        self.cycles = self.BLINK_DURATION_CYCLES
        self.alpha_value = 255

    def update(self, user_input):
        if user_input[pygame.K_LEFT]:
            self.move_left()

        elif user_input[pygame.K_RIGHT]:
            self.move_right()

        elif user_input[pygame.K_UP]:
            self.move_up()

        elif user_input[pygame.K_DOWN]:
            self.move_down()

        if self.is_blinking:
            self.blink()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def kill(self):
        self.is_alive = False

    def blink(self):
        if self.cycles < self.BLINK_DURATION_CYCLES:
            interval = (255 // (FPS // 2))
            new_alpha = self.alpha_value - interval

            if new_alpha < 0:
                self.is_visible = False
            
            if self.alpha_value == 255:
                self.is_visible = True

            if self.is_visible:
                self.alpha_value = new_alpha
            else:
                self.alpha_value += interval

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

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10

    def move_up(self):
        if self.rect.top > (SCREEN_HEIGHT // 2):
            self.rect.y -= 10

    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 10
            
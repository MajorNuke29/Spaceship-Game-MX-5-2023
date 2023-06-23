import pygame

from game.utils.constants import SPACESHIP, SPACESHIP_SHIELD, SHIELD_TYPE, MISILE_TYPE, HEART_TYPE, SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BULLET_PLAYER_TYPE, BULLET_MISILE_TYPE
from game.components.weapon import Weapon

class SpaceShip:

    WIDTH = 40
    HEIGTH = 60
    X_POS = (SCREEN_WIDTH // 2)
    Y_POS = SCREEN_HEIGHT // 2

    BLINK_DURATION_SECS = 2
    BLINK_DURATION_CYCLES = BLINK_DURATION_SECS * FPS

    DELAY_DURATION_SECS = 0.3
    DELAY_DURATION_CYCLES = DELAY_DURATION_SECS * FPS
    
    ALPHA_INTERVAL = (255 // (FPS // 2))
    SPEED = 12

    def __init__(self, lifes = 3):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.X_POS
        self.rect.centery = self.Y_POS
        self.weapon = Weapon(self, self.HEIGTH)
        self.bullet = BULLET_PLAYER_TYPE

        self.is_alive = True
        self.lifes = lifes
        self.default_lifes = lifes
        self.is_blinking = False
        self.is_visible = True
        self.can_shoot = True
        self.is_invincible = False
        self.powerup = None
        
        self.powerup_start = 0
        self.powerup_end = 0
        self.blink_cycles = self.BLINK_DURATION_CYCLES
        self.shoot_delay_cycles = self.DELAY_DURATION_CYCLES
        self.alpha_value = 255


    def add_powerup(self, powerup):
        if powerup.type == SHIELD_TYPE:
            self.change_image(SPACESHIP_SHIELD, (self.WIDTH + 25, self.HEIGTH + 15))
            self.is_invincible =True

        elif powerup.type == MISILE_TYPE:
            self.bullet = BULLET_MISILE_TYPE

        elif powerup.type == HEART_TYPE:
            if self.lifes < self.default_lifes:
                self.lifes += 1
            print(self.lifes)

        self.powerup = powerup
        self.powerup_start = pygame.time.get_ticks()
        self.powerup_end = self.powerup_start + powerup.duration

    def has_powerup(self):
        return self.powerup != None

    def remove_powerup(self):
        if self.powerup.type == SHIELD_TYPE:
            self.change_image(SPACESHIP, (self.WIDTH, self.HEIGTH))
            self.is_invincible = False

        elif self.powerup.type == MISILE_TYPE:
            self.bullet = BULLET_PLAYER_TYPE

        self.powerup = None
        self.powerup_start = 0
        self.powerup_end = 0

    def change_image(self, image, size):
        self.image = pygame.transform.scale(image, size)
        new_rect = self.image.get_rect()
        new_rect.x, new_rect.y = self.rect.x, self.rect.y
        self.rect = new_rect


    def update(self, user_input):
        self.move(user_input)

        if not self.can_shoot:
            self.__shoot_delay()

        if self.is_blinking:
            self.__blink()

        if pygame.time.get_ticks() >= self.powerup_end and self.powerup_end != 0:
            self.remove_powerup()

        if self.lifes <= 0:
            self.kill()



    def set_lifes(self, lifes):
        self.lifes = lifes
        self.default_lifes = lifes



    def __shoot_delay(self):
        if self.shoot_delay_cycles < self.DELAY_DURATION_CYCLES:
            self.shoot_delay_cycles += 1
        else:
            self.can_shoot = True

    def __start_shooting_delay(self):
        self.can_shoot = False
        self.shoot_delay_cycles = 0



    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.weapon.draw(screen)


    def kill(self):
        self.is_alive = False

    def reduce_lifes(self):
        self.lifes -= 1



    def __blink(self):
        if self.blink_cycles < self.BLINK_DURATION_CYCLES:
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
            self.blink_cycles += 1
        else:
            self.is_blinking = False
            self.is_visible = True
            self.image.set_alpha(255)
            self.alpha_value = 255

    def start_blink(self):
        self.is_blinking = True
        self.blink_cycles = 0




    def shoot(self, bullet_handler):
        if self.can_shoot:
            bullet_handler.add_bullet(self.bullet, self.weapon.rect.center)
            self.__start_shooting_delay()




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
        self.lifes = self.default_lifes
        self.is_blinking = False
        self.is_visible = True
        self.blink_cycles = self.BLINK_DURATION_CYCLES
        self.alpha_value = 255
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
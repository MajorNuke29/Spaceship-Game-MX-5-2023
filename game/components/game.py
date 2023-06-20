import pygame
import random

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, SPAWN_ENEMY, ENEMY_SHOOT, BLINK
from game.components.spaceship import SpaceShip
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler


class Game:

    def __init__(self):
        pygame.init()
        pygame.time.set_timer(SPAWN_ENEMY, 700)
        pygame.time.set_timer(ENEMY_SHOOT, 1500)
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = SpaceShip()
        self.enemy_handler = EnemyHandler()
        self.bullet_handler = BulletHandler()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            elif event.type == SPAWN_ENEMY:
                self.enemy_handler.add_enemy()
            elif event.type == ENEMY_SHOOT:
                self.enemy_handler.shoot(self.bullet_handler)

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.enemy_handler.update(self.player)
        self.bullet_handler.update(self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_handler.draw(self.screen, self.player)
        self.bullet_handler.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(
                image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

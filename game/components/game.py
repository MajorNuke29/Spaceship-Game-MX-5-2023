import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, SPAWN_ENEMY, ENEMY_SHOOT, WHITE_COLOR, EASY_LEVEL_ENEMY_SPAWNS, EASY_LEVEL_MAX_ENEMIES

from game.utils import text_utils
from game.components.spaceship import SpaceShip
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.components.enemies.factories import LevelBasedEnemyFactory
from game.components.bullets import BulletFactory
from game.components.menu import MenuButtons


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
        self.runnig = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0

        self.player = SpaceShip()
        self.enemy_handler = EnemyHandler(LevelBasedEnemyFactory(EASY_LEVEL_ENEMY_SPAWNS, EASY_LEVEL_MAX_ENEMIES))
        self.bullet_handler = BulletHandler(BulletFactory())
        self.main_menu = MenuButtons(["Play", "Controls"])
        self.deaths_count = 0
        self.destroyed_enemies = 0

    def run(self):
        # Game loop: events - update - draw
        self.runnig = True

        while self.runnig:
            self.events()
            self.update()
            self.draw()

        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runnig = False
                self.playing = False
            elif event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
            elif event.type == pygame.MOUSEMOTION and not self.playing:
                self.main_menu.update(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.player.shoot(self.bullet_handler)
            elif event.type == SPAWN_ENEMY:
                self.enemy_handler.add_enemy()
            elif event.type == ENEMY_SHOOT:
                self.enemy_handler.shoot(self.bullet_handler)

    def update(self):
        if self.playing:
            if not self.player.is_alive:
                self.playing = False
                self.deaths_count += 1
                self.destroyed_enemies = self.enemy_handler.get_destroyed_enemies_count()
                self.reset()

            user_input = pygame.key.get_pressed()
            self.player.update(user_input)
            self.enemy_handler.update(self.player)
            self.bullet_handler.update(self.player, self.enemy_handler.get_enemies())

    def draw(self):
        if self.playing:
            self.clock.tick(FPS)
            self.draw_background()
            self.player.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.bullet_handler.draw(self.screen)
        else:
            self.main_menu.draw(self.screen)

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

    def draw_menu(self):
        if self.deaths_count == 0:
            text, text_rect = text_utils.get_text_surface("Menu", 30, WHITE_COLOR)
        else:
            text, text_rect = text_utils.get_text_surface("Enemies destroyed: " + str(self.destroyed_enemies), 30, WHITE_COLOR)
        
        self.screen.blit(text, text_rect)

    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
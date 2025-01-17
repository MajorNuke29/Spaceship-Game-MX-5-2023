import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, SPAWN_ENEMY, ENEMY_SHOOT, EASY_LEVEL_ENEMY_SPAWNS, EASY_LEVEL_MAX_ENEMIES, MEDIUM_LEVEL_ENEMY_SPAWNS, MEDIUM_LEVEL_MAX_ENEMIES, HARD_LEVEL_ENEMY_SPAWNS, HARD_LEVEL_MAX_ENEMIES, MENU_TRY_AGAIN, MENU_EXIT, MENU_CHANGE_DIFICULTY, MENU_OPTION_EASY, MENU_OPTION_MEDIUM, MENU_OPTION_HARD, EASY_LEVEL_LIFES, MEDIUM_LEVEL_LIFES, HARD_LEVEL_LIFES, EASY_LEVEL_DROPS, MEDIUM_LEVEL_DROPS, HARD_LEVEL_DROPS

from game.components.spaceship import SpaceShip
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.components.enemies.factories import LevelBasedEnemyFactory
from game.components.bullets import BulletFactory
from game.components.ui import MenuHandler, PlayerStats
from game.components.powerups import PoweUpHandler, PowerupFactory
from game.components import ExplosionHandler, ExplosionFactory

class Game:

    def __init__(self):
        pygame.init()
        pygame.time.set_timer(SPAWN_ENEMY, 600)
        pygame.time.set_timer(ENEMY_SHOOT, 1200)
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
        self.player_stats = PlayerStats(self.player.lifes)
        self.enemy_handler = None
        self.power_up_handler = None
        self.bullet_handler = BulletHandler(BulletFactory())
        self.menu_handler = MenuHandler()
        self.explosion_handler = ExplosionHandler(ExplosionFactory())
        self.deaths_count = 0
        self.destroyed_enemies = 0
        self.score = 0
        self.max_score = 0

    def run(self):
        # Game loop: events - update - draw
        self.runnig = True
        pygame.event.set_grab(True)

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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.runnig = False
                    self.playing = False
            elif event.type == pygame.MOUSEBUTTONDOWN and self.playing:
                if event.button == 1:
                    self.player.shoot(self.bullet_handler)
            elif event.type == SPAWN_ENEMY and self.playing:
                self.enemy_handler.add_enemy()
            elif event.type == ENEMY_SHOOT and self.playing:
                self.enemy_handler.shoot(self.bullet_handler)

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(user_input)

            if not self.player.is_alive:
                self.playing = False
                self.deaths_count += 1
                self.destroyed_enemies = self.enemy_handler.get_destroyed_enemies_count()
                self.score = self.enemy_handler.get_current_score()

                if self.max_score < self.score:
                    self.max_score = self.score

                self.menu_handler.update(self.score, self.max_score, self.destroyed_enemies, self.deaths_count)

            self.player_stats.update(self.player.lifes, self.enemy_handler.get_current_score())
            self.power_up_handler.update(self.player)
            self.enemy_handler.update(self.player)
            self.explosion_handler.update(self.enemy_handler.get_enemies())
            self.bullet_handler.update(self.player, self.enemy_handler.get_enemies(), self.power_up_handler, self.explosion_handler)

    def draw(self):
        self.clock.tick(FPS)
        self.draw_background()

        if self.playing:
            self.player.draw(self.screen)
            self.player_stats.draw(self.screen)
            self.power_up_handler.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.explosion_handler.draw(self.screen)
        else:
            self.menu_actions()

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

    def menu_actions(self):
        action = self.menu_handler.draw(self.screen)

        if action == MENU_OPTION_EASY:
            self.enemy_handler = EnemyHandler(LevelBasedEnemyFactory(EASY_LEVEL_ENEMY_SPAWNS, EASY_LEVEL_MAX_ENEMIES))
            self.power_up_handler = PoweUpHandler(PowerupFactory(EASY_LEVEL_DROPS))
            self.player.set_lifes(EASY_LEVEL_LIFES)
            self.player_stats.set_lifes(EASY_LEVEL_LIFES)
            self.playing = True
        elif action == MENU_OPTION_MEDIUM:
            self.enemy_handler = EnemyHandler(LevelBasedEnemyFactory(MEDIUM_LEVEL_ENEMY_SPAWNS, MEDIUM_LEVEL_MAX_ENEMIES))
            self.power_up_handler = PoweUpHandler(PowerupFactory(MEDIUM_LEVEL_DROPS))
            self.player.set_lifes(MEDIUM_LEVEL_LIFES)
            self.player_stats.set_lifes(MEDIUM_LEVEL_LIFES)
            self.playing = True
        elif action == MENU_OPTION_HARD:
            self.enemy_handler = EnemyHandler(LevelBasedEnemyFactory(HARD_LEVEL_ENEMY_SPAWNS, HARD_LEVEL_MAX_ENEMIES))
            self.power_up_handler = PoweUpHandler(PowerupFactory(HARD_LEVEL_DROPS))
            self.player.set_lifes(HARD_LEVEL_LIFES)
            self.player_stats.set_lifes(HARD_LEVEL_LIFES)
            self.playing = True
        elif action == MENU_TRY_AGAIN:
            self.reset()
            self.playing = True
        elif action == MENU_CHANGE_DIFICULTY:
            self.reset()
            self.playing = False
        elif action == MENU_EXIT:
            self.playing = False
            self.runnig = False

    def reset(self):
        self.player.reset()
        self.player_stats.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.power_up_handler.reset()
        self.explosion_handler.reset()
        self.menu_handler.reset()
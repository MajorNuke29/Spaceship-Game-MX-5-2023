import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
SPACESHIP_WEAPON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_weapon.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

FONT_STYLE = os.path.join(IMG_DIR, 'Other/Rodchenkocondc.otf')
FONT_SIZE = 30
TITLE_FONT_SIZE = 60

# UI constants
EMPTY_BUTTON = pygame.image.load(os.path.join(IMG_DIR, "Other/Buttons/empty_button.png"))
BACKWARD_BUTTON = pygame.image.load(os.path.join(IMG_DIR, "Other/Buttons/backward_button.png"))
REPLAY_BUTTON = pygame.image.load(os.path.join(IMG_DIR, "Other/Buttons/replay_button.png"))

# Movement constants
LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'

# Enemies constants
ENEMY_SHIP_TYPE = 'ship'
ENEMY_DRONE_TYPE = 'drone'
ENEMY_FOLLOWER_TYPE = 'follower'
ENEMIES_TYPES = [ENEMY_SHIP_TYPE, ENEMY_DRONE_TYPE, ENEMY_FOLLOWER_TYPE]

EASY_LEVEL_MAX_ENEMIES = 4
MEDIUM_LEVEL_MAX_ENEMIES = 6
HARD_LEVEL_MAX_ENEMIES = 8

EASY_LEVEL_ENEMY_SPAWNS = [3, 1, 0]
MEDIUM_LEVEL_ENEMY_SPAWNS = [2, 3, 1]
HARD_LEVEL_ENEMY_SPAWNS = [1, 2, 2]

# Bullet constants
BULLET_ENEMY_TYPE = 'enemy'
BULLET_PLAYER_TYPE = 'player'
BULLET_PLAYER_SPEED = 15

# Custom events
SPAWN_ENEMY = pygame.USEREVENT + 1
# ENEMY_SHIP_SHOOT = pygame.USEREVENT + 2
# ENEMY_DRONE_SHOOT = pygame.USEREVENT + 3
# ENEMY_FOLLOWER_SHOOT = pygame.USEREVENT + 4
ENEMY_SHOOT = pygame.USEREVENT + 5

MENU_EXIT = 'exit'
MENU_TRY_AGAIN = 'return'
MENU_PLAY = 'play'
MENU_CHANGE = 'change'
MENU_OPTION_EASY = 'easy'
MENU_OPTION_MEDIUM = 'medium'
MENU_OPTION_HARD = 'hard'

# Color
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255 ,255)
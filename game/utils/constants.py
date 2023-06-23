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
MISILE_TYPE = 'misile'
HEART_TYPE = 'heart'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
SPACESHIP_WEAPON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_weapon.png"))
MISILE = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

HEART_SPRITES = [pygame.image.load(os.path.join(IMG_DIR, 'Other/Heart/Heart.png')),
                 pygame.image.load(os.path.join(IMG_DIR, 'Other/Heart/Heart_1.png')),
                 pygame.image.load(os.path.join(IMG_DIR, 'Other/Heart/Heart_2.png')),
                 pygame.image.load(os.path.join(IMG_DIR, 'Other/Heart/Heart_3.png')),
                 pygame.image.load(os.path.join(IMG_DIR, 'Other/Heart/Heart_4.png'))]

EXPLOSION_1_SPRITES = [pygame.image.load(os.path.join(IMG_DIR, 'Explosions/Explosion_1/explosion1 (2).png')),
                       pygame.image.load(os.path.join(IMG_DIR, 'Explosions/Explosion_1/explosion1 (3).png')),
                       pygame.image.load(os.path.join(IMG_DIR, 'Explosions/Explosion_1/explosion1 (4).png')),
                       pygame.image.load(os.path.join(IMG_DIR, 'Explosions/Explosion_1/explosion1 (5).png')),
                       pygame.image.load(os.path.join(IMG_DIR, 'Explosions/Explosion_1/explosion1 (6).png')),
                       pygame.image.load(os.path.join(IMG_DIR, 'Explosions/Explosion_1/explosion1 (7).png')),
                       pygame.image.load(os.path.join(IMG_DIR, 'Explosions/Explosion_1/explosion1 (8).png')),
                       pygame.image.load(os.path.join(IMG_DIR, 'Explosions/Explosion_1/explosion1 (9).png')),
                       pygame.image.load(os.path.join(IMG_DIR, 'Explosions/Explosion_1/explosion1 (10).png')),
                       pygame.image.load(os.path.join(IMG_DIR, 'Explosions/Explosion_1/explosion1 (11).png')),]

EXPLOSION_2_SPRITES = [pygame.image.load(os.path.join(IMG_DIR, 'Explosions/Explosion_2/explosion2 (2).png')),
                       pygame.image.load(os.path.join(IMG_DIR, 'Explosions/Explosion_2/explosion2 (3).png')),
                       pygame.image.load(os.path.join(IMG_DIR, 'Explosions/Explosion_2/explosion2 (4).png')),
                       pygame.image.load(os.path.join(IMG_DIR, 'Explosions/Explosion_2/explosion2 (5).png')),
                       pygame.image.load(os.path.join(IMG_DIR, 'Explosions/Explosion_2/explosion2 (6).png')),
                       pygame.image.load(os.path.join(IMG_DIR, 'Explosions/Explosion_2/explosion2 (7).png')),
                       pygame.image.load(os.path.join(IMG_DIR, 'Explosions/Explosion_2/explosion2 (8).png')),
                       pygame.image.load(os.path.join(IMG_DIR, 'Explosions/Explosion_2/explosion2 (9).png')),
                       pygame.image.load(os.path.join(IMG_DIR, 'Explosions/Explosion_2/explosion2 (10).png')),
                       pygame.image.load(os.path.join(IMG_DIR, 'Explosions/Explosion_2/explosion2 (11).png')),]

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

EASY_LEVEL_LIFES = 6
MEDIUM_LEVEL_LIFES = 5
HARD_LEVEL_LIFES = 4

EASY_LEVEL_ENEMY_SPAWNS = [3, 1, 0]
MEDIUM_LEVEL_ENEMY_SPAWNS = [2, 3, 1]
HARD_LEVEL_ENEMY_SPAWNS = [1, 2, 2]

# Bullet constants
BULLET_ENEMY_TYPE = 'enemy'
BULLET_PLAYER_TYPE = 'player'
BULLET_PLAYER_SPEED = 15

# Drop constants
EASY_LEVEL_DROPS = [1,1,0,2]
MEDIUM_LEVEL_DROPS = [1,1,1,3]
HARD_LEVEL_DROPS = [0,1,1,3]

# Custom events
SPAWN_ENEMY = pygame.USEREVENT + 1
ENEMY_SHOOT = pygame.USEREVENT + 5

MENU_EXIT = 'exit'
MENU_TRY_AGAIN = 'return'
MENU_PLAY = 'play'
MENU_CHANGE_DIFICULTY = 'change'
MENU_OPTION_EASY = 'easy'
MENU_OPTION_MEDIUM = 'medium'
MENU_OPTION_HARD = 'hard'

# Color
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255 ,255)
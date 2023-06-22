import pygame

from game.utils.constants import SPACESHIP_WEAPON

class Weapon(pygame.sprite.Sprite):

    WIDTH = 15
    HEIGHT = 15

    def __init__(self, player, radius):
        super().__init__()
        self.player = player
        self.radius = radius
        self.image = SPACESHIP_WEAPON
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.player.rect.centerx - (self.WIDTH // 2)
        self.rect.centery = self.player.rect.centery - (radius + (self.HEIGHT // 2))

    def update(self):
        pass

    def draw(self, screen):
        player_weapon_vector = pygame.math.Vector2((self.rect.centerx - self.player.rect.centerx), (self.rect.centery - self.player.rect.centery))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        weapon_mouse_vector = pygame.math.Vector2((mouse_x - self.player.rect.centerx), (mouse_y - self.player.rect.centery))

        rotation = player_weapon_vector.angle_to(weapon_mouse_vector)
        player_weapon_vector.rotate_ip(rotation)

        print(player_weapon_vector.xy)
        
        screen.blit(self.image, self.rect.center)
        pygame.draw.line(screen, (255, 14, 14), self.player.rect.center, (self.player.rect.centerx + player_weapon_vector.x, self.player.rect.centery + player_weapon_vector.y))
        pygame.draw.line(screen, (0, 255, 0), self.player.rect.center, (self.player.rect.centerx + weapon_mouse_vector.x, self.player.rect.centery + weapon_mouse_vector.y))

    def move(self):
        self.rect.centerx = self.player.rect.centerx - (self.WIDTH // 2)
        self.rect.centery = self.player.rect.centery - (self.radius + (self.HEIGHT // 2))

    def move_evt(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        player_weapon_vector = pygame.math.Vector2((self.rect.centerx - self.player.rect.centerx), (self.rect.centery - self.player.rect.centery))
        player_mouse_vector = pygame.math.Vector2((mouse_x - self.player.rect.centerx), (mouse_y - self.player.rect.centery))

        rotation = player_weapon_vector.angle_to(player_mouse_vector)
        player_weapon_vector.rotate_ip(rotation)

        print(player_weapon_vector)

        # self.rect.move_ip()
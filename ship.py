import pygame
from pygame.sprite import Sprite
from Index import Index


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        ims = Index()
        self.images = ims.s1
        self.explode = ims.E1

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.timer = pygame.time.get_ticks()
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.death_index = None
        self.last_frame = None

        self.dieing = False
        self.dead = False

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def death(self):
        self.dead = True
        self.death_index = 0
        self.image = self.explode[self.death_index]
        self.last_frame = pygame.time.get_ticks()

    def update(self):
        # Update the ship's center value, not the rect.
            if not self.dieing:
                if pygame.time.get_ticks() - self.timer >= 360:
                    self.index += 1
                    if self.index >= len(self.images):
                        self.index = 0
                    self.image = self.images[self.index]
                    self.timer = pygame.time.get_ticks()

                if self.moving_right and self.rect.right < self.screen_rect.right:
                    self.center += self.ai_settings.ship_speed_factor
                if self.moving_left and self.rect.left > 0:
                    self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
                self.rect.centerx = self.center
            else:
                if pygame.time.get_ticks() - self.timer >= 100:   # At least 20 millisecond delay between frames
                    self.death_index += 1
                    if self.death_index >= len(self.explode):
                        self.dieing = False
                    else:
                        self.image = self.explode[self.death_index]
                        self.timer = pygame.time.get_ticks()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

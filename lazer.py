
import pygame
from Index import Index


class Lazer(pygame.sprite.Sprite):
    def __init__(self, ai_settings, screen, alien):
        super(Lazer, self).__init__()
        self.screen = screen

        ims = Index()
        self.images = ims.L1

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom
        self.timer = pygame.time.get_ticks()
        self.y = float(self.rect.y)
        self.speed_factor = ai_settings.lazer_speed

    def update(self):
        self.y += self.speed_factor
        self.rect.y = self.y

        if pygame.time.get_ticks() - self.timer >= 180:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            self.timer = pygame.time.get_ticks()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

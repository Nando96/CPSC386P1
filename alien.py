import pygame
from pygame.sprite import Sprite
from Index import index

def load_image(name):
    image = pygame.image.load(name)
    return image

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.Dead = False
        self.screen = screen
        self.ai_settings = ai_settings
        self.type = 0

        # Load the alien image, and set its rect attribute.
        Ims = index()
        self.images = Ims.a1

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.image = self.images[self.index]
        self.Explode = index().E1
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def start_death(self):
        self.Dead = True

    def death(self):
        self.image = self.Explode[0]
        if pygame.time.get_ticks() - self.timer >= 100:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.Explode[self.index]
            self.rect.x = self.x
            self.timer = pygame.time.get_ticks()

    def update(self):
        if not self.Dead:
            if pygame.time.get_ticks() - self.timer >= 360:
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]
                self.rect.x = self.x
                self.timer = pygame.time.get_ticks()

        if self.Dead:
            self.death()

        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)


class Aone(Alien):
    def __init__(self, ai_settings, screen):
        Alien.__init__(self, ai_settings, screen)
        self.type = 1
        self.screen = screen
        self.ai_settings = ai_settings
        self.value = 10
        Ims = index()
        self.images = Ims.a1

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.timer = pygame.time.get_ticks()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

class Atwo(Alien):
    def __init__(self, ai_settings, screen):
        Alien.__init__(self, ai_settings, screen)
        self.type = 2
        self.screen = screen
        self.ai_settings = ai_settings
        self.value = 20
        Ims = index()
        self.images = Ims.a2

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.timer = pygame.time.get_ticks()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

class Athree(Alien):
    def __init__(self, ai_settings, screen):
        Alien.__init__(self, ai_settings, screen)
        self.type = 3
        self.screen = screen
        self.ai_settings = ai_settings
        self.value = 40
        # Load the alien image, and set its rect attribute.
        Ims = index()
        self.images = Ims.a3

        self.index = 0
        self.image = self.images[self.index]

        self.rect = self.image.get_rect()
        self.timer = pygame.time.get_ticks()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

class Mother(Alien):
    def __init__(self, ai_settings, screen):
        Alien.__init__(self, ai_settings, screen)
        self.type = 4
        self.screen = screen
        self.ai_settings = ai_settings
        self.on = False
        # Load the alien image, and set its rect attribute.
        Ims = index()
        self.images = Ims.a4

        self.index = 0
        self.image = self.images[self.index]

        self.rect = self.image.get_rect()
        self.timer = pygame.time.get_ticks()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)
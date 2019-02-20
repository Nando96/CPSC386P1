import sys
import pygame
import pygame.font
from button import Button
from Index import index

from pygame.sprite import Group

from settings import Settings


class StartScreen():

    def __init__(self, theSettings, screen, button):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.theSettings = Settings


        self.image = index().a1[0]
        self.image2 = index().a2[0]
        self.image3 = index().a3[0]
        self.rect = self.image.get_rect()

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        screen = pygame.display.set_mode((theSettings.screen_width, theSettings.screen_height))
        screen.fill(theSettings.bg_color)

    def makeScreen(self, theSettings, screen):
        pygame.init()
        screen = pygame.display.set_mode((theSettings.screen_width, theSettings.screen_height))
        pygame.display.set_caption("Space Invaders")


        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill(theSettings.bg_color)

        # Display Space text
        font = pygame.font.Font(None, 144)
        text1 = font.render("Space", 2, (255, 255, 255))
        textpos1 = text1.get_rect()
        textpos1.centerx = background.get_rect().centerx
        font = pygame.font.Font(None, 144)

        # Display Invaders text
        text2 = font.render("Invaders", 2, (0, 255, 0))
        textpos2 = text2.get_rect()
        textpos2 = ((theSettings.screen_width / 2) - 200, theSettings.screen_height / 6)


        # Alien position and text
        font = pygame.font.Font(None, 44)
        text3 = font.render(" = 20 pts", 2, (250, 250, 250))
        textpos3 = text3.get_rect()

        text4 = font.render(" = 40 pts", 2, (250, 250, 250))
        textpos4 = text4.get_rect()

        text5 = font.render(" = 10 pts", 2, (250, 250, 250))
        textpos5 = text5.get_rect()

        # top alien
        textpos5 = ((theSettings.screen_width / 2) - 50, (theSettings.screen_height / 2) - 40)
        alienpos3 = ((theSettings.screen_width / 2) - 100, (theSettings.screen_height / 2) - 50)

        # middle alien
        textpos3 = ((theSettings.screen_width / 2) - 50, (theSettings.screen_height / 2) + 10)
        alienpos1 = ((theSettings.screen_width / 2) - 100, theSettings.screen_height / 2)

        # bottom alien
        textpos4 = ((theSettings.screen_width / 2) - 50, (theSettings.screen_height / 2) + 50)
        alienpos2 = ((theSettings.screen_width / 2) - 100, (theSettings.screen_height / 2) + 50)

        # Draw onto screen
        background.blit(text1, textpos1)
        background.blit(text2, textpos2)
        background.blit(self.image, alienpos1)
        background.blit(text3, textpos3)
        background.blit(self.image2, alienpos2)
        background.blit(text4, textpos4)
        background.blit(self.image3, alienpos3)
        background.blit(text5, textpos5)

        # Blit everything to screen
        screen.blit(self.image, (theSettings.screen_width / 2, theSettings.screen_height / 3))
        screen.blit(background, (200, 200))


        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    return

            screen.blit(background, (0, 0))
            pygame.display.flip()

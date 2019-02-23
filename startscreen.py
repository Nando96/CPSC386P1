import pygame
import pygame.font
from Index import Index
from settings import Settings
class StartScreen:

    def __init__(self, settings, screen, button):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.theSettings = Settings

        self.image = Index().a1[0]
        self.image2 = Index().a2[0]
        self.image3 = Index().a3[0]
        self.rect = self.image.get_rect()

        self.text_color = (0, 255, 0)
        self.font = pygame.font.SysFont(None, 48)
        screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        screen.fill(settings.bg_color)

    def makescreen(self, settings):
        pygame.init()
        screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        pygame.display.set_caption("Space Invaders")

        background = pygame.Surface(screen.get_size())
        background.fill(settings.bg_color)
        font = pygame.font.Font(None, 144)
        text1 = font.render("Space", 2, (0, 255, 0))
        textpos1 = text1.get_rect()
        textpos1.centerx = background.get_rect().centerx
        font = pygame.font.Font(None, 144)

        # Display Invaders text
        text2 = font.render("Invaders", 2, (0, 255, 0))
        textpos2 = ((settings.screen_width / 2) - 200, settings.screen_height / 6)

        font = pygame.font.Font(None, 44)
        text3 = font.render(" = 20 pts", 2, (250, 250, 250))

        text4 = font.render(" = 40 pts", 2, (250, 250, 250))

        text5 = font.render(" = 10 pts", 2, (250, 250, 250))

        text6 = font.render("Play", 2, (250, 250, 250))

        text7 = font.render("High Score", 2, (250, 250, 250))

        textpos5 = ((settings.screen_width / 2) - 50, (settings.screen_height / 2) - 40)
        alienpos3 = ((settings.screen_width / 2) - 100, (settings.screen_height / 2) - 50)

        # middle alien
        textpos3 = ((settings.screen_width / 2) - 50, (settings.screen_height / 2) + 10)
        alienpos1 = ((settings.screen_width / 2) - 100, settings.screen_height / 2)

        # bottom alien
        textpos4 = ((settings.screen_width / 2) - 50, (settings.screen_height / 2) + 50)
        alienpos2 = ((settings.screen_width / 2) - 100, (settings.screen_height / 2) + 50)

        textpos6 = ((settings.screen_width / 2) - 50, (settings.screen_height / 2) + 100)

        textpos7 = ((settings.screen_width / 2) - 50, (settings.screen_height / 2) + 150)

        # Draw onto screen
        background.blit(text1, textpos1)
        background.blit(text2, textpos2)
        background.blit(self.image2, alienpos1)
        background.blit(text3, textpos3)
        background.blit(self.image3, alienpos2)
        background.blit(text4, textpos4)
        background.blit(self.image, alienpos3)
        background.blit(text5, textpos5)
        background.blit(text6, textpos6)
        background.blit(text7, textpos7)
        screen.blit(self.image, (settings.screen_width / 2, settings.screen_height / 3))
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

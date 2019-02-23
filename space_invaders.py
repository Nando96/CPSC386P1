import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from bunker import make_bunker
from ship import Ship
from startscreen import StartScreen
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space Invaders")
    pygame.mixer.music.load("sounds/loop.mp3")
    play_button = Button(ai_settings, screen, "Play")
    start_screen = StartScreen(ai_settings, screen, play_button)
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    start_screen.makescreen(ai_settings)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    lazers = Group()
    aliens = Group()
    bunkers = pygame.sprite.Group(make_bunker(ai_settings, screen, 0), make_bunker(ai_settings, screen, 1),
                                  make_bunker(ai_settings, screen, 2), make_bunker(ai_settings, screen, 3))
    gf.create_fleet(ai_settings, screen, aliens)
    pygame.mixer.music.play(-1, 0.0)
    # Start the main loop for the game.
    gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, lazers, play_button, bunkers)
    while True:
        pygame.time.delay(15)
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, aliens, bullets)
            gf.update_bullets_lazers(ai_settings, lazers, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, lazers)
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, lazers, play_button, bunkers)


run_game()

import sys
from time import sleep

import pygame
import random
from bullet import Bullet
from alien import Aone, Atwo, Athree
from lazer import Lazer


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,
                 bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button,
                              ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship,
                      aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.check_button(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, aliens)
        ship.center_ship()


def fire_bullet(ai_settings, screen, ship, bullets):
    sound1 = pygame.mixer.Sound("sounds/fire.wav")

    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship, yoffset=0 * ship.rect.height)
        sound1.play()
        bullets.add(new_bullet)
    bullets.update()


def fire_alien(ai_settings, screen, aliens, lazers):
    firing_alien = random.choice(aliens.sprites())
    if len(lazers) < ai_settings.lazer_ok and \
            (ai_settings.beam_stamp is None or
             (abs(pygame.time.get_ticks() - ai_settings.beam_stamp) > ai_settings.beam_time)):
        new_lazer = Lazer(ai_settings, screen, firing_alien)

        lazers.add(new_lazer)


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, lazers, play_button, bunkers):
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    aliens.draw(screen)

    for lazor in lazers.sprites():
        lazor.blitme()

    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    bunkers.update()
    check_bunker_collisions(lazers, bullets, bunkers)

    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, aliens, bullets)


def update_bullets_lazers(ai_settings, lazers, bullets):
    bullets.update()
    lazers.update()
    # Remove bullets that are out of view
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    for lazor in lazers.copy():
        if lazor.rect.bottom > ai_settings.screen_height:
            lazers.remove(lazor)


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def check_bunker_collisions(lazers, bullets, bunkers):
    collisions = pygame.sprite.groupcollide(bullets, bunkers, True, False)
    for b_list in collisions.values():
        for block in b_list:
            block.damage(top=False)
    collisions = pygame.sprite.groupcollide(lazers, bunkers, True, False)
    for b_list in collisions.values():
        for block in b_list:
            block.damage(top=True)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, False)

    if collisions:
        for aliens in collisions.values():
            for killed in aliens:

                stats.score += killed.value
                killed.begin_death()
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, aliens)


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, lazers):
    ship.death()
    ship.update()

    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    aliens.empty()
    bullets.empty()
    lazers.empty()
    create_fleet(ai_settings, screen, aliens)
    ship.center_ship()
    sleep(1)


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets, lazers):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, lazers)
            break


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, lazers):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, lazers)
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets, lazers)
    if aliens.sprites():
        fire_alien(ai_settings, screen, aliens, lazers)
    if pygame.sprite.spritecollideany(ship, lazers):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, lazers)


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(alien_type, ai_settings, screen, aliens, alien_number, row_number):
    
    if alien_type == 1:
        alien = Aone(ai_settings, screen)
    elif alien_type == 2:
        alien = Atwo(ai_settings, screen)
    else:
        alien = Athree(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens):

    alien = Athree(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)

    number_rows = 6

    for row_number in range(number_rows):
        if row_number == 0 or row_number == 1:
            a_num = 1
        elif row_number == 2 or row_number == 3:
            a_num = 2
        else:
            a_num = 3
        for alien_number in range(number_aliens_x):

            create_alien(a_num, ai_settings, screen, aliens, alien_number,
                         row_number)

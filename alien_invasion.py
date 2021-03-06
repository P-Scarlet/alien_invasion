import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Инициализация игры и создание объекта "экран".
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Создание корабля.
    ship = Ship(ai_settings, screen)
    # Объединение пуль в группу.
    bullets = Group()

    # Начало основного алгоритма игры.
    while True:

        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()

        bullets.update()

        gf.update_screen(ai_settings, screen, ship, bullets)

    

run_game()

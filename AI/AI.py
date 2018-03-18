# -*- coding:utf-8 -*-
import pygame
from setting import Setting
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode(
        (ai_setting.screen_wide, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    while True:
        gf.check_event(ship)
        gf.update_screen(ai_setting, screen, ship)


run_game()


# -*- coding:utf-8 -*-
import pygame
import sys
# from ship import Ship


def check_event(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 1


def update_screen(ai_setting, screen, ship):
    # 更新屏幕数据
    screen.fill(ai_setting.bg_color)
    ship.bliteme()
    pygame.display.flip()

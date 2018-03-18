# -*- coding:utf-8 -*-
import pygame


class Ship():
    """control the ships in AI games"""

    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('images/ship1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.move_right = False
        self.move_left = False

    def bliteme(self):
        self.screen.blit(self.image, self.rect)

    def ship_motion_update(self):
        if self.move_right:
            self.rect.centerx += 1
        elif self.move_left:
            self.rect.centerx -= 1


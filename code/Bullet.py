
#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Entity import Entity


class Bullet(Entity):

    def __init__(self, x, y):
        super().__init__()

        self.name = "Bullet"
        self.speed = 8

        self.surf = pygame.Surface((14, 4))
        self.surf.fill((0, 255, 255))

        self.rect = self.surf.get_rect()
        self.rect.left = x
        self.rect.centery = y

    def move(self):
        self.rect.x += self.speed


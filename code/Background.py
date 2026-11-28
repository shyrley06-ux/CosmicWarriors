#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Entity import Entity


class Background(Entity):

    def __init__(self, window):
        super().__init__()
        self.window = window

        self.surf = pygame.image.load(
            "assets/images/Purple_Nebula_07-512x512.png"
        ).convert()
        self.surf = pygame.transform.scale(
            self.surf, (800, 600)
        )
        self.rect = self.surf.get_rect()

    def move(self):
        pass
    def draw(self):
        self.window.blit(self.surf, self.rect)




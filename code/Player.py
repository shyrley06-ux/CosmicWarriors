
#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.PlayShot import PlayShot
from code.Entity import Entity


class Player(Entity):

    def __init__(self, window):
        super().__init__()

        self.name = "Player"
        self.window = window
        self.speed = 3

        self.bullets = []

        self.surf = pygame.image.load(
            "assets/images/Nave roxa futurista.png"
        ).convert_alpha()

        self.surf = pygame.transform.scale(
            self.surf, (70, 70)
        )
        self.surf = pygame.transform.rotate(
            self.surf, -90
        )


        self.rect = self.surf.get_rect()
        self.rect.left = 20
        self.rect.bottom = window.get_height() - 400

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        self.rect.clamp_ip(self.window.get_rect())

        self.rect.clamp_ip(self.window.get_rect())

    def shoot(self):
        shot = PlayShot(
            self.rect.right,
            self.rect.centery
        )
        self.bullets.append(shot)



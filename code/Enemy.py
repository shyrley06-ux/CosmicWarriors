
#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Entity import Entity
from code.EnemyShot import EnemyShot


class Enemy(Entity):

    def __init__(self, window):
        super().__init__()
        self.shots = []

        self.name = "Enemy"
        self.window = window
        self.speed = 0
        self.health = 100

        self.surf = pygame.image.load(
            "assets/images/Enemy3.png"
        ).convert_alpha()

        self.surf = pygame.transform.scale(
            self.surf, (80, 50)
        )

        self.rect = self.surf.get_rect()

    def move(self):
        pass

    def shoot(self):
        shot = EnemyShot(
            self.rect.left,
            self.rect.centery
        )
        self.shots.append(shot)





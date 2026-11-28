
#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Entity import Entity


class EnemyShot(Entity):

    def __init__(self, x, y):
        super().__init__()

        self.name = "EnemyShot"
        self.speed = 5

        # Superfície transparente para o efeito visual
        self.surf = pygame.Surface(
            (26, 12),
            pygame.SRCALPHA
        )

        # Brilho externo
        pygame.draw.ellipse(
            self.surf,
            (255, 50, 20, 100),
            (0, 0, 26, 12)
        )

        # Corpo do projétil
        pygame.draw.ellipse(
            self.surf,
            (255, 65, 25),
            (3, 2, 20, 8)
        )

        # Núcleo brilhante
        pygame.draw.ellipse(
            self.surf,
            (255, 230, 90),
            (7, 4, 12, 4)
        )

        self.rect = self.surf.get_rect()
        self.rect.left = x - self.rect.width
        self.rect.centery = y

    def move(self):
        self.rect.x -= self.speed


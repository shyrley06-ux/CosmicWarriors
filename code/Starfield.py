
#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import pygame


class Starfield:

    def __init__(self, window):
        self.window = window
        self.width = 800
        self.height = 600
        self.stars = []

        # Carregar o fundo da partida
        self.background = pygame.image.load(
            "assets/images/Purple_Nebula_06-512x512.png"
        ).convert()

        self.background = pygame.transform.scale(
            self.background, (self.width, self.height)
        )

        # Criar estrelas
        for _ in range(100):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            speed = random.randint(1, 5)
            radius = random.choice([1, 1, 2])

            self.stars.append({
                "x": x,
                "y": y,
                "speed": speed,
                "radius": radius
            })

    def move(self):
        for star in self.stars:
            star["y"] += star["speed"]

            if star["y"] > self.height:
                star["y"] = 0
                star["x"] = random.randint(0, self.width - 1)

    def draw(self):
        # Desenhar a nebulosa
        self.window.blit(self.background, (0, 0))

        # Desenhar estrelas sobre a imagem
        for star in self.stars:
            pygame.draw.circle(
                self.window,
                (220, 230, 255),
                (star["x"], star["y"]),
                star["radius"]
            )


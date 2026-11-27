
#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Starfield import Starfield


class Level:

    def __init__(self, window):
        self.window = window
        self.name = "Cosmic Warriors"
        self.entity_list = []
        self.score_to_win = 100

        self.starfield = Starfield(window)
        self.clock = pygame.time.Clock()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return "EXIT"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            self.starfield.move()
            self.starfield.draw()

            pygame.display.update()
            self.clock.tick(60)

        return "MENU"

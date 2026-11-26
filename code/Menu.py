#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Background import Background


class Menu:

    def __init__(self, window):
        self.window = window
        self.background = Background(window)

        self.title_font = pygame.font.Font(None,72)
        self.option_font = pygame.font.Font(None, 42)
        self.options = [
            "NEW GAME",
            "SCORE",
            "EXIT",
        ]
        self.selected_option = 0

    def run(self):
        self.background.draw()
        title = self.title_font.render(
            "COSMIC WARRIORS", True, (255, 255, 255)
        )
        title_rect = title.get_rect(center=(400, 150))
        self.window.blit(title,title_rect)

        for index, option in enumerate(self.options):
            color = (0, 255, 255) if index == self.selected_option else (255, 255, 255)

            text = self.option_font.render(
                option, True, color
            )

            text_rect = text.get_rect(
                center=(400, 300 + index * 70)
            )
            self.window.blit(text, text_rect)

        pygame.display.update()





#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Menu import Menu
from code.Level import Level


class Game:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.window = pygame.display.set_mode(
            size=(800, 600)
        )

        pygame.display.set_caption("Cosmic Warriors")

        pygame.mixer.music.load(
            "assets/audio/8bit-spaceshooter.mp3"
        )

        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)


    def run(self):
        menu = Menu(self.window)

        while True:
            action = menu.run()

            if action == "EXIT":
                break

            elif action == "NEW GAME":
                level = Level(self.window)
                result = level.run()

                if result == "EXIT":
                    break
                elif result == "GAME OVER":
                    print("GAME OVER")
                elif result == "NEXT LEVEL":
                    print("Parabéns! Próximo nível")
                elif result == "YOU WIN":
                    print("Você venceu!")

            elif action == "SCORE":
                print("SCORE selecionado!")

        pygame.quit()



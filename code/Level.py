
#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import random

from code.Starfield import Starfield
from code.Enemy import Enemy
from code.Player import Player
from code.EntityMediator import EntityMediator


class Level:

    def __init__(self, window):
        self.window = window
        self.name = "Cosmic Warriors"

        self.level_number = 1
        self.lives = 5
        self.score = 0
        self.clock = pygame.time.Clock()

        self.level_settings = {
            1: {
                "time": 105,
                "score_to_win": 125
            },
            2: {
                "time": 165,
                "score_to_win": 250
            }
        }

        self.time_limit = self.level_settings[1]["time"]
        self.score_to_win = self.level_settings[1]["score_to_win"]

        self.entity_list = []

        self.starfield = Starfield(window)
        self.player = Player(window)
        self.enemy_shots = []
        self.last_enemy_shot = pygame.time.get_ticks()

        # Criar 27 naves em posicoes aleatorias
        for i in range(27):
            enemy = Enemy(window)

            enemy.rect.x = random.randint(
                0,window.get_width()

            )
            enemy.rect.y = random.randint(
                80,window.get_height() - enemy.rect.height - 20
            )


            self.entity_list.append(enemy)

        # Fonte menor para a HUD
        self.font = pygame.font.Font(None, 20)

        self.start_ticks = pygame.time.get_ticks()

    def draw_hud(self):
        """Desenha as informações do jogo na horizontal."""

        elapsed_seconds = (
            pygame.time.get_ticks() - self.start_ticks
        ) // 1000

        remaining_seconds = max(
            0, self.time_limit - elapsed_seconds
        )

        hud_items = [
            f"NIVEL: {self.level_number}",
            f"PONTOS: {self.score}/{self.score_to_win}",
            f"VIDAS: {self.lives}",
            f"TEMPO: {remaining_seconds}s"
        ]

        x = 20
        y = 15
        spacing = 35

        for text in hud_items:
            surface = self.font.render(
                text, True, (255, 255, 255)
            )

            self.window.blit(surface, (x, y))
            x += surface.get_width() + spacing

    def run(self):
        running = True

        while running:
            elapsed_seconds = (
                                      pygame.time.get_ticks() - self.start_ticks
                              ) // 1000

            remaining_seconds = max(
                0, self.time_limit - elapsed_seconds
            )

            if self.lives <= 0:
                return "GAME OVER"

            if self.score >= self.score_to_win:
                if self.level_number == 1:
                    return "NEXT LEVEL"
                return "YOU WIN"

            if remaining_seconds <= 0:
                return "GAME OVER"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "EXIT"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return "MENU"

                    elif event.key == pygame.K_SPACE:
                        print("Space Detected")
                        self.player.shoot()

            self.starfield.move()
            self.starfield.draw()



            # Movimentar e desenhar os inimigos
            for enemy in self.entity_list:
                enemy.move()

                self.window.blit(
                    enemy.surf,
                    enemy.rect
                )

            # Disparo automático a cada 1,2 segundos
            current_ticks = pygame.time.get_ticks()

            if (
                self.entity_list
                and current_ticks - self.last_enemy_shot >= 700
            ):
                enemy = random.choice(self.entity_list)
                enemy.shoot()

                self.enemy_shots.extend(enemy.shots)
                enemy.shots.clear()

                self.last_enemy_shot = current_ticks


                # Adicionar os tiros criados à lista geral
                for shot in enemy.shots[:]:
                    if shot not in self.enemy_shots:
                        self.enemy_shots.append(shot)


            # Movimentar e desenhar a nave do jogador
            self.player.move()
            self.window.blit(
                self.player.surf,
                self.player.rect
            )


            # Movimentar e desenhar os tiros do jogador
            for shot in self.player.bullets[:]:
                shot.move()

                self.window.blit(
                    shot.surf,
                    shot.rect
                )

                if shot.rect.left > self.window.get_width():
                    self.player.bullets.remove(shot)

            # Movimentar e desenhar os tiros inimigos
            for shot in self.enemy_shots[:]:
                shot.move()

                self.window.blit(
                    shot.surf,
                    shot.rect
                )

                if shot.rect.right < 0:
                    self.enemy_shots.remove(shot)

            # Mediar as colisões
            points, lost_lives = EntityMediator.verify_collision(
                self.player.bullets,
                self.enemy_shots,
                self.entity_list,
                self.player
            )

            self.score += points
            self.lives -= lost_lives


            self.draw_hud()

            pygame.display.update()
            self.clock.tick(60)

        return "MENU"

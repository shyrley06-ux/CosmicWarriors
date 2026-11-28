
#!/usr/bin/python
# -*- coding: utf-8 -*-

class EntityMediator:

    @staticmethod
    def verify_collision(player_shots, enemy_shots, enemies, player):
        score = 0
        lives_lost = 0

        # Tiros do jogador atingindo inimigos
        for shot in player_shots[:]:
            for enemy in enemies[:]:
                if shot.rect.colliderect(enemy.rect):
                    if shot in player_shots:
                        player_shots.remove(shot)

                    if enemy in enemies:
                        enemies.remove(enemy)

                    score += 5
                    break

        # Tiros inimigos atingindo o jogador
        for shot in enemy_shots[:]:
            if shot.rect.colliderect(player.rect):
                if shot in enemy_shots:
                    enemy_shots.remove(shot)

                lives_lost += 1

        return score, lives_lost

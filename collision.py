from gameConst import SCORE_TABLE

def player_hit_by_enemy_bullets(player, enemy_bullets):
    for bullet in enemy_bullets[:]:
        if player.rect.colliderect(bullet["rect"]):
            enemy_bullets.remove(bullet)
            return True
    return False


def enemies_hit_by_player(enemies, player, explosions, now, stats):
    for enemy in enemies[:]:
        for bullet in player.bullets[:]:
            if enemy.rect.colliderect(bullet["rect"]):
                player.bullets.remove(bullet)
                enemy.hp -= 1

                if enemy.hp <= 0:
                    explosions.append({
                        "pos": enemy.rect.center,
                        "frame": 0,
                        "last_update": now
                    })
                    enemies.remove(enemy)

                    stats["kills"] += 1
                    stats["score"] += SCORE_TABLE.get(enemy.type, 0)
                break
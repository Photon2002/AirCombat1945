import random
from gameConst import WIDTH, HEIGHT

def spawn_heal(heals, heal_img, distance, next_heal_distance):
    if distance < next_heal_distance:
        return next_heal_distance

    rect = heal_img.get_rect()
    rect.x = WIDTH + 20
    rect.y = random.randint(50, HEIGHT - 50)

    heals.append({"rect": rect})

    return next_heal_distance + random.randint(200, 300)


def update_heals(heals, player, heal_img, screen):
    for heal in heals[:]:
        heal["rect"].x -= player.speed

        if heal["rect"].right < 0:
            heals.remove(heal)
            continue

        if player.rect.colliderect(heal["rect"]):
            player.hp = min(player.max_hp, player.hp + 20)
            heals.remove(heal)
            continue

        screen.blit(heal_img, heal["rect"])
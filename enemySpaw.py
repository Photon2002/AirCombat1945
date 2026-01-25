import random
from enemy import Enemy
from gameConst import WIDTH, HEIGHT

def spawn_enemy(enemies, enemy_types):
    # losowanie typu wroga wg wag
    enemy_type = random.choices(
        population=list(enemy_types.keys()),
        weights=[0.33, 0.3, 0.07, 0.13, 0.12, 0.05]  # ME109, FW190 , ME262, JU87, ME110, HE111
    )[0]

    side = random.choice(["left", "right"])

    # tworzymy przeciwnika, podając typ i cały słownik enemy_types
    enemy = Enemy(
        enemy_type=enemy_type,
        enemy_types=enemy_types,
        screen_width=WIDTH,
        screen_height=HEIGHT,
        side=side
    )

    enemies.append(enemy)
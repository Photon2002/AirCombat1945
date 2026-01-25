import sys
from enemy import update_enemies, draw_enemies
from gameConst import *
from assets import *
from background import *
from player import Player
from explosion import update_explosions, draw_explosions
from enemyBullets import update_enemy_bullets, draw_enemy_bullets
from enemySpaw import spawn_enemy
from collision import player_hit_by_enemy_bullets, enemies_hit_by_player
from hud import draw_hud, draw_menu, draw_game_over
from healing import spawn_heal, update_heals
from enemyTypes import load_enemy_types

GAME_MENU = "menu"
GAME_PLAYING = "playing"
GAME_PAUSED = "paused"
GAME_QUIT = "quit"
GAME_OVER = "game_over"

bullets = []
enemies = []
explosions = []
enemy_bullets = []
heals = []

score = 0
kills = 0
distance = 0
next_heal_distance = 0

def reset_game():
    global score, kills, distance
    enemies.clear()
    enemy_bullets.clear()
    player.reset()
    score = 0
    kills = 0
    distance = 0

game_state = GAME_MENU

pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AIR COMBAT 1945")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 36)

plane_img = load_image("assets/MB5.png", (220, 75))
bullet_img = load_image("assets/bulletGreen.png", (80, 20))
enemy_bullet_img = load_image("assets/bulletRed.png", (80, 20))
enemy_types = load_enemy_types()
heal_img = load_image("assets/Healing.png", (64, 64))
parallax = create_parallax()
stats = {
    "score": 0,
    "kills": 0
}

player = Player(plane_img)
explosion_frames = load_explosions()
load_music()
pygame.mixer.music.play(-1)
last_enemy_spawn = 0
last_shot_time = 0

# --- game loop ---
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if game_state == GAME_PLAYING:
                    game_state = GAME_PAUSED
                elif game_state == GAME_PAUSED:
                    game_state = GAME_PLAYING

        if game_state == GAME_MENU:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    reset_game()
                    game_state = GAME_PLAYING
                elif event.key == pygame.K_ESCAPE:
                    running = False

        if game_state == GAME_OVER:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    reset_game()
                    game_state = GAME_MENU
                elif event.key == pygame.K_ESCAPE:
                    running = False

        if game_state == GAME_PLAYING:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state = GAME_MENU  # albo PAUSE


    if game_state == GAME_MENU:
        draw_menu(screen, font)
        pygame.display.flip()
        clock.tick(60)

    elif game_state == GAME_PAUSED:
        draw_enemies(screen, enemies)
        player.draw_bullets(screen, bullet_img)
        draw_enemy_bullets(screen, enemy_bullets, enemy_bullet_img)
        draw_explosions(screen, explosions, explosion_frames)
        draw_hud(screen, font, player, stats, distance)

        pause_text = font.render("PAUSED", True, (255, 255, 0))
        screen.blit(pause_text, pause_text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

        pygame.display.flip()
        clock.tick(60)

    elif game_state == GAME_PLAYING:
        distance += player.speed * 0.1

        next_heal_distance = spawn_heal(
            heals, heal_img, distance, next_heal_distance
        )

        parallax.update(player.speed / max_speed)
        parallax.draw(screen)
        keys = pygame.key.get_pressed()
        player.update(keys)

        keys = pygame.key.get_pressed()

        current_time = pygame.time.get_ticks()
        if current_time - last_enemy_spawn > enemy_spawn_cooldown:
            spawn_enemy(enemies, enemy_types)
            last_enemy_spawn = current_time

        keys = pygame.key.get_pressed()
        player.shoot(bullet_img, keys[pygame.K_SPACE])
        player.update_bullets(screen, bullet_img)

        now = pygame.time.get_ticks()

        update_enemies(enemies, player.speed, HEIGHT, WIDTH, enemy_bullets, enemy_bullet_img, now)
        update_enemy_bullets(enemy_bullets, speed)

        if player_hit_by_enemy_bullets(player, enemy_bullets):
            if now - player.last_hit_time > player.hit_cooldown:
                player.hp -= 1
                player.last_hit_time = now
            if player.hp <= 0:
                player.hp = 0
                game_state = GAME_OVER

        update_heals(heals, player, heal_img, screen)
        enemies_hit_by_player(enemies, player, explosions, now, stats)

        now = pygame.time.get_ticks()

        update_explosions(explosions, explosion_frames, now)

        # drawing
        screen.blit(plane_img, player.rect)
        draw_enemies(screen, enemies)
        player.draw_bullets(screen, bullet_img)
        draw_enemy_bullets(screen, enemy_bullets, enemy_bullet_img)
        draw_explosions(screen, explosions, explosion_frames)
        draw_hud(screen, font, player, stats, distance)

        pygame.display.flip()
        clock.tick(60)  # 60 FPS

    elif game_state == GAME_OVER:
        draw_game_over(screen, font, stats, distance)
        pygame.display.flip()
        clock.tick(60)

pygame.quit()
sys.exit()
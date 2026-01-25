import pygame
from gameConst import WIDTH, HEIGHT

def draw_hud(screen, font, player, stats, distance):
    y = 10
    x = 10

    # HP BAR
    max_hp = player.max_hp
    bar_width = 150
    bar_height = 16

    hp_ratio = player.hp / max_hp
    pygame.draw.rect(screen, (80, 80, 80), (x, y + 6, bar_width, bar_height))        # tło paska
    pygame.draw.rect(screen, (0, 255, 0), (x, y + 6, bar_width * hp_ratio, bar_height))  # zielony pasek HP

    x += bar_width + 30

    # Kills
    kills_text = font.render(f"Kills: {stats['kills']}", True, (255, 255, 255))
    screen.blit(kills_text, (x, y))
    x += kills_text.get_width() + 30

    # Score
    score_text = font.render(f"Score: {stats['score']}", True, (255, 215, 0))
    screen.blit(score_text, (x, y))
    x += score_text.get_width() + 30

    # Distance
    dist_text = font.render(f"{int(distance)} m", True, (180, 180, 255))
    screen.blit(dist_text, (x, y))


def draw_menu(screen, font):
    screen.fill((20, 20, 30))

    title = font.render("AIR COMBAT 1945", True, (255, 255, 255))
    start = font.render("ENTER - Start", True, (200, 200, 200))
    quit_text = font.render("ESC - Exit", True, (200, 200, 200))

    screen.blit(title, title.get_rect(center=(WIDTH//2, HEIGHT//2 - 60)))
    screen.blit(start, start.get_rect(center=(WIDTH//2, HEIGHT//2)))
    screen.blit(quit_text, quit_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 40)))

def draw_game_over(screen, font, stats, distance):
    screen.fill((10, 10, 20))

    title = font.render("GAME OVER", True, (255, 60, 60))
    score_text = font.render(f"Score: {stats['score']}", True, (255, 215, 0))
    kills_text = font.render(f"Kills: {stats['kills']}", True, (200, 200, 200))
    dist_text = font.render(f"Distance: {int(distance)} m", True, (180, 180, 255))

    hint1 = font.render("ENTER - Back to menu", True, (180, 180, 180))
    hint2 = font.render("ESC - Quit", True, (180, 180, 180))

    screen.blit(title, title.get_rect(center=(WIDTH//2, HEIGHT//2 - 120)))
    screen.blit(score_text, score_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 40)))
    screen.blit(kills_text, kills_text.get_rect(center=(WIDTH//2, HEIGHT//2)))
    screen.blit(dist_text, dist_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 40)))
    screen.blit(hint1, hint1.get_rect(center=(WIDTH//2, HEIGHT//2 + 100)))
    screen.blit(hint2, hint2.get_rect(center=(WIDTH//2, HEIGHT//2 + 140)))

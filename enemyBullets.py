def update_enemy_bullets(enemy_bullets, player_speed):
    for bullet in enemy_bullets:
        # pociski w przód
        if "speed_x" in bullet and "speed_y" in bullet:
            bullet["rect"].x += bullet["speed_x"] - player_speed
            bullet["rect"].y += bullet["speed_y"]
        else:
            bullet["rect"].x += bullet["speed"] - player_speed

def draw_enemy_bullets(screen, bullets, bullet_img):
    for bullet in bullets:
        img = bullet.get("img") or bullet_img  # jeśli bullet ma własny, użyj jego, inaczej domyślny
        screen.blit(img, bullet["rect"])

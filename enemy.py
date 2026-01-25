import pygame
import random
import math

from gameConst import ENEMY_BURST_DELAY, ENEMY_BURST_PAUSE, ENEMY_BULLET_SPEED

class Enemy:
    def __init__(self, enemy_type, enemy_types, screen_width, screen_height, side="left"):
        self.type = enemy_type
        self.enemy_type = enemy_type
        data = enemy_types[enemy_type]  # pobranie danych z enemyTypes.py

        self.img = data["img"]
        self.rect = self.img.get_rect()
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Pozycja startowa
        if side == "left":
            self.rect.x = -self.rect.width
        else:
            self.rect.x = screen_width + random.randint(100, 300)
        self.rect.y = random.randint(50, screen_height - self.rect.height - 50)

        # Statystyki wroga
        self.speed = random.uniform(*data["speed_range"])
        self.burst_count = data["burst_count"]
        self.hp = data["hp"]
        self.rear_burst_count = data.get("rear_burst_count", 0)

        # Strzelanie
        self.shots_left = self.burst_count
        self.last_shot = pygame.time.get_ticks()
        self.cooldown = False

        if self.rear_burst_count > 0:
            self.rear_shots_left = self.rear_burst_count
            self.rear_last_shot = pygame.time.get_ticks()
            self.rear_cooldown = False

        # Ruch
        self.active = False
        self.pattern = random.choice(["straight", "wave", "climb", "dive"])
        self.angle = random.uniform(0, math.pi * 2)
        self.vertical_speed = random.uniform(1.5, 3.0)

    def update(self, player_speed, screen_height):
        self.rect.x += self.speed - player_speed

        if not self.active:
            if self.rect.right > 0 and self.rect.left < self.screen_width:
                self.active = True

        if self.active:
            if self.pattern == "wave":
                self.angle += 0.05
                self.rect.y += int(math.sin(self.angle) * 3)
            elif self.pattern == "climb":
                self.rect.y -= self.vertical_speed
            elif self.pattern == "dive":
                self.rect.y += self.vertical_speed

        # ograniczenie ruchu w pionie
        self.rect.y = max(20, min(screen_height - self.rect.height - 20, self.rect.y))

    def try_shoot(self, enemy_bullets, bullet_img, now):
        if not self.active:
            return

        # przednie działko
        self.shoot_front(enemy_bullets, bullet_img, now)

        # tylne działko, jeśli w danych jest rear_burst_count
        if self.rear_burst_count > 0:
            self.shoot_rear(enemy_bullets, bullet_img, now)

        if self.type == "HE111":
            self.shoot_bottom_rear(enemy_bullets, bullet_img, now)

    def shoot_front(self, enemy_bullets, bullet_img, now):
        if not hasattr(self, "last_shot"):
            self.last_shot = 0
            self.shots_left = self.burst_count
            self.cooldown = False

        if not self.cooldown:
            if now - self.last_shot >= ENEMY_BURST_DELAY:
                bullet_rect = bullet_img.get_rect()
                bullet_rect.midleft = self.rect.midright
                enemy_bullets.append({
                    "rect": bullet_rect,
                    "speed": ENEMY_BULLET_SPEED + self.speed,
                    "angle": 0,
                    "travelled": 0
                })
                self.shots_left -= 1
                self.last_shot = now
                if self.shots_left <= 0:
                    self.cooldown = True
        else:
            if now - self.last_shot >= ENEMY_BURST_PAUSE:
                self.shots_left = self.burst_count
                self.cooldown = False
                self.last_shot = now

    def shoot_rear(self, enemy_bullets, bullet_img, now):
        if not hasattr(self, "rear_last_shot"):
            self.rear_last_shot = 0
            self.rear_shots_left = self.rear_burst_count
            self.rear_cooldown = False

        if not self.rear_cooldown:
            if now - self.rear_last_shot >= ENEMY_BURST_DELAY:
                bullet_rect = bullet_img.get_rect()
                if self.enemy_type == "JU87":
                    bullet_rect.centerx = self.rect.centerx - 15
                    bullet_rect.centery = self.rect.centery - 57
                elif self.enemy_type == "ME110":
                    bullet_rect.centerx = self.rect.centerx - 5  # trochę dalej w lewo
                    bullet_rect.centery = self.rect.centery - 60  # trochę w górę
                elif self.enemy_type == "HE111":
                    bullet_rect.centerx = self.rect.centerx + 25  # więcej w lewo
                    bullet_rect.centery = self.rect.centery - 75  # bliżej środka
                rear_speed = ENEMY_BULLET_SPEED * 0.5
                angle_deg = 135
                rotated_bullet_img = pygame.transform.rotate(bullet_img, -45)  # obrót pod kątem w górę
                rotated_bullet_img = pygame.transform.rotate(rotated_bullet_img, -180)
                rad = math.radians(angle_deg)
                enemy_bullets.append({
                    "img": rotated_bullet_img,
                    "rect": bullet_rect,
                    "speed_x": int(-rear_speed * math.cos(rad)),
                    "speed_y": int(-rear_speed * math.sin(rad)),
                    "angle": angle_deg,
                    "travelled": 0
                })
                self.rear_shots_left -= 1
                self.rear_last_shot = now
                if self.rear_shots_left <= 0:
                    self.rear_cooldown = True
        else:
            if now - self.rear_last_shot >= ENEMY_BURST_PAUSE:
                self.rear_shots_left = self.rear_burst_count
                self.rear_cooldown = False
                self.rear_last_shot = now

    def shoot_bottom_rear(self, enemy_bullets, bullet_img, now):
        if not hasattr(self, "bottom_last_shot"):
            self.bottom_last_shot = 0
            self.bottom_shots_left = self.rear_burst_count  # używamy tej samej liczby strzałów co tylne
            self.bottom_cooldown = False

        if not self.bottom_cooldown:
            if now - self.bottom_last_shot >= ENEMY_BURST_DELAY:
                bullet_rect = bullet_img.get_rect()

                # Offset: trochę w lewo i w dół od środka samolotu
                bullet_rect.centerx = self.rect.centerx - 27
                bullet_rect.centery = self.rect.centery + 25

                rear_speed = ENEMY_BULLET_SPEED * 0.5
                angle_deg = 250  # w lewo i w dół
                rotated_bullet_img = pygame.transform.rotate(bullet_img, -135)  # obrót pod kątem w górę
                rad = math.radians(angle_deg)
                enemy_bullets.append({
                    "img": rotated_bullet_img,
                    "rect": bullet_rect,
                    "speed_x": int(-rear_speed * math.cos(rad)),
                    "speed_y": int(-rear_speed * math.sin(rad)),
                    "angle": angle_deg,
                    "travelled": 0
                })

                self.bottom_shots_left -= 1
                self.bottom_last_shot = now

                if self.bottom_shots_left <= 0:
                    self.bottom_cooldown = True
        else:
            if now - self.bottom_last_shot >= ENEMY_BURST_PAUSE:
                self.bottom_shots_left = self.rear_burst_count
                self.bottom_cooldown = False
                self.bottom_last_shot = now

    def is_offscreen(self, width, margin=400):
        return self.rect.right < -margin or self.rect.left > width + margin

def update_enemies(enemies, player_speed, screen_height, width,
                   enemy_bullets, enemy_bullet_img, now):
    for enemy in enemies[:]:
        enemy.update(player_speed, screen_height)
        enemy.try_shoot(enemy_bullets, enemy_bullet_img, now)

        if enemy.is_offscreen(width):
            enemies.remove(enemy)

def draw_enemies(screen, enemies):
    for enemy in enemies:
        screen.blit(enemy.img, enemy.rect)
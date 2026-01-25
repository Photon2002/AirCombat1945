import pygame
from gameConst import *


class Player:
    def __init__(self, img):
        self.img = img
        self.rect = img.get_rect()
        self.rect.y = HEIGHT // 2

        self.max_hp = 100
        self.hp = self.max_hp

        self.speed = min_speed
        self.target_speed = min_speed

        self.bullets = []
        self.last_shot_time = 0

        self.last_hit_time = 0
        self.hit_cooldown = 400

    def reset(self):
        self.rect.y = HEIGHT // 2
        self.speed = min_speed
        self.target_speed = min_speed

        self.hp = self.max_hp
        self.bullets.clear()
        self.last_shot_time = 0

    def update(self, keys):
        # ruch w pionie
        if keys[pygame.K_w]:
            self.rect.y -= vertical_speed
        if keys[pygame.K_s]:
            self.rect.y += vertical_speed

        # prędkość w poziomie
        if keys[pygame.K_d]:
            self.target_speed = min(max_speed, self.target_speed + acceleration)
        elif keys[pygame.K_a]:
            self.target_speed = max(min_speed, self.target_speed - deceleration)

        self.speed += (self.target_speed - self.speed) * 0.1

        self.rect.x = int(
            (self.speed - min_speed) / (max_speed - min_speed) * (WIDTH - self.rect.width)
        )

        # ograniczenie ekranu
        self.rect.y = max(0, min(HEIGHT - self.rect.height, self.rect.y))

    def shoot(self, bullet_img, shooting):
        current_time = pygame.time.get_ticks()
        if shooting and current_time - self.last_shot_time > shoot_cooldown:
            bullet_rect = bullet_img.get_rect()
            bullet_rect.midleft = (
                self.rect.right - 75,
                self.rect.centery + 25
            )
            self.bullets.append({
                "rect": bullet_rect,
                "travelled": 0
            })
            self.last_shot_time = current_time

    def update_bullets(self, screen, bullet_img):
        for bullet in self.bullets[:]:
            bullet["rect"].x += PLAYER_BULLET_SPEED
            bullet["travelled"] += PLAYER_BULLET_SPEED

            if bullet["travelled"] >= PLAYER_BULLET_RANGE:
                self.bullets.remove(bullet)
                continue

            screen.blit(bullet_img, bullet["rect"])

    def draw_bullets(self, screen, bullet_img):
        for bullet in self.bullets:
            screen.blit(bullet_img, bullet["rect"])
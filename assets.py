import pygame

def load_image(path, size=None):
    img = pygame.image.load(path).convert_alpha()
    if size:
        img = pygame.transform.scale(img, size)
    return img

def load_explosions():
    frames = []
    for i in range(1, 8):
        img = load_image(f"assets/explosion/{i}.png", (140, 140))
        frames.append(img)
    return frames

def load_music():
    pygame.mixer.music.load("songs/ZERO_Ace_Combat_Zero_Lucas_Ricciotti.mp3")
    pygame.mixer.music.set_volume(0.5)
from assets import load_image
from gameConst import WIDTH, HEIGHT

class Parallax:
    def __init__(self, backgrounds):
        self.backgrounds = backgrounds
        self.BASE_SCROLL_SPEED = 0.5

    def update(self, world_speed):
        for bg in self.backgrounds:
            bg["x"] -= self.BASE_SCROLL_SPEED + bg["speed"] * world_speed
            if bg["x"] <= -bg["img"].get_width():
                bg["x"] = 0

    def draw(self, screen):
        for bg in self.backgrounds:
            screen.blit(bg["img"], (bg["x"], 0))
            screen.blit(bg["img"], (bg["x"] + bg["img"].get_width(), 0))

def create_parallax():
    layers = [
        {"img": load_image("assets/bg/forest_sky.png", (WIDTH, HEIGHT)), "speed": 0.1, "x": 0},
        {"img": load_image("assets/bg/forest_mountain.png", (WIDTH, HEIGHT)), "speed": 0.4, "x": 0},
        {"img": load_image("assets/bg/forest_back.png", (WIDTH, HEIGHT)), "speed": 0.6, "x": 0},
        {"img": load_image("assets/bg/forest_long.png", (WIDTH, HEIGHT)), "speed": 1.0, "x": 0},
        {"img": load_image("assets/bg/forest_mid.png", (WIDTH, HEIGHT)), "speed": 1.5, "x": 0},
        {"img": load_image("assets/bg/forest_short.png", (WIDTH, HEIGHT)), "speed": 2.2, "x": 0},
    ]
    return Parallax(layers)
#stałe w grze
WIDTH, HEIGHT = 1024, 768

speed = 10.0
vertical_speed = 8.0
target_speed = 5.0
min_speed = 1.0
max_speed = 20.0
acceleration = 0.3    # jak szybko przyspiesza
deceleration = 0.4    # jak szybko zwalnia

enemy_speed = 6.0
enemy_spawn_cooldown = 1500  # ms
last_enemy_spawn = 0


ENEMY_SHOOT_COOLDOWN = 1200  # ms
ENEMY_BULLET_SPEED = 12
ENEMY_BURST_COUNT = 3
ENEMY_BURST_DELAY = 300      # ms między strzałami w serii
ENEMY_BURST_PAUSE = 1500     # ms przerwy po serii

PLAYER_BULLET_RANGE = 900
ENEMY_BULLET_RANGE = 700

shoot_cooldown = 200  # ms

PLAYER_BULLET_SPEED = 15


BASE_SCROLL_SPEED = 0.5   # minimalny ruch świata

EXPLOSION_FRAME_TIME = 80  # ms

BULLET_MARGIN = 300  # how many pixels behind screen will be tolerated

SCORE_TABLE = {
    "ME109": 100,
    "FW190": 200,
    "JU87": 150,
    "ME262": 500,
    "ME110": 300,
    "HE111": 1000
}
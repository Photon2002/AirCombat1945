from assets import load_image

def load_enemy_types():
    return {
        "ME109": {
            "img": load_image("assets/Me-109F.png", (220, 60)),
            "speed_range": (7.0, 10.0),
            "burst_count": 3,
            "hp": 3
        },
        "FW190": {
            "img": load_image("assets/FW190.png", (240, 70)),
            "speed_range": (9.0, 11.0),
            "burst_count": 4,
            "hp": 4
        },
        "ME262": {
            "img": load_image("assets/Me-262.png", (220, 70)),
            "speed_range": (11.0, 14.0),
            "burst_count": 5,
            "hp": 6
        },
        "JU87": {
            "img": load_image("assets/Ju87.png", (220, 90)),
            "speed_range": (5.0, 7.0),
            "burst_count": 1,
            "rear_burst_count": 3,
            "hp": 2
        },
        "ME110": {
            "img": load_image("assets/ME110.png", (325, 80)),
            "speed_range": (8.0, 10.0),
            "burst_count": 3,
            "rear_burst_count": 2,
            "hp": 10
        },
        "HE111": {
            "img": load_image("assets/He111.png", (440, 120)),
            "speed_range": (4.0, 6.0),
            "burst_count": 1,
            "rear_burst_count": 2,
            "hp": 20
        }
    }
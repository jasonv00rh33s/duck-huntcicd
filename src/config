import argparse

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
DUCK_COORDS = [(350, 390), (450, 390), (550, 390), (650, 390)]

def parse_args():
    parser = argparse.ArgumentParser(description="Duck Hunt Game")
    parser.add_argument(
        "--difficulty", choices=["easy", "normal", "hard"],
        default="normal", help="Game difficulty (default: normal)"
    )
    parser.add_argument(
        "--bg_color", choices=["image", "blue", "black", "gray"],
        default="image", help="Background style: default image or solid color"
    )
    return parser.parse_args()

DIFFICULTY_SPEED = {
    "easy":   {"duck_step": 8,  "flight_duration": 150, "escape_speed": 1.2},
    "normal": {"duck_step": 10, "flight_duration": 100, "escape_speed": 1.5},
    "hard":   {"duck_step": 14, "flight_duration": 50, "escape_speed": 2.0},
}

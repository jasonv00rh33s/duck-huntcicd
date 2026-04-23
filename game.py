import pygame
from src.config import parse_args
from src.engine import GameEngine, handle_quit()
from src.duck import Duck
from src.ui import HUD

def main():
    args = parse_args()
    engine = GameEngine(fps=60)
    hud = HUD(engine, bg_color=args.bg_color)
    duck = Duck(hud.duck_surface, difficulty=args.difficulty)
    duck.spawn()

    score = 0
    crosses = 0
    state = "flying"  # "flying" | "falling"

    def game_loop():
        nonlocal score, crosses, state

        for event in pygame.event.get():
            handle_quit(event)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if state == "flying":
                    mx, my = pygame.mouse.get_pos()
                    if duck.is_hit(mx, my):
                        duck.kill()
                        score += 1
                        state = "falling"
 
        duck.update()

          if state == "flying" and duck.is_escaped():
            crosses += 1
            if crosses >= 3:
                hud.show_game_over(score)
            duck.spawn()

        elif state == "falling" and duck.is_fallen():
            duck.spawn()
            state = "flying"

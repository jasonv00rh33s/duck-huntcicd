import pygame
import sys
from tkinter import messagebox, Tk
from src.config import SCREEN_WIDTH

class HUD:
    def __init__(self, engine, bg_color="image"):
        self.engine = engine
        self.bg_color = bg_color
        self._load_assets()   
        self._init_crosshair() 

    def _load_assets(self):
        e = self.engine
        self.background = e.load_image("assets/background.png")
        self.overlay = e.load_image("assets/overlay.png")
        self.score_img = e.load_image("assets/score.png")
        self.red_cross = e.load_image("assets/red_cross.png")
        self.crosshair = e.load_image("assets/crosshair.png")  
        duck_raw = e.load_image("assets/duck.png")
        w = duck_raw.get_width() // 3
        h = duck_raw.get_height() // 3
        self.duck_surface = pygame.transform.scale(duck_raw, (w, h))

    def _init_crosshair(self):
        pygame.mouse.set_visible(False)
        w = self.crosshair.get_width()
        h = self.crosshair.get_height()
        if w > 64 or h > 64:
            self.crosshair = pygame.transform.scale(self.crosshair, (48, 48))

    def draw_crosshair(self, screen: pygame.Surface):
        mx, my = pygame.mouse.get_pos()
        w = self.crosshair.get_width()
        h = self.crosshair.get_height()
        screen.blit(self.crosshair, (mx - w // 2, my - h // 2))

    def draw_score(self, screen, score):
        screen.blit(self.score_img, (SCREEN_WIDTH - 220, 0))
        font = pygame.font.Font(None, 60)
        text = font.render(str(score), 1, (58, 31, 4))
        screen.blit(text, (SCREEN_WIDTH - 80, 8))

    def draw_crosses(self, screen, cross_count):
        base_x = SCREEN_WIDTH - 165
        for i in range(min(cross_count, 3)):
            screen.blit(self.red_cross, (base_x + i * 47, 55))

    def draw_background(self, screen):
        if self.bg_color == "image":
            screen.blit(self.background, (0, 0))
        elif self.bg_color == "blue":
            screen.fill((135, 206, 235)) 
        elif self.bg_color == "black":
            screen.fill((0, 0, 0))        
        elif self.bg_color == "gray":
            screen.fill((128, 128, 128))  

    def draw_overlay(self, screen):
        screen.blit(self.overlay, (0, 0))
        
    def show_game_over(self, score):
        pygame.mouse.set_visible(True)
        Tk().withdraw()
        messagebox.showinfo("Game Over", f"Game over!\nScore: {score}")
        pygame.quit()
        sys.exit()

    def draw_frame(self, screen, duck_surface, duck_pos, score, crosses):
        self.draw_background(screen)
        screen.blit(duck_surface, duck_pos)
        self.draw_overlay(screen)
        self.draw_score(screen, score)
        self.draw_crosses(screen, crosses)
        self.draw_crosshair(screen)

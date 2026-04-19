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
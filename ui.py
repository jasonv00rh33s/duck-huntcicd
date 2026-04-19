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
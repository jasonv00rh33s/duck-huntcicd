import pytest
from unittest.mock import MagicMock, patch
import pygame
from src.ui import HUD

# Маркер для тестів інтерфейсу 
@pytest.mark.ui
class TestHUD:

    # Фікстура для створення моку двигуна гри 
    @pytest.fixture
    def mock_engine(self):
        engine = MagicMock()
        # Мокуємо завантаження зображень, щоб повертати пусту поверхню
        surface_mock = MagicMock(spec=pygame.Surface)
        surface_mock.get_width.return_value = 300
        surface_mock.get_height.return_value = 300
        engine.load_image.return_value = surface_mock
        return engine

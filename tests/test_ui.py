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
    
    # Фікстура для ініціалізації HUD з мокованим двигуном 
    @pytest.fixture
    def hud(self, mock_engine):
        with patch('pygame.mouse.set_visible'):
            return HUD(mock_engine)

    def test_hud_initialization(self, mock_engine):
        """Перевірка коректної ініціалізації HUD та завантаження асетів [cite: 10]"""
        with patch('pygame.mouse.set_visible') as mock_visible:
            hud = HUD(mock_engine)
            assert hud.bg_color == "image"
            # Перевірка, чи викликалися методи завантаження зображень
            assert mock_engine.load_image.called
            # Перевірка, чи було приховано курсор миші
            mock_visible.assert_called_with(False)

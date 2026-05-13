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
        with patch('pygame.mouse.set_visible'), \
             patch('pygame.transform.scale') as mock_scale:

            mock_scale.return_value = mock_engine.load_image.return_value
            return HUD(mock_engine)

    def test_hud_initialization(self, mock_engine):
        """Перевірка коректної ініціалізації HUD та завантаження асетів"""
        with patch('pygame.mouse.set_visible') as mock_visible, \
             patch('pygame.transform.scale'): # Додаємо цей патч тут
            hud = HUD(mock_engine)
            assert hud.bg_color == "image"
            assert mock_engine.load_image.called
            mock_visible.assert_called_with(False)
    
    @pytest.mark.parametrize("color, expected_rgb", [
        ("blue", (135, 206, 235)),
        ("black", (0, 0, 0)),
        ("gray", (128, 128, 128))
    ])
    def test_draw_background_colors(self, mock_engine, color, expected_rgb):
        """Перевірка заливки фону відповідними кольорами [cite: 10]"""
        # Додаємо патчі сюди, бо ми створюємо HUD вручну
        with patch('pygame.mouse.set_visible'), \
             patch('pygame.transform.scale'):
            
            hud = HUD(mock_engine, bg_color=color)
            screen_mock = MagicMock()
            hud.draw_background(screen_mock)
            screen_mock.fill.assert_called_with(expected_rgb)

    def test_draw_score(self, hud):
        """Тестування відображення рахунку з використанням мокування шрифтів """
        screen_mock = MagicMock()
        with patch('pygame.font.Font') as mock_font_class:
            mock_font = MagicMock()
            mock_font_class.return_value = mock_font
            
            hud.draw_score(screen_mock, 150)
            
            # Перевірка рендерингу тексту
            mock_font.render.assert_called()
            assert "150" in str(mock_font.render.call_args)

    @patch('src.ui.messagebox.showinfo')
    @patch('src.ui.Tk')
    @patch('src.ui.sys.exit')
    @patch('src.ui.pygame.quit')
    def test_show_game_over(self, mock_pygame_quit, mock_sys_exit, mock_tk, mock_msg, hud):
        """Тестування завершення гри та виклику діалогового вікна (Mocking) """
        hud.show_game_over(50)
        
        # Перевірка відображення вікна з результатом
        mock_msg.assert_called_once()
        assert "50" in mock_msg.call_args[0][1]
        
        # Перевірка коректного завершення програм
        mock_pygame_quit.assert_called_once()
        mock_sys_exit.assert_called_once()

    def test_draw_crosses(self, hud):
        """Перевірка малювання хрестиків (життів) [cite: 10]"""
        screen_mock = MagicMock()
        hud.draw_crosses(screen_mock, 2)
        # Має бути 2 виклики blit для червоних хрестиків
        assert screen_mock.blit.call_count == 2

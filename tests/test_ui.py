import pytest
from unittest.mock import MagicMock, patch
from src.ui import HUD

@pytest.fixture
def mock_engine_with_assets():
    """Створює фейковий ігровий рушій, який повертає пусті поверхні замість картинок."""
    engine = MagicMock()
    
    # Фейкова картинка, яка має розміри 90x90
    dummy_surface = MagicMock()
    dummy_surface.get_width.return_value = 90
    dummy_surface.get_height.return_value = 90
    
    # Коли HUD викличе load_image, повертаємо фейкову картинку
    engine.load_image.return_value = dummy_surface
    return engine

@patch('src.ui.pygame.mouse.set_visible')
@patch('src.ui.pygame.transform.scale')
def test_hud_initialization(mock_scale, mock_set_visible, mock_engine_with_assets):
    """Перевіряє завантаження ассетів та налаштування HUD."""
    # Задаємо моку transform.scale повернення магічного об'єкта
    mock_scale.return_value = MagicMock()
    
    hud = HUD(engine=mock_engine_with_assets, bg_color="gray")
    
    assert hud.bg_color == "gray"
    # Перевіряємо, що мишка стала невидимою (замінена на приціл)
    mock_set_visible.assert_called_once_with(False)
    # HUD має завантажити 6 картинок (фон, оверлей, рахунок, хрестик, приціл, качка)
    assert mock_engine_with_assets.load_image.call_count == 6

def test_hud_draw_background_colors(mock_engine_with_assets):
    """Перевіряє заливку екрану різними кольорами."""
    hud = HUD(engine=mock_engine_with_assets, bg_color="blue")
    mock_screen = MagicMock()
    
    hud.draw_background(mock_screen)
    # Перевіряємо rgb код для "blue" з файлу ui.py
    mock_screen.fill.assert_called_once_with((135, 206, 235))

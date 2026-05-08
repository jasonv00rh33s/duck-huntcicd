import pytest
from unittest.mock import MagicMock, patch
from src.ui import HUD

@pytest.fixture
def mock_engine_with_assets():
    """Створює фейковий ігровий рушій, який повертає пусті поверхні замість картинок."""
    engine = MagicMock()
    
    dummy_surface = MagicMock()
    dummy_surface.get_width.return_value = 90
    dummy_surface.get_height.return_value = 90
    
    engine.load_image.return_value = dummy_surface
    return engine

@patch('src.ui.pygame.mouse.set_visible')
@patch('src.ui.pygame.transform.scale')
def test_hud_initialization(mock_scale, mock_set_visible, mock_engine_with_assets):
    """Перевіряє завантаження ассетів та налаштування HUD."""
    mock_scale.return_value = MagicMock()
    
    hud = HUD(engine=mock_engine_with_assets, bg_color="gray")
    
    assert hud.bg_color == "gray"
    mock_set_visible.assert_called_once_with(False)
    assert mock_engine_with_assets.load_image.call_count == 6

# Додано мокування для scale та set_visible, щоб запобігти крашу Pygame
@patch('src.ui.pygame.mouse.set_visible')
@patch('src.ui.pygame.transform.scale')
def test_hud_draw_background_colors(mock_scale, mock_set_visible, mock_engine_with_assets):
    """Перевіряє заливку екрану різними кольорами."""
    mock_scale.return_value = MagicMock()
    
    hud = HUD(engine=mock_engine_with_assets, bg_color="blue")
    mock_screen = MagicMock()
    
    hud.draw_background(mock_screen)
    mock_screen.fill.assert_called_once_with((135, 206, 235))

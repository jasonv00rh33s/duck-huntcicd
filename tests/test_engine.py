import pytest
from unittest.mock import patch
from src.engine import GameEngine

@patch('src.engine.pygame') # Повністю мокаємо pygame в engine.py
def test_engine_init(mock_pygame):
    """Перевіряє ініціалізацію головного рушія гри."""
    engine = GameEngine(fps=30)
    
    # Перевіряємо, чи викликались базові функції Pygame
    mock_pygame.init.assert_called_once()
    mock_pygame.display.set_mode.assert_called_once_with((800, 600))
    mock_pygame.display.set_caption.assert_called_once_with("Duck Hunt")
    
    assert engine.fps == 30
    assert engine._running is False

@patch('src.engine.sys.exit')
@patch('src.engine.pygame.quit')
def test_engine_quit(mock_pygame_quit, mock_sys_exit):
    """Перевіряє логіку безпечного виходу з гри."""
    engine = GameEngine()
    engine.quit()
    
    mock_pygame_quit.assert_called_once()
    mock_sys_exit.assert_called_once()

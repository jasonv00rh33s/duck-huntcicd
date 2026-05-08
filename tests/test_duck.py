import pytest
import pygame
from unittest.mock import MagicMock, patch
from src.duck import Duck

# --- ФІКСТУРИ (Fixtures) ---
@pytest.fixture
def mock_surface():
    """Створює мок-об'єкт поверхні Pygame, щоб не ініціалізувати реальне вікно."""
    return MagicMock(spec=pygame.Surface)

@pytest.fixture
def duck_normal(mock_surface):
    """Повертає екземпляр качки зі стандартною складністю."""
    return Duck(surface=mock_surface, difficulty="normal")

# --- ТЕСТОВІ МАРКЕРИ (Test markers) ---
@pytest.mark.gameplay
def test_duck_initial_state(duck_normal):
    """Перевіряє правильність початкових параметрів качки."""
    assert duck_normal._alive is True
    assert duck_normal._escaping is False
    assert duck_normal._frame_count == 0

# --- ПАРАМЕТРИЗАЦІЯ (Parametrization) ---
@pytest.mark.parametrize("difficulty, expected_speed", [
    ("easy", 8),
    ("normal", 10),
    ("hard", 14)
])
def test_duck_speed_parametrization(mock_surface, difficulty, expected_speed):
    """Перевіряє, чи правильно встановлюється швидкість залежно від рівня складності."""
    duck = Duck(surface=mock_surface, difficulty=difficulty)
    assert duck.base_speed == expected_speed

# --- МОКУВАННЯ (Mocking) ---
@patch('src.duck.random.randint')
def test_duck_spawn_mocking(mock_randint, duck_normal):
    """Використовує мокування для фіксації випадкового числа при спавні."""
    mock_randint.return_value = 150  # Фіксуємо координату X
    duck_normal.spawn()
    assert duck_normal._x == 150
    assert duck_normal._alive is True

@pytest.mark.gameplay
def test_duck_kill(duck_normal):
    """Перевіряє логіку "вбивства" об'єкта качки."""
    duck_normal.spawn()
    duck_normal.kill()
    assert duck_normal._alive is False
    assert duck_normal._vy == 6  # Задана швидкість падіння з duck.py

@pytest.mark.parametrize("mouse_x, mouse_y, expected_hit", [
    (50, 50, True),   # Координати всередині хітбоксу (10..100)
    (200, 200, False) # Координати поза хітбоксом
])
def test_duck_is_hit(duck_normal, mouse_x, mouse_y, expected_hit):
    """Перевіряє механіку реєстрації влучання миші."""
    # Штучно встановлюємо координати качки
    duck_normal._x = 10
    duck_normal._y = 10
    duck_normal._alive = True
    # DUCK_WIDTH та DUCK_HEIGHT дорівнюють 90
    assert duck_normal.is_hit(mouse_x, mouse_y) == expected_hit

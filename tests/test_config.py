import pytest
import sys
from unittest.mock import patch
from src.config import parse_args, DIFFICULTY_SPEED

def test_parse_args_defaults():
    """Перевіряє, чи встановлюються дефолтні значення, якщо аргументи не передані."""
    # Імітуємо запуск скрипта без параметрів: python game.py
    with patch.object(sys, 'argv', ['game.py']):
        args = parse_args()
        assert args.difficulty == 'normal'
        assert args.bg_color == 'image'

def test_parse_args_custom():
    """Перевіряє парсинг кастомних аргументів користувача."""
    # Імітуємо запуск: python game.py --difficulty hard --bg_color blue
    test_args = ['game.py', '--difficulty', 'hard', '--bg_color', 'blue']
    with patch.object(sys, 'argv', test_args):
        args = parse_args()
        assert args.difficulty == 'hard'
        assert args.bg_color == 'blue'



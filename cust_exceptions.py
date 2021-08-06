"""Исключения, используемые в программе."""
from typing import Any


class InputParameterVerificationError(Exception):
    """Исключение для неверных параметров на входе декоратора."""

    def __init__(self, msg: str = 'Wrong input parameters.') -> None:
        """Инициализация."""
        super().__init__(msg)


class ResultVerificationError(Exception):
    """Исключение для результата выполнения функции."""

    def __init__(self: Any, msg: str = 'Your function return wrong results.') -> None:
        """Инициализация."""
        super().__init__(msg)


class FailRepeatTimesError(Exception):
    """Исключение для неверного количества раз повторения вызова функции."""

    def __init__(self, msg: str = 'Your function returns wrong results.') -> None:
        """Инициализация."""
        super().__init__(msg)

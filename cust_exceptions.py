"""Исключения, используемые в программе."""
from typing import Any


class InputParameterVerificationError(Exception):
    """Исключение для неверных параметров на входе декоратора."""

    def __init__(self, msg='Wrong input parameters.', *args: Any, **kwargs: Any) -> None:
        """Инициализация."""
        super().__init__(msg, *args, **kwargs)


class ResultVerificationError(Exception):
    """Исключение для результата выполнения функции."""

    def __init__(self, msg='Your function return wrong results.', *args: Any, **kwargs: Any) -> None:
        """Инициализация."""
        super().__init__(msg, *args, **kwargs)


class FailRepeatTimesError(Exception):
    """Исключение для неверного количества раз повторения вызова функции."""

    def __init__(self, msg='Your function return wrong results.', *args: Any, **kwargs: Any) -> None:
        """Инициализация."""
        super().__init__(msg, *args, **kwargs)

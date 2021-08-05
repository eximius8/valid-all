"""Файл для декоратора valid_all."""
from cust_exceptions import (
    FailRepeatTimesError,
    InputParameterVerificationError,
    ResultVerificationError)
from typing import Callable, Any

def valid_all(
    input_validation: Callable,
    output_validation: Callable,
    on_fail_repeat_times: int = 1,
    default_behavior: Callable = None,
) -> Callable:
    """Основной декоратор."""
    if on_fail_repeat_times == 0:
        # Неверно указан параметр
        raise FailRepeatTimesError

    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if not input_validation(*args, **kwargs):
                # Проверка входных парметров
                raise InputParameterVerificationError
            result = func(*args, **kwargs)
            if output_validation(result):
                # Функция прошла проверку выходных параметров с первого раза
                return func(*args, **kwargs)
            else:
                # Запомнить ошибку, если функция не прошла проверку
                error = ResultVerificationError()
            if on_fail_repeat_times < 0:
                # Функцию можно повторить бесконечно
                while not output_validation(result):
                    result = func(*args, **kwargs)
            else:
                # Функцию можно повторить указанное число раз
                for _ in range(on_fail_repeat_times - 1):
                    # Повторяем функцию необходимое количество раз
                    result = func(*args, **kwargs)
                    if output_validation(result):
                        return result
                    else:
                        error = ResultVerificationError()
                if default_behavior:
                    # Если задана default_behavior выполнить её
                    default_behavior()
                else:
                    raise error
        return wrapper
    return decorator

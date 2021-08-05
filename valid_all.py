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
    """Декоратор для валидации функции."""
    if on_fail_repeat_times == 0:
        raise FailRepeatTimesError

    def decoration(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if input_validation(*args, **kwargs):
                result = func(*args, **kwargs)
                if output_validation(result):
                    return func(*args, **kwargs)
                else:
                    error = ResultVerificationError()
                    
                    if on_fail_repeat_times < 0:
                        while not output_validation(result):
                            result = func(*args, **kwargs)
                    else:
                        for i in range(on_fail_repeat_times):
                            result = func(*args, **kwargs)
                            if output_validation(result):
                                return result
                            else:
                                print(error)
                        if not default_behavior:
                            pass
                        else:
                            default_behavior()
            else:
                raise InputDataError("Входные данные не прошли валидацию")

        return wrapper

    return decoration
"""Исключения, используемые в программе"""

class InputParameterVerificationError(Exception):
    """Исключение для неверных параметров на входе декоратора."""

    def __init__(self, msg='Wrong input parameters.', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class ResultVerificationError(Exception):
    """Исключение для результата выполнения функции."""

    def __init__(self, msg='Your function return wrong results.', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

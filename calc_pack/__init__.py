from .addition import add
from .subtraction import subtract
from .multiplication import multiply
from .division import divide


class Calculator:
    """
    Класс для выполнения арифметических операций с использованием модулей пакета.

    Методы:
        add(x, y): Возвращает сумму x и y.
        subtract(x, y): Возвращает разницу между x и y.
        multiply(x, y): Возвращает произведение x и y.
        divide(x, y): Возвращает результат деления x на y.
    """

    def add(self, x, y):
        return add(x, y)

    def subtract(self, x, y):
        return subtract(x, y)

    def multiply(self, x, y):
        return multiply(x, y)

    def divide(self, x, y):
        return divide(x, y)

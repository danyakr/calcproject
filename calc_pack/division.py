def divide(x, y):
    """
    Возвращает результат деления одного числа на другое.

    Args:
        x (float): Делимое.
        y (float): Делитель.

    Returns:
        float: Результат деления x на y.

    Raises:
        ZeroDivisionError: Если y равен нулю.
    """
    if y == 0:
        raise ZeroDivisionError("На ноль делить нельзя!")
    return x / y

def divide(dividend: float, divisor: float) -> float:
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 8, operator=divide)
print(result)
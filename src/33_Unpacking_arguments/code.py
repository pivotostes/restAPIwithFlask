def multiply(*args):
    # print(args)
    total = 1
    for arg in args:
        total *= arg

    return total


print(multiply(1, 2, 3, 4, 5))


def add(x, y):
    return x + y


num1 = [1, 4]
print(add(*num1))

nums2 = {"x": 15, "y": 6}
print(add(**nums2))


def apply(*args, operator):
    if operator == '*':
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"


print(apply(1, 2, 3, 4, 5, operator="+"))
print(apply(1, 2, 3, 4, 5, operator="*"))

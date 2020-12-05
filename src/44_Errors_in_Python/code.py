def divide(dividend: float, divisor: float) -> float:
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": [78, 87]},
    {"name": "Jen", "grades": [100, 90]}
]

print("-- Welcome to the average grade program. --")
try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except ZeroDivisionError as e:
    print(e)
    print(f"ERROR: {name} has no grades!")
else:
    print("-- All students averages calculated --")
finally:
    print("-- End of student average calculation! Thank you! --")

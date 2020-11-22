sequence = [1, 3, 5, 9, 11]
doubled = [(lambda x: x * 2)(x) for x in sequence]
doubled_2 = list(map(lambda x: x * 2, sequence))

print(sequence)
print(doubled)
print(doubled_2)

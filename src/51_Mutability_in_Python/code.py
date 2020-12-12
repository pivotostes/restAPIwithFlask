a = []
b = []

print(id(a))
print(id(b))
print(id(a) == id(b))

a.append(35)

print(a)
print(b)


c = 8597
d = 8597

print(id(c))
print(id(d))
print(id(c) == id(d))

print(c)
print(d)

c = 8596

print(id(c))
print(id(d))
print(id(c) == id(d))

print(c)
print(d)

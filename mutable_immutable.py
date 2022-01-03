## integer is immutable
x = 1
print(id(x))

x = x + 1
print(id(x))

## list is mutable
y = [1,2,3]
print(id(y))
y.append(4)
print(id(y))

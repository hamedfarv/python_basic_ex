def multiply(*number):
    total = 1
    for numbers in number:
        total *=numbers
    return total

print("start")
print(multiply(1,2,3))



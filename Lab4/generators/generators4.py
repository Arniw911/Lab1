def squares(a, b):
    for i in range(a, b+1):
        yield i**2

square = squares(3, 7)

for i in square:
    print(i)

    
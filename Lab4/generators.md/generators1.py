def generate_squears(N):
    for i in range(1, N+1):
        yield (i**2)

squares = generate_squears(10)


for i in squares:
    print(i)
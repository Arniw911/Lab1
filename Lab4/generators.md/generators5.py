def nums(n):
    for i in range(n+1):
        yield (n-i)

reverse = nums(10)


for i in reverse:
    print(i)
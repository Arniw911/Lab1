def filter_prime(numlist):
    sum = 0
    primelist = []
    for i in numlist:
        is_prime = True
        if i < 2:
            is_prime = False
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primelist.append(i)
    return primelist
print(filter_prime([6, 4, 3, 2, 5, 1, 7, 8, 9, 9]))

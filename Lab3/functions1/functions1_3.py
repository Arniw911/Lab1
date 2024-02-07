def solve(numheads, numlegs):
    c = 0
    r = 0
    for c in range(numheads):
        r = (c+1) - r
        if 2*(c+1) + 4*r == numlegs:
            return "Chicken: " + str(c+1) + '\n' + "Rabbits: " + str(r)
print(solve(35, 94))

import math
sides = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))
if sides == 4:
    print(length * length)
else: 
    a = length/(2 *math.tan(180 * math.pi/(sides * 180)))
    print(a* sides*length/2)
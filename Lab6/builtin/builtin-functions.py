#Ex 1
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
multiply = 1
for i in list:
    multiply = i * multiply
print(multiply)

#Ex 2
my_str = "ABcde"

lower_num = 0 
upper_num = 0

for i in my_str:
    if i.islower():
        lower_num+=1
    elif i.isupper():
        upper_num+=1
print("Amount of lower case letters is {}, amount of upper is {}".format(lower_num,upper_num))   

#Ex 3
def isPalindrome(string):
    return string==string[::-1]
print(isPalindrome("walaw"))

#Ex 4 
import time
from threading import Timer
from math import sqrt

def delayedSquareRoot(number, delay_ms):
    def square_root():
        result = sqrt(number)
        print(f"Square root of {number} after {delay_ms} milliseconds is {result}")

    t = Timer(delay_ms / 1000, square_root)
    t.start()

number = 25100
delay_ms = 2123
delayedSquareRoot(number, delay_ms)

while True:
    time.sleep(1)


#Ex 5
my_tuple = (True, 1 , "a")

print(all(my_tuple))
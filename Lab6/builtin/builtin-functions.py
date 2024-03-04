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
print("Number of lowercase letters is {} and number of uppercase letters is {}".format(lower_num,upper_num))   

#Ex 3
def isPalindrome(string):
    string2 = ''.join(reversed(string))
    return string==string2
print(isPalindrome("walaw"))

#Ex 4 
import time
import math

def squareRoot(number):
    return math.sqrt(number)
def delay(number, delay_ms):
    delaySeconds = delay_ms / 1000
    time.sleep(delaySeconds)
    result = squareRoot(number)
    print(f"The square root of {number} after {delay_ms} is {result}")

num = int(input())
delaytime = int(input())

delay(num, delaytime)



#Ex 5
my_tuple = (True, 1 , "a")

print(all(my_tuple))

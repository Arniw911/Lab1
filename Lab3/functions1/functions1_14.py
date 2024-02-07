from functions1_1 import gToOunce
from functions1_2 import ftoc
from functions1_3 import solve
from functions1_4 import filter_prime
from functions1_5 import wordPermutations
from functions1_6 import reversecentence
from functions1_7 import has_33
from functions1_8 import spy_game
from functions1_9 import sphere
from functions1_10 import uniquenums
from functions1_11 import is_palindrome
from functions1_12 import histogram
from functions1_13 import comparison
from itertools import permutations
import random



print(gToOunce(12))
print(ftoc(88))
print(solve(35, 94))
print(filter_prime([6, 4, 3, 2, 5, 1, 7, 8, 9, 9]))
wordPermutations("abc")
reversecentence("We are ready")
print(has_33([1, 3, 3]))
print(spy_game([1,2,4,0,0,7,5]))
sphere(9)
print(uniquenums([1,0,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,5,5]))
print(is_palindrome("lalal"))
histogram([4, 9, 7])
a = random.randrange(1, 21)
comparison(a)
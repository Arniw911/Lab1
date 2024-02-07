from itertools import permutations

def  wordPermutations(word):
    for p in permutations(word):
        print(''.join(p))

wordPermutations("abc")
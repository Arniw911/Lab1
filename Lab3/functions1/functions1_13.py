import random
def comparison(randomnum):
    name = input("Hello! What is your name?" '\n')
    print('\n' "Well " + name + ", I am thinking of a number between 1 and 20.")
    count = 1
    while(True):
        print("Take a guess.")
        inputnum = int(input())
        if inputnum < randomnum:
            print('\n' "Your guess is too low.")
            count = count + 1
        elif inputnum > randomnum:
            print('\n' "Your guess is too high.")
            count = count + 1
        elif inputnum == randomnum:
            print('\n' "Good job, "+ name + "! You guessed my number in", count, "guesses!")
            break
a = random.randrange(1, 21)
comparison(a)

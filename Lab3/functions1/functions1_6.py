def reversecentence(getline):
    words = getline.split()
    reversedWords = reversed(words)
    for i in reversedWords:
        print(i, end = ' ')

reversecentence("We are ready")


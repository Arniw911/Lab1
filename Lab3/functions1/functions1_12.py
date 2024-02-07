def histogram(list):
    for i in range(len(list)):
        for j in range(list[i]):
            print("*",end = '')
        print("\n", end = '')
    
histogram([4, 9, 7])
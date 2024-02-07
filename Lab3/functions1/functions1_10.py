def uniquenums(ulist):
    sortlist = []
    for x in ulist:
        if x not in sortlist:
            sortlist.append(x)
    return sortlist
print(uniquenums([1,0,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,5,5]))
from movies import movies
def averageIMDB(movies, newlist):
    averagelist = []
    for i in newlist:
        for j in movies:
            if i == j["name"]:
                averagelist.append(j["imdb"])
    sum = 0
    for k in averagelist:
        sum = k + sum
    return sum/len(averagelist)
print(averageIMDB(movies, ['Usual Suspects', 'Hitman', 'Dark Knight', 'The Help', 'The Choice',
 'Colonia', 'Love', 'Joking muck', 'What is the name', 'Detective', 'We Two']))



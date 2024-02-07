from movies import movies
def averageByCategory(movies, category):
    validmovie = []
    for i in movies:
        if i["category"] == category:
            validmovie.append(i["imdb"])
    sum = 0
    for j in validmovie:
        sum = j + sum
    return sum/len(validmovie)
print(averageByCategory(movies, "Thriller"))
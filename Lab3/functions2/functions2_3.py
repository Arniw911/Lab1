from movies import movies
def moviesByCategory(movies, category):
    validmovie = []
    for i in movies:
        if i["category"] == category:
            validmovie.append(i["name"])
    return validmovie
print(moviesByCategory(movies, "Thriller"))
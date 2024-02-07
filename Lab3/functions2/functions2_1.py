from movies import movies
def rate(name, movies):
    for i in movies:
        if i["name"] == name:
            if i["imdb"] > 5.5:
                return True
    return False
print(rate('We Two', movies))


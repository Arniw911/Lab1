import datetime

ds1 = input()
ds2 = input()

date1 = datetime.datetime.strptime(ds1, '%y-%m-%d-%H-%M-%S')
date2 = datetime.datetime.strptime(ds2, '%y-%m-%d-%H-%M-%S')

delta = date2 - date1

seconds = delta.total_seconds()

print(seconds)

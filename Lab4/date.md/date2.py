import datetime

today = datetime.date.today()
tommorow = datetime.date.today() + datetime.timedelta(days = 1)
yesterday = datetime.date.today() + datetime.timedelta(days = -1)

print("Today is " + str(today))
print("Tommorow it will be " + str(tommorow))
print("Yesterday it was " + str(yesterday))
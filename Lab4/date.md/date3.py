import datetime

milliseconds = str(datetime.datetime.now())
millisecondsnow = milliseconds.split(".")
print(millisecondsnow[1])

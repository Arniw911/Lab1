#Example1
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Example2
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#Example3
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Example4
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
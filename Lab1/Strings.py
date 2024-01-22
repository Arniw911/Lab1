#Example1
print("Hello")
print('Hello')

#Example2
a = "Hello"
print(a)

#Example3
#You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Example4
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Example5
#Loop through the letters in the word "banana":

for x in "banana":
  print(x)

#Example6
#The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))

#Example7
#Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)

#Example8
#Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Example9
#Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)

#Example10
#print only if "expensive" is NOT present:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


#Exercice1
x = "Hello World"
print(len(x))

#Exercice2
txt = "Hello World"
x = txt[0]

#Exercice3
txt = "Hello World"
x = txt[2:5]

#Exercice4
txt = " Hello World "
x = txt.strip()

#Exercice5
txt = "Hello World"
txt = txt.upper()

#Exercice6
txt = "Hello World"
txt = txt.lower()

#Exercice7
txt = "Hello World"
txt = txt.replace("H", "J")

#Exercice8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#Ex 1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#ans: in


#Ex 2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#ans: fruits.add("orange")


#Ex 3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#ans: fruits.update(more_fruits)


#Ex 4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#ans: fruits.remove("banana")


#Ex 5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#ans: fruits.discard("banana")
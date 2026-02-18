# Name : Ronnie Muturi
# Date : 18/02/2026
# program to show tples in python
# tuples of fruits 

fruits = ("Avocado","Kiwi", "Apple", "Banana", "Orange")

print(len(fruits))
print(fruits[0])
print(fruits[4])
print(fruits[-1])
print(fruits[-5])

# error -> fruits.append("Guava")

fruits_list = list(fruits)

fruits_list.append("Guava")

print(fruits_list)
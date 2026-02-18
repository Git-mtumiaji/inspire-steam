# Name : Ronnie Muturi
# Date : 18/02/2026
# program to show dictionaries in python 


car = {"Model" : "Audi",
        "Make" : "Q8",
        "Colour" : "Cherry",
        "Year" : "2025"}

print(car)

print(car["Model"])
print(car["Year"])
# using forloop for dictionries
students = {"Alice" : 24,
            "James" : 18,
             "Mark" : 22,
             "Daisy" : 19}

for key in students:
    print(key)

for val in students.values():
    print(val)
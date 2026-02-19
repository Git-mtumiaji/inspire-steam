# Name : Ronnie Muturi
# Date : 19/02/2026

# Classes(objects) in python

class Human:
    # First we define the attributes of a human being
    type = "Mammal"
    legs = 2
    brain = True
    warm_blooded = True
    city = "Nairobi"

    # We then create a constructor for the class/object
    #The constructor will be used to create copies for this object
    def __init__(self,name,age):
        self.human_name = name
        self.human_age = age

    def tell_story(self):
        print(f"Hello, I am [self.human_name]. Here is a story")
        print(f"There once was a ship who put to sea. The name was called Sir. Billy only")

#craete the humans
ron = Human("Ron", 17)
toto = Human("Toto", 20)

#List the humans created do things
ron.tell_story()
print("Ron's age is: ", ron.human_age)

# Modify one of the objects withut modifying other objects
print(f"Ron's location :", ron.city)
print(f"Toto's location :", toto.city)
toto.city = "Kiambu"

print(f"Ron's location :", ron.city)
print(f"Toto's location :", toto.city)
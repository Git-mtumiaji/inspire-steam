# Name : Ronnie Muturi
# Date : 23/02/2026
# Program to show inheritance in python


class Animal():

    def __init__(self,species,weight,food):
        self.species = species
        self.weight = weight
        self.food = food

    def grow(self,weight):
        weight = 1.1 * weight 
        print(f"The animal weighs {weight} Kgs")

    def eat(self,food):
        print(f"The animal eats {food}")

class Dog(Animal):

    def __init__(self,colour,species,height,breed):
        super().__init__(species,weight,food)
        self.height = height
        self.colour = colour
        self.breed = breed


    def barks(self):
        print(f"The dog says woof woof")

class Horse(Animal):

    def __init__(self,species,weight,food):
        self.species = species
        self.weight = weight
        self.food = food

    def neighs(self):
        print(f"The horse says neigh neigh")


# Name : Ronnie Muturi
# Date : 16/02/2026
# program to calculate the factorials of numbers

number = int(input("Enter the number x: ")) #Gets the number from user
factorial = 1 # initialize factorial 1
for x in range (0 , number):
    factorial = factorial * (x+1)
    number = (number - 1)


print(f"{number}! = {factorial}")
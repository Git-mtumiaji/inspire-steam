# Name : Ronnie Muturi
# Date : 13/02/2026
# program to calculate arithmetic progression

# calculating nth term

a = int(input("Enter the first number :"))
n = int(input("Enter the number of terms :"))
d = int(input("Enter the common difference :"))

nth_term = a + (n - 1) * d
sn = (n / 2) * ((2 * a) + ((n - 1) * d))
print(f"The nth term is : {nth_term}")
print(f"The sum of the terms is : {sn}")

# program to calculate geometric progression

# Assignment 

a = int(input("Enter the first number :"))
n = int(input("Enter the number of terms :"))
r = int(input("Enter the common ratio :"))

sn_gp = (a * (r**n)) / (r - 1)
print(f"The sum of the terms is : {sn_gp}")
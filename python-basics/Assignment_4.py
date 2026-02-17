# Name : Ronnie Muturi
# Date : 14/02/2026
# program to calculate geometric progression


a = int(input("Enter the first number :"))
n = int(input("Enter the number of terms :"))
r = int(input("Enter the common ratio :"))

sn_gp = (a * (r**n)) / (r - 1)
print(f"The sum of the terms is : {sn_gp}")
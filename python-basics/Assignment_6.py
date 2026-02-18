# Name : Ronnie Muturi
# Date : 17/02/2026
# program to display diamond and triangle using * and showing a quadratic equation

# 1. displaying diamond and triangle using * 
    # DIAMOND
rows = int(input("enter diamond height (odd number): "))
n = rows // 2 + 1

for i in range (n):
    print(" " * (n - i -1) + "*" * (2 * i + 1))

for i in range (n - 2, -1, -1):
    print(" " * (n - i -1) + "*" * (2 * i + 1))

   #TRIANGLE
rows = int(input("Enter nuber of rows: "))
for x in range(rows):
    print(" " * (rows - x - 1), end ="")
    print ("*" * (2 * x + 1))

# 2. Showing a quadratic equation
a = int(input("Enter the first number :"))
x = int(input("Enter the x? :"))
b = int(input("Enter the b? :"))
c = int(input("Enter the c? :"))
# Formula
quad_equation = (a * (x**2)) + (b * x) + c

print(f"The quadratic equation is {quad_equation}")
# Name : Ronnie Muturi
# Date : 13/02/2026

# program to show for loops in python and printing to show tables of squares using for loops and (**)
# Assignment 3
import math
for i in range (10,0,-1):
    print(i)

for y in range (-180,180,30):
    print(f"cosine of {y} = {math.cos(y)}")

for y in range (-180,180,30):
    print(f"sine of {y} = {math.sin(y)}")   
    
for y in range (-180,180,30):
    print(f"tangent of {y} = {math.tan(y)}")   


print(f"{'Angle (°)':>10} | {'sin':>8} | {'cos':>8} | {'tan':>8}")
print("-" * 42)

for angle in range(-180, 181, 30):
    radians = math.radians(angle)
    
    sin_val = math.sin(radians)
    cos_val = math.cos(radians)
    
    if abs(cos_val) < 1e-10:
        tan_val = "undef"
    else:
        tan_val = f"{math.tan(radians):.3f}"
    
    print(f"{angle:>10} | {sin_val:>8.3f} | {cos_val:>8.3f} | {tan_val:>8}")
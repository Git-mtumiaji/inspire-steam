# Name : Ronnie Muturi
# Date : 17/02/2026
# program to format the output in different styles

name = "Ronnie Muturi"

weight = 85 # weight in kgs

fav_team = "Arsenal"

height = 126.86 # height in cm

# 1. format using printf(f"{}")

print(f"My name is {name} and I weigh {weight} kgs.")

# 2. using f string
msg = f"My name is {name} and I suport {fav_team}."
print(msg)

# 3. using {} and .format

print("My name is {0} and I am {1} cm tall ". format(name,height))

# 4. Using output specifiers %s strings %f -> float

import math
print("The value of pi is approximately %5.3f." %math.pi)
print("I support %s " %fav_team)
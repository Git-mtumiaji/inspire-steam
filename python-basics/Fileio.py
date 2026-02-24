# Name : Ronnie Muturi
# Date : 24/02/2026
# Program to perform file operations

# create new file
new_file = open("student_data.txt", "r+")


# write to new file
new_file.write("{ Student Name : Ronnie Muturi , ID : 29783789 , email : gichohi.ronnie@gmail.com }")


# Read from the file
new_file = open("student_data.txt", "r+")

data = new_file.read()

print(data)

new_file.close()

# Delete file
#use os module
import os
os.remove("remove.txt")

# Delete folder
os.rmdir("folder")
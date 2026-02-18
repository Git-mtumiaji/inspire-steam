# Name : Ronnie Muturi
# Date : 18/02/2026
# program to show lists in python
# list of friends
friends = ["Rachael","Ross","Chandler","Monica","Joey"]

print(friends)
friends.sort()
print(friends)

friends.reverse()
print(friends)
friends.append("Jack")
print(friends)

new_friends = ["tracy","James", "kang`ethe", "Faith","Don","Augustine","Wendy"]
print(len(new_friends))

#new list of students
students = friends + new_friends

print(students)
students.pop()
print(students)
students.insert(5,"Jenny")
print(students)
students.insert(9,"Valarie")
print(students)
students.extend("James")
print(students)

students.remove("Joey")
print(students)

new_students = students.copy()
print(new_students)

# Dictionary = unordered, changable, index

#Making dictionary
# student = { "name" : "duraan", "email" : "duran@gmail.com", "age": 30}
# student2 = dict(name="abdi", email="abdi@gmail.com", age=25)

# print(student)
# print(student2)

# accessing key
# student = { "name" : "duraan", "email" : "duran@gmail.com", "age": 30}

# # x = student["email"]
# x = student.get("email")
# print(x)

# Change item

# student = { "name" : "duraan", "email" : "duran@gmail.com", "age": 30}

# student["name"] = "Ahmed"

# print(student)

# How to loop over dictionary

#Print Key
# student = { "name" : "duraan", "email" : "duran@gmail.com", "age": 30}

# for x in student:
#     print(x)
    
#Print Value

# for x in student:
#     print(student[x])

#print both key and value

# student = { "name" : "duraan", "email" : "duran@gmail.com", "age": 30}

# for x, y in student.items():
#     print(x, y)

# Check if item exists in dict
# student = { "name" : "duraan", "email" : "duran@gmail.com", "age": 30}

# if "class" in student:
#     print("yes")
# else:
#     print("No")

# Check Length of the dict

# student = { "name" : "duraan", "email" : "duran@gmail.com", "age": 30}

# print(len(student))

# How to add an item

# student = { "name" : "duraan", "email" : "duran@gmail.com", "age": 30}

# student["subject"] = "English"

# print(student)

# How to remove item

# # student = { "name" : "duraan", "email" : "duran@gmail.com", "age": 30}

# # student.pop("age")
# # student.popitem() # Before Python 3.7, it will remove random

# # del student # Delete the dict

# # student.clear() # Empty dict

# # print("Student: ", student)

# # Nested

# students = {
# "student1": { 
#             "name" : "duraan",
#             "email" : "duran@gmail.com", 
#             "age": 30,
#             "subject": "English",
#             "enrolled": True
#         },
# "student2" : {
#             "name": "Ahmed",
#             "email": "Ahmed@gmail.com",
#             "age": 25,
#             "subject": "Math",
#             "enrolled": False
#         }

# }

# print(students)


# Making a nested dictionary

# student1 = { 
#             "name" : "duraan",
#             "email" : "duran@gmail.com", 
#             "age": 30,
#             "subject": "English",
#             "enrolled": True
#         }
# student2 = {
#             "name": "Ahmed",
#             "email": "Ahmed@gmail.com",
#             "age": 25,
#             "subject": "Math",
#             "enrolled": False
#         }

# students2 = {
#     "student1": student1,
#     "student2": student2
# }

# print(students2)
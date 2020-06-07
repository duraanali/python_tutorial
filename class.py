# Python = Object Oriented Programming Language
# Almost everything in Python is object with properties and methods
# Class = Blueprint

# class Person:
#     x = 5
    
# p1 = Person()
# print(p1.x)

# init function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print("Hello, my name is " + self.name)
        
p1 = Person("Abdi", 30)
# print(p1.name, p1.age)
# p1.greeting()
# p1.age = 31
# del p1.age
# print(p1.age)

#Subclass/Parent-Child Class/Inheritance

class Student(Person):
    def __init__(self, name, age, graduationyear):
        super().__init__(name, age)
        self.graduationyear = graduationyear
        
    def welcome(self):
        print("Congratulations " + self.name + " Welcome to the class of", + self.graduationyear)
        
student1 = Student("Jamaal", 25, 2020)
student2 = Student("Hamdi", 26, 2021)

student2.welcome()
# function - block of code

# basic function
def magacaFun():
    print("Hello World")
    
# Pass
def magacaFun():
    pass

# Arguments

def salam(name):
    print("ASC", name)
    
salam("Duraan")

def add(x):
    print(10 * x)
    
add(5)

# Multiple Arguments

def salam(first_name, last_name):
    print("ASC", first_name, last_name)
    
salam("duraan", "ali")


# Arbitrary Arguments (Args)

def myKids(*kids):
    print("My youngest kid is " + kids[0])
    
myKids("Nasteexo", "Uthmaan")

# Keyword Arguments (Kwargs)

def myKids(child1, child2):
    print("My youngest kid is " + child2)
    
myKids(child1 = "Nasteexo", child2 = "Uthmaan")

# Arbitrary Keyword Arguments (**Kwargs) - DICT

def kids(**kids):
    print("her first name is " + kids["first_name"])
    print("her last name is " + kids["last_name"])

kids(first_name = "Nasteexo", last_name = "Ahmed")


# Return Value

def fun1(x, y):
    return y * x

print(fun1(7, 8))

#default Parameter

def wadan(wadan = "Somalia"):
    print("I am from " + wadan)

wadan()


# Lambda Function/Expressions - SMALL ANONYMOUS FUNCTION

# lambda argument : expression

x = lambda a: a + 10
print(x(5))

# Multiply

x = lambda a, b: a * b
print(x(9, 10))

# Power of Lambda: Function within function

def myFun(n):
    return lambda a: a * n

double = myFun(3)

print(double(10))
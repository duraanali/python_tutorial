# Simple Calculator made in Python if statement

# Input = Meel wax la galiyo

# statement = input("What is in your mind? ")

# print(statement)

first_number = float(input("Enter Your Number: "))
operator = input("Choose Operator: ")
second_number = float(input("Enter your second number: "))

if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "/":
    print(first_number / second_number)
elif operator == "*":
    print(first_number * second_number)
else:
    print("Invalid Operator")
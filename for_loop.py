 # For Loop = Interate over sequence (Ku soo cel celi waxyaabo)
 
# fruits = ["Apple", "Banana", "Cherry"]
 
# for item in fruits:
#      print(item)

# Loop over a string

# for x in "banana":
#     print(x)

# Break and Continue

# fruits = ["Apple", "Banana", "Cherry"]

# for x in fruits:
#     print(x)
#     if x == "Banana":
#         print("Found")
#         break

# for x in fruits:
#     print(x)
#     if x == "Banana":
#         print("Found")
#         continue

# Range

# for x in range(6):
#     print(x)

# for x in range(1, 20, 3):
#     print(x)

# Nested for loop

# colors = ["Red", "Yellow", "Orange"]
# fruits = ["Apple", "Banana", "Cherry"]

# for x in colors:
#     for y in fruits:
#         print(x, y)
    
# Enumerate - Counter - Build-in Function

fruits = ["Apple", "Banana", "Cherry"]

for counter, x in enumerate(fruits):
    print(counter, x)
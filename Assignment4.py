import math

# Get the coordinates for the calculation
isValid = False
while not isValid:
    string1 = input("Enter x coordinate of point 1: ")
    if string1.isnumeric():
        x1 = float(string1)
        isValid = True
    else:
        print("<< Coordinate must be a number. >>")
isValid = False
while not isValid:
    string1 = input("Enter y coordinate of point 1: ")
    if string1.isnumeric():
        y1 = float(string1)
        isValid = True
    else:
        print("<< Coordinate must be a number. >>")
isValid = False
while not isValid:
    string1 = input("Enter x coordinate of point 2: ")
    if string1.isnumeric():
        x2 = float(string1)
        isValid = True
    else:
        print("<< Coordinate must be a number. >>")
isValid = False
while not isValid:
    string1 = input("Enter y coordinate of point 2: ")
    if string1.isnumeric():
        y2 = float(string1)
        isValid = True
    else:
        print("<< Coordinate must be a number. >>")


# calculate the distance
dist = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

print("")
print("Distance between points =", dist)


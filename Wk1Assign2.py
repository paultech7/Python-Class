
# Get the inputs for the calculation
length = -1
width = -1
while length < 0:
    length = int(input("Enter a positive number for the length: "))
while width < 0:
    width = int(input("Enter a positive number for the width: "))

# calculate the area
area = length * width

print("")
print("Area =", area)

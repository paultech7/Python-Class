
# Get the inputs for the calculation
length = -1
width = -1
while length < 0:
    string1 = input("Enter the length: ")
    if string1.isdigit() and int(string1) > 0:
        length = int(string1)
    else:
        print("<< Length must be a positive number. >>")
while width < 0:
    string1 = input("Enter the width: ")
    if string1.isdigit() and int(string1) > 0:
        width = int(string1)
    else:
        print("<< Width must be a positive number. >>")

# calculate the area
area = length * width

print("")
print("Area =", area)

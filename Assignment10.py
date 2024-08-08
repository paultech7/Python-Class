# Get the age
age = 0
while age == 0:
    string1 = input("Enter your age: ")
    if string1.isdigit() and int(string1) > 0:
        age = int(string1)
    else:
        print("<< Please enter a positive integer for your age. >>")

# Calculate the category of the age
if age > 65:
    category = "Senior citizen"
elif age < 18:
    category = "Minor"
else:
    category = "Adult"

print("")
print("Your age category is", category)

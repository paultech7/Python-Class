# Get the age
string1 = input("Enter your age: ")

# Validate the input
if string1.isdigit():
    age = int(string1)
    if age > 0:

        # Calculate the category of the age and show the result
        if age > 65:
            category = "Senior citizen"
        elif age < 18:
            category = "Minor"
        else:
            category = "Adult"
        print("Your age category is", category)

    else:
        print("Error: Please enter a positive integer for your age.")
else:
    print("Error: Please enter a positive integer for your age.")


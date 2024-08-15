# Get the number of rows and the pattern character
string1 = input("Enter the number of rows: ")
patternInput = input("Enter the character for the pattern: ")
patternChar = patternInput[0]

# Validate the input
if string1.isdigit():
    numberOfRows = int(string1)
    if numberOfRows > 0:

        # Print a right triangle with the requested number of rows
        print("")
        for row in range(numberOfRows):
            for column in range(row + 1):
                print(patternChar, end="")
            print("")

    else:
        print("Error: Please enter a positive integer.")
else:
    print("Error: Please enter a positive integer.")

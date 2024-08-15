# Get the number of rows and the pattern character
string1 = input("Enter the number of rows: ")
patternCharIn = input("Enter the character for the pattern: ")
patternChar = patternCharIn[0]

# Validate the input
if string1.isdigit():
    numberOfRows = int(string1)
    if numberOfRows > 0:

        # Print a right triangle with the requested number of rows
        print("")
        row = patternChar
        for x in range(numberOfRows):
            print(row)
            row += patternChar

    else:
        print("Error: Please enter a positive integer.")
else:
    print("Error: Please enter a positive integer.")

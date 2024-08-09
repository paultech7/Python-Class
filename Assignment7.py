# Get the year to test
string1 = input("Enter the year: ")

# Validate the input
if string1.isdigit():
    year = int(string1)
    if year > 0:

        # Determine if the year is a leap one
        isLeapYear = False
        if year - (4 * int(year / 4)) == 0:
            if year - (100 * int(year / 100)) != 0:
                isLeapYear = True
            elif year - (400 * int(year / 400)) == 0:
                isLeapYear = True

        # Show the result
        if isLeapYear:
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")

    else:
        print("Error: the year must be a positive integer.")
else:
    print("Error: the year must be a positive integer.")

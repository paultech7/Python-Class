# Get the year to test
year = 0
while year == 0:
    string1 = input("Enter the year: ")
    if string1.isdigit() and int(string1) > 0:
        year = int(string1)
    else:
        print("<< Please enter a positive integer for the year. >>")

# Test if the year is a leap one. Leap years are divisible by 4 but not by 100 unless it is also divisible by 400.
isLeapYear = False
if year - (4 * int(year / 4)) == 0:
    if year - (100 * int(year / 100)) != 0:
        isLeapYear = True
    elif year - (400 * int(year / 400)) == 0:
        isLeapYear = True

print("")
if isLeapYear:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

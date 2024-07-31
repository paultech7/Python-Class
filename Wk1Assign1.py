# Get the inputs for the calculation
principal = 0
while principal == 0:
    string1 = input("Enter the principal amount: ")
    if string1.isdigit():
        principal = int(string1)
    else:
        print("<< Principal must be a number. >>")
rate = 0
while rate == 0:
    string1 = input("Enter the interest rate as a percentage: ")
    if string1.isdigit():
        rate = int(string1)
    else:
        print("<< Interest rate must be a number. >>")
years = 0
while years == 0:
    string1 = input("Enter the number of years: ")
    if string1.isdigit():
        years = int(string1)
    else:
        print("<< Years must be a number. >>")

# calculate the simple interest
simpleInt = (principal * rate * years) / 100

print("")
print("Simple interest is", simpleInt)

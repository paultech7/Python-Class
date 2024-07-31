
# Get the inputs for the calculation
principal = int(input("Enter the principal amount: "))
interest = int(input("Enter the interest as a percentage: "))
years = int(input("Enter the number of years: "))

simpleInt = (principal * interest * years) / 100

print("")
print("Simple interest is", simpleInt)

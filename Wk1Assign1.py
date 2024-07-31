
# Get the inputs for the calculation
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter the interest rate as a percentage: "))
years = int(input("Enter the number of years: "))

# calculate the interest
simpleInt = (principal * rate * years) / 100

print("")
print("Simple interest is", simpleInt)

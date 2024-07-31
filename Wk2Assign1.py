# Get the inputs for the calculation
weight = -1
height = -1.0
while weight < 0:
    weight = int(input("Enter the weight in kilograms: "))
while height < 0.0:
    height = float(input("Enter the height in meters: "))

# calculate the BMI and the category
BMI = weight / (height * height)
category = "normal"
if BMI >= 30.0:
    category = "obese"
elif BMI >= 25.0:
    category = "overweight"
elif BMI < 18.5:
    category = "underweight"

print("")
print("BMI =", BMI, "which is", category)

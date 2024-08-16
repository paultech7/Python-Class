# Get the starting integer
inputString = input("Enter a positive integer: ")

# Validate the input
number = 0
while number == 0:
    if inputString.isdigit():
        number = int(inputString)
        if number <= 0:
            inputString = input("Number must be a positive integer. Re-enter: ")
    else:
        inputString = input("Invalid entry. Please enter a positive integer: ")

# Calculate the Collatz sequence for the integer until it reaches 1.
seq = inputString
while number != 1:
    if number % 2 == 0:
        number //= 2
    else:
        number = number * 3 + 1
    seq += ", " + str(number)

# Show the resulting sequence
print("")
print("Collatz sequence is (" + seq + ")")

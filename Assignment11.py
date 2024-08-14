# Get the starting integer
string1 = input("Enter a positive integer: ")

# Validate the input
if string1.isdigit():
    number = int(string1)
    if number > 0:

        # Calculate the Collatz sequence for the integer until it reaches 1.
        seq = string1
        while number != 1:
            if number % 2 == 0:
                number /= 2
            else:
                number = number * 3 + 1
            seq += ", " + str(number)
        else:
            # Show the resulting sequence
            print("Collatz sequence is (" + seq + ")")

    else:
        print("Error: Please enter a positive integer.")
else:
    print("Error: Please enter a positive integer.")

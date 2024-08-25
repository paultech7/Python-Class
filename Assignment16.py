import math


# Define a function that tests if the passed integer is a prime.
# Returns: True if the number is prime; False if it is not.
def is_prime(pos_int):
    if pos_int <= 1:
        return False
    elif pos_int == 2:
        return True
    elif pos_int % 2 == 0:
        return False        # all even numbers > 2 are not prime
    else:
        # Since we now know the number is not divisible by 2,
        # we only need to test for division by odd numbers.
        for divisor in range(3, math.ceil(math.sqrt(pos_int)) + 1, 2):
            if pos_int % divisor == 0:
                return False
        else:
            return True


# Get a positive integer
string_in = input("Enter a positive integer: ")
while True:
    if string_in.isnumeric():
        numberIn = int(string_in)
        if numberIn > 0:
            break
        else:
            string_in = input("Error: number must be a positive integer. Re-enter: ")
    else:
        string_in = input("Error: number must be a positive integer. Re-enter: ")

# Test if the integer is a prime and show the result
if is_prime(numberIn):
    print("Number is prime.")
else:
    print("Number is NOT prime.")

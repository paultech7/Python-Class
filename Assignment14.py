# Define a function named power that takes two integers, base and exponent, as input.
# Returns:  base raised to the power of exponent.
def power(base, exponent):
    return base ** exponent


# Get the base and exponent
while True:
    base_input = input("Enter the base: ")
    if base_input.isnumeric() or (base_input[0] == '-' and base_input[1:].isnumeric()):
        base_arg = int(base_input)
        break
    else:
        print("Error: base must be an integer.")
while True:
    exp_input = input("Enter the exponent: ")
    if exp_input.isnumeric() or (exp_input[0] == '-' and exp_input[1:].isnumeric()):
        exp_arg = int(exp_input)
        break
    else:
        print("Error: exponent must be an integer.")

# Call the power function and show the result
print(f"Power = {power(base_arg, exp_arg):.2f}")

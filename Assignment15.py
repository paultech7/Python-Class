# Define a function to test whether a string is a palindrome.
# Implement the function in a way that uses recursion.
# Returns: True if the parameter is a palindrome, False otherwise
def is_palindrome(string_param):
    if len(string_param) <= 1:
        return True
    end_position = len(string_param) - 1
    if string_param[0] != string_param[end_position]:
        return False
    return is_palindrome(string_param[1:end_position])


# Get the string to test
string_in = input("Enter a string: ")

# Show the result
if is_palindrome(string_in):
    print(string_in, " is a palindrome.")
else:
    print(string_in, " is NOT a palindrome.")

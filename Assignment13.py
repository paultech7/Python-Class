# Get the string to test
string1 = input("Enter a string: ")

# Test if the string is a palindrome by looping from the beginning and end of the string and comparing characters
fromBegin = 0
fromEnd = len(string1) - 1
isPalindrome = True
while fromBegin < fromEnd:
    if string1[fromBegin] != string1[fromEnd]:
        isPalindrome = False
        break
    fromBegin += 1
    fromEnd -= 1

# Show the result
if isPalindrome:
    print("String is a palindrome")
else:
    print("String is not a palindrome")

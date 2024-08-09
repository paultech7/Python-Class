# Get the character to test
string1 = input("Enter a letter: ")

# Determine whether the character is a vowel or consonant, or the input is invalid
if len(string1) == 1 and string1.isalpha():
    letter = string1.lower()
    if letter in "aeiou":
        text = "'" + string1 + "' is a vowel."
    else:
        text = "'" + string1 + "' is a consonant."
else:
    text = "Error: The entry was not a single letter."

print(text)

# Get the character to test
string1 = input("Enter a letter: ")

# Determine whether the character is a vowel or consonant, or the input is invalid
if len(string1) == 1 and string1.isalpha():
    letter = string1.lower()
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        text = "'" + string1 + "' is a vowel."
    else:
        text = "'" + string1 + "' is a consonant."
else:
    text = "The entry was not a single letter. >>"

print("")
print(text)

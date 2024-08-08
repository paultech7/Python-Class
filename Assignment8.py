# Get the marks for the 3 subjects. Verify the marks are between 0 and 100.
mark1 = 0
mark2 = 0
mark3 = 0
markIsInvalid = True
while markIsInvalid:
    string1 = input("Enter the mark for subject 1: ")
    if string1.isdigit():
        mark1 = int(string1)
        if 0 <= mark1 <= 100:
            markIsInvalid = False
    if markIsInvalid:
        print("<< Please enter a number between 0 and 100. >>")

markIsInvalid = True
while markIsInvalid:
    string1 = input("Enter the mark for subject 2: ")
    if string1.isdigit():
        mark2 = int(string1)
        if 0 <= mark2 <= 100:
            markIsInvalid = False
    if markIsInvalid:
        print("<< Please enter a number between 0 and 100. >>")
markIsInvalid = True
while markIsInvalid:
    string1 = input("Enter the mark for subject 3: ")
    if string1.isdigit():
        mark3 = int(string1)
        if 0 <= mark3 <= 100:
            markIsInvalid = False
    if markIsInvalid:
        print("<< Please enter a number between 0 and 100. >>")

# Calculate the average mark
average = (mark1 + mark2 + mark3) / 3

# Assign the grade based on the average
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print("")
print("The grade is", grade)
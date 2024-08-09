# Get the marks for the 3 subjects.
string1 = input("Enter the mark for subject 1: ")
string2 = input("Enter the mark for subject 2: ")
string3 = input("Enter the mark for subject 3: ")

# Validate the inputs
if string1.isdigit():
    mark1 = int(string1)
else:
    mark1 = -1
if string2.isdigit():
    mark2 = int(string2)
else:
    mark2 = -1
if string3.isdigit():
    mark3 = int(string3)
else:
    mark3 = -1

if 0 <= mark1 <= 100 and 0 <= mark2 <= 100 and 0 <= mark3 <= 100:

    # Calculate the average mark and assign the grade
    average = (mark1 + mark2 + mark3) / 3
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

    # Show the result
    print("The grade is", grade)

else:
    print("Error: the marks must be positive integers between 0 and 100.")

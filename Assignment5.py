import math

# Get the hours to convert
hours = -1.0
while hours < 0:
    string1 = input("Enter hours: ")
    if (string1.isnumeric() or string1.replace(".", "", 1).isnumeric())\
            and float(string1) > 0:
        hours = float(string1)
    else:
        print("<< Hours must be a positive number. >>")

# calculate the equivalent minutes and seconds
totalSecs = hours * 3600
minutes = int(totalSecs / 60)
secs = int(totalSecs - (minutes * 60))

print("")
print(f"{hours} hours = {minutes} minutes : {secs} seconds")

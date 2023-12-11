# Mason England
# CS 1400 - MWF 8:30

#setup
print("Welcome to the fronkian calender")

year = input("    Enter a year: ")

digits = []

for i in year:
    digits.append(int(i))

# check if the year is a leap year
print("\n")
if int(year) % 9 == 0 and digits[2] != digits[3]:
    print(F"Thank you, the calendar has made a decision\n    {year} is a leap year!")
elif digits[2] % 2 == 0 and digits[2] < digits[3] and digits[2] + digits[3] == int(str(digits[0]) + str(digits[1])):
    print(F"Thank you, the calendar has made a decision\n    {year} is a leap year!")
else:
    print(F"Thank you, the calendar has made a decision\n    {year} is NOT a leap year")



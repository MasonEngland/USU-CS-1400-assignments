# Mason England
# CS1400 - 8:30

import math
print("Welcome!")
# prompt user for all the data
invest_amount = float(input("Enter an investment amount: $"))
monthly_payment = float(input("how much will you be paying each month?: $"))
annual_interest = float(input("what is your annual interest?(%): "))
number_of_years = float(input("how many years will you be investing?: "))
monthly_interest = (annual_interest / 12) / 100

# separate parts of equations
part1 = pow(1 + monthly_interest, number_of_years * 12)

part2 = (part1 - 1)/monthly_interest

# do the calculations
future_value = (invest_amount * (part1)) + (monthly_payment * part2 * (1 + monthly_interest))

# output calculations to the user
print(F"The Future amount of Money You will Have in {int(number_of_years)} years is: {round(future_value, 2)}")
# Problem 1 - Paying Debt off in a Year

# Write a program to calculate the credit card balance after one year
# if a person only pays the minimum monthly payment required by the credit card company each month.

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# monthlyPaymentRate - minimum monthly payment rate as a decimal

# So your program only prints out one thing:
# the remaining balance at the end of 12 months in the format:
# Remaining balance: 4784.0
# Be sure to print out no more than two decimal digits of accuracy

# A summary of the required math is found below:
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

monthlyInterestRate = annualInterestRate / 12.0

for month in range(1, 13):
    monthlyPayment = balance * (monthlyPaymentRate)
    unpaidBalance = balance - monthlyPayment
    balance = unpaidBalance + unpaidBalance*(monthlyInterestRate)       

print("Remaining balance: "+str(round(balance,2)))



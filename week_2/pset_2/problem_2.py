# Problem 2 - Paying Debt Off in a Year

# Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
# By a fixed monthly payment, we mean a single number which does not change each month,
# but instead is a constant amount that will be paid each month.

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

# The program should print out one line:
# the lowest monthly payment that will pay off all debt in under 1 year, for example:
# Lowest Payment: 180

# Assume that the interest is compounded monthly according to the balance at the end of the month
# (after the payment for that month is made).

# The monthly payment must be a multiple of $10 and is the same for all months.
# Notice that it is possible for the balance to become negative using this payment scheme, which is okay.

# A summary of the required math is found below:
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

def checker(balance,monthlyInterestRate,fixedMonthlyPayment):
    """
    checks if given fixedMonthlyPayment enables 0 balance at end on 12 months
    :return: True is condition satisfied, False otherwise
    """
    global found
    for month in range(1,13):
        unpaidBalance = balance - fixedMonthlyPayment
        balance = unpaidBalance + unpaidBalance*monthlyInterestRate
    if balance <= 0:
        found = True
        return found
    else:
        return found

#main
monthlyInterestRate = annualInterestRate / 12.0
fixedMonthlyPayment = 0

found = False
while not found :
    fixedMonthlyPayment+=10
    checker(balance,monthlyInterestRate,fixedMonthlyPayment)

print(fixedMonthlyPayment)


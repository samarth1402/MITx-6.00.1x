# Problem 3 - Using Bisection Search to Make the Program Faster

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

# To recap the problem:
# We are searching for the smallest monthly payment such that we can pay off the entire balance within a year.

# What is a reasonable lower bound for this payment value? $0 is the obvious anwer, but you can do better than that.
# If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the original balance,
# so we must pay at least this much every month.
# One-twelfth of the original balance is a good lower bound.

# What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year.
# What we ultimately pay must be greater than what we would've paid in monthly installments,
# because the interest was compounded on the balance we didn't pay off each month.
# So a good upper bound for the monthly payment would be one-twelfth of the balance,
# after having its interest compounded monthly for an entire year.

# In short:
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

# Write a program that uses these bounds and bisection search to find the smallest monthly payment to the cent
# such that we can pay off the debt within a year.

monthlyInterestRate = annualInterestRate / 12.0

low = balance / 12
high = (balance * (1 + annualInterestRate)**12 ) / 12


found = False
while not found :
    mid = (high + low) / 2
    fixedMonthlyPayment = round(mid, 2)
    remBalance = balance
    #loop to find remaining balance at the end of 12 months
    for month in range(1,13):
        unpaidBalance = remBalance - fixedMonthlyPayment
        remBalance = unpaidBalance + unpaidBalance*monthlyInterestRate
    #conditions on remaining balance
    if abs(remBalance) <= 0.1:              #0.1 is the expulsion value
        found = True
    elif remBalance > 0:
        low = mid + 0.01
    elif remBalance < 0:
        high = mid - 0.01

print(fixedMonthlyPayment)


#!/usr/bin/env python

'''
Paying off Credit Card Debt in a Year
Params: <outstanding_balance>, <monthly_interest_rate>
Return: <monthly_payment>, <remaining_balance>, <number_of_months>
Definition: Calculates the monthly payment (multiple of ten) needed to pay off an initial balance within at least 12 months, the number of months needed to pay off the debt, and the remaining balance after the payments (negative).
'''


def MonthlyPayment(outstanding_balance, monthly_interest_rate):
    monthly_payment = 0.0
    number_of_months = 0
    debt = True
    while debt:
        monthly_payment += 10
        remaining_balance = outstanding_balance
        for i in xrange(12):
            if remaining_balance > 0:
                remaining_balance *= (1.0 + monthly_interest_rate)
                remaining_balance -= monthly_payment
            else:
                number_of_months = i
                debt = False
                break


    return monthly_payment, remaining_balance, number_of_months


def main ():

    outstanding_balance = float(raw_input('Enter the outstanding balance on your credit card: '))
    annual_interest_rate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
    monthly_interest_rate = annual_interest_rate / 12

    monthly_payment, remaining_balance, number_of_months = MonthlyPayment(outstanding_balance, monthly_interest_rate)

    print "RESULT:"
    print "Monthly payment to pay off debt in 1 year: ", monthly_payment
    print "Balance: ", "{0:0.2f}".format(remaining_balance)
    print "Number of months needed: ", number_of_months




if __name__ == '__main__':
	main()

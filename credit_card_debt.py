#!/usr/bin/env python

'''
Credit Card Debt
Params: <param 1>, <pram 2>, ... <param n>
Return: <return value>
Definition: describe what the function is doing
'''


def MonthlyPayment(outstanding_balance, minimum_monthly_payment_rate):
	monthly_payment = outstanding_balance * minimum_monthly_payment_rate
	return monthly_payment

def PrinciplePaid(monthly_payment, monthly_interest_rate, outstanding_balance):
	interest_paid = outstanding_balance * monthly_interest_rate
	principle_paid = monthly_payment - interest_paid
	return principle_paid


def RemainingBalance(outstanding_balance, principle_paid):
	remaining_balance = outstanding_balance - principle_paid
	return remaining_balance


def monthly_ouput (monthly_payment, principle_paid, remaining_balance, outstanding_balance, minimum_monthly_payment_rate, monthly_interest_rate):
	
	index = 0
	while index < 12:
		print "{0:0.2f}".format(monthly_payment)
		print "{0:0.2f}".format(principle_paid)
		print "{0:0.2f}".format(remaining_balance)

		outstanding_balance = remaining_balance
		monthly_payment = MonthlyPayment(outstanding_balance, minimum_monthly_payment_rate)
		principle_paid = PrinciplePaid(monthly_payment, monthly_interest_rate, outstanding_balance)
		remaining_balance = RemainingBalance(outstanding_balance, principle_paid)

		index = index + 1
	



def main():
	outstanding_balance = float(raw_input('What is the outstanding balance on your credit card?'))

	annual_interest_rate = float(raw_input('What is the annual interest rate?'))

	minimum_monthly_payment_rate = float(raw_input('What is the monthly minimum percentage rate?'))

	monthly_interest_rate = annual_interest_rate / 12

	monthly_payment = MonthlyPayment(outstanding_balance, minimum_monthly_payment_rate)

	principle_paid = PrinciplePaid(monthly_payment, monthly_interest_rate, outstanding_balance)

	remaining_balance = RemainingBalance(outstanding_balance, principle_paid)

	monthly_ouput (monthly_payment, principle_paid, remaining_balance, outstanding_balance, minimum_monthly_payment_rate, monthly_interest_rate)






if __name__ == '__main__':
	main()


#!/usr/bin/env python

'''
Credit Card Debt
Params: <monthly_payment>, <principle_paid>, <remaining_balance>, <outstanding_balance>, <minimum_monthly_payment_rate>, <monthly_interest_rate>
Return: Monthly Payment, Principle Paid, Remaining Balance
Definition: Calculates minimum monthly payment, principle paid each month, and the remaining principle balance after that month's payment. At the end pf 12 months, it calculates the amount of principle paid off, and the amount of principle remaining. 
'''

#calculates minimum monthly payment on remaining balance
def MonthlyPayment(outstanding_balance, minimum_monthly_payment_rate):
	monthly_payment = outstanding_balance * minimum_monthly_payment_rate
	return monthly_payment

#calculates amount of each monthly payment that goes toward principle
def PrinciplePaid(monthly_payment, monthly_interest_rate, outstanding_balance):
	interest_paid = outstanding_balance * monthly_interest_rate
	principle_paid = monthly_payment - interest_paid
	return principle_paid


#calculates amount of principle remaining after monthly payment
def RemainingBalance(outstanding_balance, principle_paid):
	remaining_balance = outstanding_balance - principle_paid
	return remaining_balance


def MonthlyOutput(monthly_payment, principle_paid, remaining_balance, outstanding_balance, minimum_monthly_payment_rate, monthly_interest_rate):
	
	index = 0
	initial_balance = outstanding_balance
	
	while index < 12:
		print "Month: " + str(index + 1)
		print "> Minimum Monthly Payment: $" , str("{0:0.2f}".format(monthly_payment))
		print "> Minimum Monthly Payment: $" , str("{0:0.2f}".format(monthly_payment))
		print "> Principle Paid: $" , str("{0:0.2f}".format(principle_paid))
		print "> Remaining Balance: $" , str("{0:0.2f}".format(remaining_balance))

		outstanding_balance = remaining_balance
		monthly_payment = MonthlyPayment(outstanding_balance, minimum_monthly_payment_rate)
		principle_paid = PrinciplePaid(monthly_payment, monthly_interest_rate, outstanding_balance)
		remaining_balance = RemainingBalance(outstanding_balance, principle_paid)

		index = index + 1
		
	print "RESULT"
	print "> Total amount paid: $" , str("{0:0.2f}".format(initial_balance - remaining_balance))
	print "> Remaining balance: $" , str("{0:0.2f}".format(remaining_balance))
	



def main():
	outstanding_balance = float(raw_input('Enter the outstanding balance on your credit card:'))

	annual_interest_rate = float(raw_input('Enter the annual interest rate as a decimal:'))

	minimum_monthly_payment_rate = float(raw_input('Enter the minimum monthly payment rate as a decimal:'))

	monthly_interest_rate = annual_interest_rate / 12

	monthly_payment = MonthlyPayment(outstanding_balance, minimum_monthly_payment_rate)

	principle_paid = PrinciplePaid(monthly_payment, monthly_interest_rate, outstanding_balance)

	remaining_balance = RemainingBalance(outstanding_balance, principle_paid)

	MonthlyOutput(monthly_payment, principle_paid, remaining_balance, outstanding_balance, minimum_monthly_payment_rate, monthly_interest_rate)






if __name__ == '__main__':
	main()


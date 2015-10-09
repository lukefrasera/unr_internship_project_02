#!/usr/bin/env python

'''
Paying off Credit Card Debt in a Year
Params: 
Return: ?
Definition:  
'''



def RemainingBalance(outstanding_balance, monthly_interest_rate, monthly_payment):

	for index in range(0,12):
		outstanding_balance = outstanding_balance * (1 + monthly_interest_rate)
		remaining_balance = outstanding_balance - monthly_payment
	return remaining_balance
	
def MonthlyPayment (outstanding_balance, monthly_interest_rate):
	monthly_payment = 10.0
	remaining_balance = RemainingBalance(outstanding_balance, monthly_interest_rate, monthly_payment)
	if (remaining_balance > 0):	
		monthly_payment = monthly_payment + 10
		remaining_balance = RemainingBalance(outstanding_balance, monthly_interest_rate, monthly_payment)
	
	return monthly_payment 


def main ():

	outstanding_balance = float(raw_input('Enter the outstanding balance on your credit card: '))

	annual_interest_rate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))

	monthly_interest_rate = annual_interest_rate / 12
	
	print MonthlyPayment(outstanding_balance, monthly_interest_rate)
	
	




if __name__ == '__main__':
	main()

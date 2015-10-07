#!/usr/bin/env python

'''
Paying off Credit Card Debt in a Year
Params: 
Return: ?
Definition:  
'''

def CompoundInterest (outstanding_balance, monthly_interest_rate):
	
	principle = outstanding_balance
	for index in range(0,12):
		interest= outstanding_balance + (outstanding_balance * monthly_interest_rate)
		principal = interest
	
	return principle



def MonthlyPayment (outstanding_balance, monthly_interest_rate):
	total_balance = CompoundInterest(outstanding_balance, monthly_interest_rate)
	monthly_payment = total_balance/12
	return monthly_payment



def RemainingBalance(outstanding_balance, monthly_interest_rate, monthly_payment):

	for index in range(0,12):
		outstanding_balance = outstanding_balance * (1 + monthly_interest_rate)
		remaining_balance = outstanding_balance - monthly_payment
	return remaining_balance
	


def main ():

	outstanding_balance = float(raw_input('Enter the outstanding balance on your credit card: '))

	annual_interest_rate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))

	monthly_interest_rate = annual_interest_rate / 12

	monthly_payment = MonthlyPayment (outstanding_balance, monthly_interest_rate)

	print monthly_payment
	print RemainingBalance(outstanding_balance, monthly_interest_rate, monthly_payment)
	
	




if __name__ == '__main__':
	main()

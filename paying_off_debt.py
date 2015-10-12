#!/usr/bin/env python

'''
Paying off Credit Card Debt in a Year
Params: 
Return: ?
Definition:  
'''



def RemainingBalance(outstanding_balance, monthly_interest_rate, monthly_payment):
	
	remaining_balance = outstanding_balance
	
	for index in xrange(12):
		remaining_balance = remaining_balance * (1 + monthly_interest_rate)
		remaining_balance = remaining_balance - monthly_payment
		# print remaining_balance
		
	return remaining_balance
	
def MonthlyPayment(outstanding_balance, monthly_interest_rate):
	monthly_payment = 10.0
	remaining_balance = RemainingBalance(outstanding_balance, monthly_interest_rate, monthly_payment)
	while(remaining_balance > 0):	
		monthly_payment = monthly_payment + 10
		remaining_balance = RemainingBalance(outstanding_balance, monthly_interest_rate, monthly_payment)
	
	return monthly_payment
	
def PaymentTerm(remaining_balance, monthly_payment):
	
	if remaining_balance + monthly_payment < 0:
		print '11 months'
		
	elif remaining_balance + monthly_payment > 0:
		print '12 months'
	

def main ():

	outstanding_balance = float(raw_input('Enter the outstanding balance on your credit card: '))
	annual_interest_rate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
	monthly_interest_rate = annual_interest_rate / 12
	monthly_payment = MonthlyPayment(outstanding_balance, monthly_interest_rate)
	
	print monthly_payment
	print RemainingBalance(outstanding_balance, monthly_interest_rate, monthly_payment)

	
	




if __name__ == '__main__':
	main()

#!/usr/bin/env python

'''
Paying off debt in a year or less
'''


def FindMinimumPaymentOneYear(balance, interest):
    # Set default Monthly payment
    m_pay = 0
    number_months = 0
    debt = True

    # Find Minimum payment
    while debt:
        # check payment method
        m_pay += 10
        start_balance = balance
        for i in xrange(12):
            if start_balance > 0:
                start_balance *= 1 + interest
                start_balance -= m_pay
            else:
                number_months = i
                debt = False
                break
    return m_pay, number_months, start_balance



def main():
    balance = float(raw_input('Input Outstanding Balance:'))
    m_interest = float(raw_input('Input Annual Interest:'))/12.0

    # Find minimum payment and the number of months to pay off debt as as the remaining balance
    m_pay, number_months, remaining_balance = FindMinimumPaymentOneYear(balance, m_interest)

    print "Monthly payment to pay off debt in 1 year: ", m_pay
    print "Number of months needed: ", number_months
    print "Balance: {0:0.2f}".format(remaining_balance)


if __name__ == '__main__':
    main()
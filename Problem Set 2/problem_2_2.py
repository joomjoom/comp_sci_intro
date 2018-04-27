# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 22:35:42 2018

@author: Jumma
"""

def min_payment(balance, annualInterestRate, fixedPaymentRate=10):
    '''
    calculates minimum payment to pay off balance in 1 year
    min payment can only be a multiple of 10
    '''
    
    def remaining_balance(balance, annualInterestRate, fixedPaymentRate, month=12):
        '''
        calculates the remaining balance on debt after one year
        '''
        
        ubalance = balance - fixedPaymentRate
        newBalance = ubalance + (annualInterestRate/12) * ubalance
        
        return balance if month == 0 \
        else remaining_balance(newBalance, annualInterestRate, fixedPaymentRate, month-1)
    
    
    return fixedPaymentRate if remaining_balance(balance, annualInterestRate, fixedPaymentRate) <= 0\
    else min_payment(balance, annualInterestRate, fixedPaymentRate+10)

balance = 3926
annualInterestRate = .2 
print('Lowest Payment: ', min_payment(balance, annualInterestRate))
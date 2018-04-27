# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 22:46:00 2018

@author: Jumma
"""

def remaining_balance(balance, annualInterestRate, monthlyPaymentRate, month=12):
    '''
    calculates the remaining balance on debt after one year
    '''
    
    #ubalance = balance - monthlyPaymentRate*balance
    ubalance = balance - monthlyPaymentRate
    newBalance = ubalance + (annualInterestRate/12) * ubalance
    
    if month == 0:
        return balance
    else:
        return remaining_balance(newBalance, annualInterestRate, monthlyPaymentRate, month-1)

balance = 3926
annualInterestRate = .2 
monthlyPaymentRate = 1981
print('Remaining balance: ',round(remaining_balance(balance, annualInterestRate, monthlyPaymentRate), 2))
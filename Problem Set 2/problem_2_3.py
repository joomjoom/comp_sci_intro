# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 23:18:56 2018

@author: Jumma
"""

def min_payment(balance, annualInterestRate, lBound, uBound):
    '''
    calculates minimum payment to pay off balance in 1 year
    optimized to use bisection search to calculate down to the cent
    '''
    def remaining_balance(balance, annualInterestRate, rateGuess, month=12):
        '''
        calculates the remaining balance on debt after one year
        '''
        #rateGuess = (lBound + uBound) / 2
        ubalance = balance - rateGuess
        newBalance = ubalance + (annualInterestRate/12) * ubalance
        
        return balance if month == 0 \
        else remaining_balance(newBalance, annualInterestRate, rateGuess, month-1)
    
    bal = remaining_balance(balance, annualInterestRate, (lBound+uBound)/2)
    
    if abs(bal) <= .01:
        return (lBound + uBound) / 2
        #return (balance / 12) + ((balance * (1 + annualInterestRate / 12.0)**12) / 12.0)
    
    elif bal > .01:
        return min_payment(balance, annualInterestRate, (lBound + uBound) / 2, uBound)
        
    else:
        return min_payment(balance, annualInterestRate, lBound, (lBound + uBound) / 2)

balance = 999999
annualInterestRate = .18 
print('Lowest Payment: ', round(min_payment(balance, annualInterestRate, (balance / 12), ((balance * (1 + annualInterestRate / 12.0)**12) / 12.0)), 2))
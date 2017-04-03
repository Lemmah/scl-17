#!/usr/bin/env python
# encoding: utf-8

'''
We are making a loan calculator that calculates the amount repayable when a loan is from the inputs.

'''
'''amount = input('Enter the amount:\n')
time = input('Repayable after how many months:\n')
rate = input('The rate you wish to use per month in percentage:\n')
'''
def calculate_repayable(amount, rate, time):
    return amount + (amount*(rate/100)*(time/12))

print(calculate_interest(amount, rate, time))

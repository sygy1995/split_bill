# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 00:07:30 2022

@author: Yifan
"""

def split_meal_check(individual_price_list, shared_price, tip, discount, tax):
    party_size = len(individual_price_list)
    grand_total = sum(individual_price_list) + shared_price + tip  - discount + tax
    split_evenly = shared_price / party_size
    food_expense_list = [i+split_evenly for i in individual_price_list]
    total_food = sum(individual_price_list) + shared_price
    
    individual_price__individual_due = {}
    
    for i, individual_price in enumerate(individual_price_list):
        if individual_price not in individual_price__individual_due:
            individual_due = food_expense_list[i] / total_food * grand_total
            individual_price__individual_due[individual_price] = individual_due
    
    print("There are " + str(party_size) + " people in our group")
    print("Grand total is " + str(grand_total))
    for individual_price in individual_price__individual_due:
        print("If your individual order is " + str(individual_price) + " your total due is " + str(individual_price__individual_due[individual_price]))
        

individual_price_list = [16.99, 16.99, 16.99, 26.49, 27.49]
shared_price = 0
tip = 8.14
discount = 0
tax = 18.89
split_meal_check(individual_price_list, shared_price, tip, discount, tax)
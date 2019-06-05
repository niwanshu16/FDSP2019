# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:37:55 2019

@author: KIIT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


from apyori import apriori

dataset = pd.read_csv('Market_Basket_Optimisation.csv' , header = None)
dataset = dataset.replace(np.nan , 'None')
item_purchase = []
for i in range(0,7501):
    temp =[]
    for j in range(0,20):
        if dataset.values[i,j]!='None':
            temp.append(dataset.values[i,j])
    item_purchase.append(temp)
        
    
rules = apriori(item_purchase,min_support = 0.003 , min_confidence = 0.25 , min_lift = 4)
# This functions returns generator
results = list(rules)

for item in results:
    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
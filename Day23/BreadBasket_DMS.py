# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 14:49:30 2019

@author: KIIT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset =pd.read_csv('BreadBasket_DMS.csv')

# Dealine with None Value
dataset['Item'] = dataset['Item'].replace('NONE' , np.nan)
dataset['Item'].isnull().any(axis=0)
dataset = dataset.dropna()


#1. Draw the pie chart of top 15 selling items.

top_15 = dataset['Item'].value_counts().head(15)
top_15.index
explode = [0]*15
explode[0] = 0.05
plt.pie(top_15.values , labels = top_15.index , autopct = '%1.1f',explode = explode)

plt.savefig('savfig.jpg')

#2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
item_purchase=[]
dataset['Transaction'].max()
from apyori import apriori
for i in range(1,9684):    
    item_purchase.append(list(dataset['Item'][dataset['Transaction']==i]))
    
rules = apriori(item_purchase,min_support = 0.0025 , min_confidence = 0.2 , min_lift = 3)
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

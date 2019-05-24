# -*- coding: utf-8 -*-
"""
Created on Wed May 22 18:01:16 2019

@author: KIIT
"""

import pandas as pd

dataset = pd.read_json('usagov_bitly_data.json',lines = True)

dataset = dataset.fillna('Missing')
dataset = dataset.replace('','Unknown')

frequent_tz = dataset['tz'].value_counts().head(10)
country = list(frequent_tz.index)
value = list(frequent_tz.values)
frequency_tz = dataset['tz'].value_counts()

plt.bar(country,value )
plt.xticks(rotation=90)
plt.show()

# From field a extract url 

list1 = dataset['a']
list_ver=[]
for i in list1:
    x = i.split('(')
    list_ver.append(x[0])
    
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 08:35:10 2019

@author: KIIT
"""

# Automobile 

import pandas as pd

dataset = pd.read_csv('Automobile.csv')

dataset[dataset['price'].isnull()]

dataset['price'] = dataset['price'].fillna(round(dataset['price'].mean()))

price = dataset['price'].values

price_min = price.min()
price_max = price.max()
price_mean = price.mean()
price_std = price.std()
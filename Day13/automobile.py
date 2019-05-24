# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:00:44 2019

@author: KIIT
"""

# Automobile.csv file

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('Automobile.csv')

value = dataset['make'].value_counts()
explode = [0]*10
explode[0]=0.2
plt.pie(value.values[0:10],labels = value.index[:10],explode = explode,autopct="%2.2f%%")
plt.show()
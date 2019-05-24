# -*- coding: utf-8 -*-
"""
Created on Fri May 24 10:03:15 2019

@author: KIIT
"""

# IGN analysis
import pandas as pd

dataset = pd.read_csv('ign.csv')

# Task-1
score_df = dataset[(dataset['score'] > 7 ) & (dataset['platform']=='Xbox One')]

# Task - 2

# Review distribution for xbox one

review_Xbox_one = dataset['score_phrase'][(dataset['platform']=='Xbox One')]
review_playstation4 = dataset['score_phrase'][(dataset['platform']=='PlayStation 4')]
review_Xbox_one.hist(bins = 20,grid = False,xrot = 90)
review_playstation4.hist(bins = 20,grid = False,xrot = 90)
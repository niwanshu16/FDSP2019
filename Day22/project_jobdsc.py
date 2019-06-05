# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:08:00 2019

@author: KIIT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('monster_com-job_sample.csv')

# Data Preprocessing

dataset['country'].value_counts()

dataset_tr = dataset.iloc[:,5:]


# String Matching 
dataset_tr = dataset_tr.dropna(subset = ['organization'])


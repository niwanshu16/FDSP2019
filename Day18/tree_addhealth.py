# -*- coding: utf-8 -*-
"""
Created on Wed May 29 18:14:37 2019

@author: KIIT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('tree_addhealth.csv')

from sklearn.preprocessing import Imputer
imputer = Imputer(strategy='mean')
imputer.fit(dataset)
X = imputer.transform(dataset)
dataset = pd.DataFrame(X, columns = dataset.columns)

dataset.isnull().any(axis=0)

features = dataset.iloc[:,[0,1,2,3,4,5,6,8,9,10,11,12,13,14,15]].values
labels = dataset.iloc[:,7:8].values
from sklearn.preprocessing import OneHotEncoder
for i in range(13):
    if i ==6:
        continue
    else:
        onehotencoder = OneHotEncoder(categorical_features=[i])
        features = onehotencoder.fit_transform(features).toarray()
        features = features[:,1:]
    
    

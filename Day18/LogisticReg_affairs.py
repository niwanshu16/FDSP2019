# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:58:11 2019

@author: KIIT
"""
# Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importing the dataset
dataset = pd.read_csv('affairs.csv')
features = dataset.iloc[:,0:8].values
labels = dataset.iloc[:,8].values
# Label Encoder
# Occupation_husband
from sklearn.preprocessing import OneHotEncoder
ohc1 = OneHotEncoder(categorical_features=[7])
features = ohc1.fit_transform(features).toarray()
features = features[:,1:]

# Occupation

ohc2 = OneHotEncoder(categorical_features= [10])
features = ohc2.fit_transform(features).toarray()
features = features[:,1:]

# Apply Standard scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features = sc.fit_transform(features)

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size =0.2,random_state=0)
# Implementing a Logistic Regression

from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(features_train,labels_train)

predict = log_reg.predict(features_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test,predict)

'''
    Predict the probability of an affair for a random
    woman not present in the dataset. She's a 25-year-old teacher 
    who graduated college, has been married for 3 years, has 1 child, 
    rates herself as strongly religious, rates her marriage as fair, and her 
    husband is a farmer.
'''

j = np.array([3,25,3,1,4,16,4,2]).reshape(1,-1)
j= ohc1.transform(j).toarray()
j = j[:,1:]
# Occupation
j = ohc2.transform(j).toarray()
j=j[:,1:]
j = sc.transform(j)
ans = log_reg.predict(j)
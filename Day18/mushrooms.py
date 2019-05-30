# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:20:42 2019

@author: KIIT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('mushrooms.csv')
features = dataset.iloc[:,[5,21,22]].values
labels = dataset.iloc[:,0].values

dataset['odor'].value_counts()

from sklearn.preprocessing import LabelEncoder , OneHotEncoder
encoder = LabelEncoder()
features[:,0] = encoder.fit_transform(features[:,0])
features[:,1] = encoder.fit_transform(features[:,1])
features[:,2] = encoder.fit_transform(features[:,2])
labels = labels.reshape(-1,1)
labels = encoder.fit_transform(labels)

ohc1 = OneHotEncoder(categorical_features=[0])
features = ohc1.fit_transform(features).toarray()
features = features[:,1:]


ohc1 = OneHotEncoder(categorical_features=[8])
features = ohc1.fit_transform(features).toarray()
features = features[:,1:]


ohc1 = OneHotEncoder(categorical_features=[13])
features = ohc1.fit_transform(features).toarray()
features = features[:,1:]

ohc1 = OneHotEncoder(categorical_features=[0])
labels = ohc1.fit_transform(labels).toarray()
labels = labels[:,1:]
# Splitting the dataset
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size = 0.2,random_state = 0)

# Applying Logistic Regression

from sklearn.linear_model import LogisticRegression
lin_reg = LogisticRegression()
lin_reg.fit(features_train,labels_train)

predict = lin_reg.predict(features_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test,predict)

success_rate = (cm[0][0] + cm[1][1])/cm.sum()*100
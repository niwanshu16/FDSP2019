# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:28:54 2019

@author: KIIT
"""

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
ohc = OneHotEncoder(categorical_features=[7])
features = ohc.fit_transform(features).toarray()
features = features[:,1:]

# Occupation
ohc = OneHotEncoder(categorical_features= [10])
features = ohc.fit_transform(features).toarray()
features = features[:,1:]

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size =0.2,random_state=0)

# Apply Standard scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features = sc.fit_transform(features)

# Implementing a KNearestNeighbour

from sklearn.neighbors import KNeighborsRegressor
knn_reg = KNeighborsRegressor(n_neighbors=3,p=2)
knn_reg.fit(features_train,labels_train)

predict = log_reg.predict(features_test)
predict = (predict>0.5)
from sklearn.metrics import confusion_matrix
cm_kneighbours1 = confusion_matrix(labels_test,predict)

ans = knn_reg.predict(j)

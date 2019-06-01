# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 17:01:44 2019

@author: KIIT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('IRIS.csv')

features = dataset.iloc[:,1:-1].values
labels = dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(features,labels , test_size = 0.2 , random_state = 0)


from sklearn.svm import SVC
svc = SVC(kernel ='linear',random_state = 0)
svc.fit(X_train,y_train)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,svc.predict(X_test))
confusion_matrix(y_train,svc.predict(X_train))

svc.score(X_test,y_test)


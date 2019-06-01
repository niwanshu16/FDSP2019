# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:46:42 2019

@author: KIIT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Download Dataset
dataset = pd.read_csv('breast_cancer.csv')
'''
Clump Thickness (1 – 10)                                     
Uniformity of Cell Size(1 - 10)                            
Uniformity of Cell Shape (1 - 10)                        
Marginal Adhesion (1 - 10)                                  
Single Epithelial Cell Size (1 - 10)                       
Bare Nuclei (1 - 10)                                              
Bland Chromatin (1 - 10)                                  
Normal Nucleoli (1 - 10)                                      
Mitoses (1 - 10)
'''
columns = ['ID Number','Clump Thickness (1 – 10)',
           'Uniformity of Cell Size(1 - 10)','Uniformity of Cell Shape (1 - 10)',                     
'Marginal Adhesion (1 - 10)',                                
'Single Epithelial Cell Size (1 - 10)',                       
'Bare Nuclei (1 - 10)',                              
'Bland Chromatin (1 - 10)',                             
'Normal Nucleoli (1 - 10)','Mitoses (1 - 10)','Class: (2 for Benign and 4 for Malignant)']

#columns = np.array(columns).reshape(1,-1)
dataset.columns = columns

dataset['Class'] = np.where(dataset['Class: (2 for Benign and 4 for Malignant)']==2 ,0,1)

dataset.isnull().any(axis=0)
dataset['Bare Nuclei (1 - 10)'] = dataset['Bare Nuclei (1 - 10)'].replace(np.nan,dataset['Bare Nuclei (1 - 10)'].mean())


data = dataset.iloc[:,1:]

# Split into features and labels
features = data.iloc[:,:-1].values
labels = data.iloc[:,-1].values

# Split into training and test data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(features,labels,test_size = 0.2,random_state=0)

from sklearn.svm import SVC
svc = SVC(kernel='linear' , random_state=0,degree = 3)
svc.fit(X_train,y_train)

from sklearn.metrics import confusion_matrix
svc_cm = confusion_matrix(y_test,svc.predict(X_test))
svc_cm_train = confusion_matrix(y_train,svc.predict(X_train))
svc.score(X_test,y_test)

# 2nd split
from sklearn.model_selection import StratifiedKFold
from sklearn.base import clone


clone_result = []
skfolds = StratifiedKFold(n_splits = 3 , random_state =0)
for train_index,test_index in skfolds.split(X_train,y_train):
    clone_clf = clone(svc)
    X_train_folds = X_train[train_index]
    y_train_folds = y_train[train_index]
    X_test_folds = X_train[test_index]
    y_test_folds = y_train[test_index]
    
    clone_clf.fit(X_train_folds,y_train_folds)
    y_pred_clone = clone_clf.predict(X_test_folds)
    n_correct = sum(y_pred_clone==y_test_folds)
    clone_result.append(n_correct/len(y_pred_clone))

cm_clone = confusion_matrix(y_test_folds,y_pred_clone)

# Naive Byes is not good in this case
from sklearn.naive_bayes import  BernoulliNB 

bnb = BernoulliNB()
bnb.fit(X_train,y_train)

cm_bnb = confusion_matrix(y_test,bnb.predict(X_test))
bnb.score(X_test,y_test)




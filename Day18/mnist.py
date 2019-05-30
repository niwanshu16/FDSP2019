# -*- coding: utf-8 -*-
"""
Created on Thu May 30 07:11:55 2019

@author: KIIT
"""
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from sklearn.datasets import fetch_openml
data = fetch_openml('mnist_784',version =1 , cache = True)
mnist = data['data']
data['target']

X,y = mnist,data['target']
X.shape
y.shape


# Some Data visualization

some_digit = X[36000]
some_digit_image = some_digit.reshape(28,28)
# Interpolation is used when the small image is scale up
plt.imshow(some_digit_image, cmap = matplotlib.cm.binary,interpolation = 'nearest')
plt.axis('off')
plt.show()

y[36000]


# Create test set and training set
'''
In MNIST first 60000 is training set and 10000 is test set

Some dataset perform poor when they get some similar instances in a row
So, we have to shuffle the indexex to avoid this scenario

Shuffling may be poor for some dataset like timestamp and weather condition related 
data but not in this case
'''
X_train,X_test,y_train,y_test = X[:60000],X[60000:],y[:60000],y[60000:]
shuffle_index = np.random.permutation(60000)
X_train,y_train = X_train[shuffle_index],y_train[shuffle_index]


'''
TRAINING A BINARY CLASSIFIER using SGDClassifier
'''

from sklearn.linear_model import SGDClassifier

# True for 9 Else False
y_train_9 = (y_train=='9')
y_test_9 = (y_test =='9')
y_train_1 =(y_train=='1')
# Training of SGD classifier
sgd_clf = SGDClassifier(random_state=0)
sgd_clf.fit(X_train,y_train_9)

# Another Example
sgd_clf.fit(X_train,y_train_1)
some_digit = X_train[3000]
sgd_clf.predict([some_digit])


# Evaluate using Cross Validation

from sklearn.model_selection import StratifiedKFold
'''
This cross-validation object is a variation of KFold that returns stratified folds.
The folds are made by preserving the percentage of samples for each class
'''
from sklearn.base import clone

skfolds = StratifiedKFold(n_splits=3,random_state=0)
for train_index,test_index in skfolds.split(X_train,y_train_9):
    clone_clf = clone(sgd_clf)
    X_train_folds = X_train[train_index]
    y_train_folds = (y_train_9[train_index])
    X_test_folds = X_train[test_index]
    y_test_fold = (y_train_9[test_index])
    # Divide into training and test set
    
    clone_clf.fit(X_train_folds,y_train_folds)
    y_pred = clone_clf.predict(X_test_folds)
    n_correct = sum(y_pred == y_test_fold)
    print(n_correct/len(y_pred))
    
from sklearn.model_selection import cross_val_score
# Parameters(estimator object,features,target variable, kfolds cv=2 (k=2),)
cross_val_score(sgd_clf , X_train,y_train_9 ,cv=3 , scoring='accuracy')

# These two methods are used to evaluate your performance































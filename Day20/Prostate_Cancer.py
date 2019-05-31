# -*- coding: utf-8 -*-
"""
Created on Fri May 31 15:44:40 2019

@author: KIIT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
(1) Train the unregularized model (linear regressor) and calculate the mean squared error.
(2) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

(b) Can we predict whether lpsa is high or low, from other variables?


'''
dataset = pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat" , delimiter = ' ')

corr_matrix = dataset.corr()
corr_matrix['lpsa'].sort_values(ascending = False)
dataset.isnull().any(axis=0)
features = dataset.iloc[:,0:-1].values
labels = dataset.iloc[:,-1].values

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
features = scaler.fit_transform(features)

# Train Test Split

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(features,labels,test_size = 0.2,random_state = 0)

# Apply linear regression
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_train,y_train)

predict = lin_reg.predict(X_test)

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(predict,y_test)
rmse = np.sqrt(mse)

mean_lpsa = dataset['lpsa'].mean()

# Regularization

from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

lin_lasso = Lasso()
lin_ridge = Ridge()

lin_ridge.fit(X_train,y_train)
predict_ridge = lin_ridge.predict(X_test)

mse_ridge = mean_squared_error(predict_ridge,y_test)
rmse_ridge = np.sqrt(mse_ridge)

lin_lasso.fit(X_train,y_train)
predict_lasso = lin_lasso.predict(X_test)

mse_lasso = mean_squared_error(predict_lasso,y_test)
rmse_lasso = np.sqrt(mse_lasso)

print('rmse {} \n rmse_Ridge {} \n rmse_lasso {} '.format(rmse,rmse_ridge,rmse_lasso))
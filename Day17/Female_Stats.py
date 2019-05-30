# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:41:45 2019

@author: KIIT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('Female_Stats.csv')
# Independent Variable , Dependent Variable
x = dataset.iloc[:,1:].values
y = dataset.iloc[:,0:1].values

# Splitting into test and training data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 0)

# Preprocessing Technique
plt.scatter(dataset.iloc[:,0:1],dataset.iloc[:,1:2])
plt.scatter(dataset.iloc[:,0:1],dataset.iloc[:,2:3])
dataset.hist(bins=20,figsize = (20,15))
dataset.isnull().any(axis=0)

# Check whose influence is more 

import statsmodels.api as sm
x_train = sm.add_constant(x_train)
x_train_opt = x_train[:,[0,1,2]]
lin_reg1 = sm.OLS(endog = y_train,exog = x_train_opt).fit()
lin_reg1.summary()
lin_reg1.pvalues


x_train_opt = x_train_opt[:,[1,2]]
lin_reg1 = sm.OLS(endog = y_train,exog = x_train_opt).fit()
lin_reg1.summary()
lin_reg1.pvalues

from sklearn.linear_model import LinearRegression
lin_reg2 = LinearRegression()
lin_reg2.fit(x_train,y_train)
predict = lin_reg2.predict(x_test)

mean_difference1 = abs(predict.mean() - y_test.mean())
"""
Result array([1.96391438e-14, 3.41764808e-19])
"""
# Father height influenced more


#Father Height is constant

# Increasing one inch in mother's height

dataset['momheight'] = dataset['momheight'] + 1

# Independent Variable , Dependent Variable
x = dataset.iloc[:,1:].values
y = dataset.iloc[:,0:1].values

lin_reg3 = LinearRegression()
lin_reg3.fit(x,y)
predict = lin_reg3.predict(x)
mean_difference2 = abs(predict.mean() - y.mean())
# Mother Height is constant

# Increasing one inch in Father's height

dataset = pd.read_csv('Female_Stats.csv')
dataset['dadheight'] = dataset['dadheight']+1

# Independent Variable , Dependent Variable
x = dataset.iloc[:,1:].values
y = dataset.iloc[:,0:1].values

import statsmodels.api as sm
x_train = sm.add_constant(x_train)
x_train_opt = x_train[:,[0,1,2]]
lin_reg1 = sm.OLS(endog = y_train,exog = x_train_opt).fit()
lin_reg1.summary()
lin_reg1.pvalues


x_train_opt = x_train[:,[1,2]]
lin_reg1 = sm.OLS(endog = y_train,exog = x_train_opt).fit()
lin_reg1.summary()
lin_reg1.pvalues

lin_reg4 = LinearRegression()
lin_reg4.fit(x,y)
predict = lin_reg4.predict(x)
mean_difference3 = abs(predict.mean() - y.mean())

'''
array([5.41502381e-14, 2.17219611e-19])
'''
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:33:06 2019

@author: KIIT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('iq_size.csv')

# Split into features and labels
features = dataset.iloc[:,1:].values
labels = dataset.iloc[:,0:1].values

plt.scatter(features[:,2],labels)

# Apply Multiple LR

from sklearn.linear_model import LinearRegression
lin_reg1 = LinearRegression()
lin_reg1.fit(features,labels)

j = np.array([90,70,150]).reshape(1,3)
predict = lin_reg1.predict(j)

features_opt = sm.add_constant(features)

features_opt = features_opt[:,[0,1,2,3]]
import statsmodels.api as sm
lin_reg2 = sm.OLS(endog = labels, exog = features_opt).fit()
lin_reg2.summary()


features_opt = features_opt[:,[0,1,2]]
lin_reg2 = sm.OLS(endog = labels, exog = features_opt).fit()
lin_reg2.summary()


features_opt = features_opt[:,[1,2]]
lin_reg2 = sm.OLS(endog = labels, exog = features_opt).fit()
lin_reg2.summary()

features_opt = features_opt[:,[1]]
lin_reg2 = sm.OLS(endog = labels, exog = features_opt).fit()
lin_reg2.summary()

# Prediction on the basis of brain size
lin_reg1.fit(features[:,0:1],labels)
m = np.array([90]).reshape(1,-1)
predict1 = lin_reg1.predict(m)


# Looping through p values
features_opt = features_opt[:,[0,1,2,3]]
import statsmodels.api as sm
while true:
    lin_reg2 = sm.OLS(endog = labels, exog = features_opt).fit()
    p_value = lin_reg2.pvalues
    

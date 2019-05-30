# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:10:26 2019

@author: KIIT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import Dataset

dataset = pd.read_csv('bluegills.csv')

dataset['age'].value_counts()
x = dataset.iloc[:,0:1].values
y = dataset.iloc[:,1:].values
plt.scatter(x,y)



from sklearn.linear_model import LinearRegression
linear_reg = LinearRegression()
linear_reg.fit(x,y)

j = np.array([5])
j = j.reshape(1,-1)
predict = linear_reg.predict(j)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 5)
x_poly = poly_reg.fit_transform(x)

linear_reg1 = LinearRegression()
linear_reg1.fit(x_poly,y)
predict1 = linear_reg1.predict(poly_reg.transform(j))
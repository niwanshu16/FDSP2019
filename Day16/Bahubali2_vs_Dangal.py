# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:02:39 2019

@author: KIIT
"""

# Box Office prediction 

# Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')
dataset.isnull().any(axis = 0)

# Data is already preprocessed

x = dataset.iloc[:,0:1].values
y_Bahubali = dataset.iloc[:,1:2].values
y_Dangal = dataset.iloc[:,-1:].values

# Regressor for bahubali
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x,y_Bahubali)

# Regression for Dangal
regressor1 = LinearRegression()
regressor1.fit(x,y_Dangal)


# Visualizing the Bahubali
plt.scatter(x,y_Bahubali,color = 'red')
plt.plot(x,regressor.predict(x),color='blue')
plt.xlabel("Days")
plt.ylabel("Profit(Bahubali)")
plt.title("Training Visualization")
plt.show()

# Visualizing the dangal
plt.scatter(x,y_Dangal,color = 'red')
plt.plot(x,regressor.predict(x),color='blue')
plt.xlabel("Days")
plt.ylabel("Profit(Dangal)")
plt.title("Training Visualization")
plt.show()

# Finding profir for 10th day
day = np.array([10,11,12,13,14,15])
day = day.reshape(6,-1)
Bahubali_10 = regressor.predict(day)
Dangal_10 = regressor1.predict(day)

df = pd.DataFrame({'Bahubali':Bahubali_10.reshape(6,),'Dangal':Dangal_10.reshape(6,)})
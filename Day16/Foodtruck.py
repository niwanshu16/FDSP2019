# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:21:06 2019

@author: KIIT
"""

# Importing the Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading the csv file

dataset = pd.read_csv('Foodtruck.csv')
X = dataset.iloc[:,0:1].values# Independent variable
Y = dataset.iloc[:,-1:].values

dataset.dtypes

dataset.hist(bins=20)


# Tocheck Null values
dataset.isnull().any(axis=0)

# No need to preprocess data

# Divide the data into training and test set

# Traing Set --> X_train(features),Y_train(Label)
# Test Set --> X_test(features),Y_test(Label--Predicting Values)
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,random_state = 0)



from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,Y_train)

predict = regressor.predict(X_test)

df = pd.DataFrame({"Actual": Y_test,"Predict":predict})

# Visualizing the training data
plt.scatter(X_train,Y_train,color = 'blue',label='Training')
plt.plot(X_train,regressor.predict(X_train),color='red')
plt.xlabel("Population")
plt.ylabel("Profit")
plt.title("Training Visualization")
plt.legend()
plt.show()

# Visualizing the Test Data
plt.scatter(X_test,Y_test,color='blue',label = 'Prediction')
plt.plot(X_test,predict,color='red')
plt.xlabel('Population')
plt.ylabel('Profit')
plt.title("Test Visulaization")
plt.legend()
plt.show()

j = np.array([4.56,4.67])
# We Have to reshape the array
j = j.reshape(2,-1)
ex = regressor.predict(j)
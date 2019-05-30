# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:28:30 2019

@author: KIIT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

cols=["mpg", "cylinders", "displacement",
    "horsepower","weight","acceleration", "model year", "origin", 
    "car name"]
dataset = pd.read_csv('Auto_mpg.txt' , delimiter =r'\s+' , header = None)
dataset.columns = cols

# Handling the ? value
value=dataset['horsepower'].value_counts().head(1)
real=list(value.index)
dataset['horsepower']=dataset['horsepower'].replace('?',real[0])
dataset["horsepower"] = np.array(dataset["horsepower"], dtype = np.float_)



features = dataset.iloc[:,1:]
labels = dataset.iloc[:,0].values
features = features.iloc[:,:-1].values


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(features,labels,test_size = 0.2,random_state=0)

from sklearn.tree import DecisionTreeRegressor
tree_reg = DecisionTreeRegressor()
tree_reg.fit(X_train,y_train)
predict = tree_reg.predict(X_test)

# Error

from sklearn.metrics import mean_squared_error
tree_mse = mean_squared_error(y_test,predict)
tree_rmse = np.sqrt(tree_mse)


'''
 Find out the MPG value of a 80's model car of origin 3, weighing
     2630 kgs with 6 cylinders, having acceleration around 22.2 m/s 
     due to it's 100 horsepower engine giving it a displacement of about 
     215. (Give the prediction from both the models)
'''
example = np.array([6,215,100,2630,22.2,80,3]).reshape(1,-1)
example_tree = tree_reg.predict(example)


# Random Forest Regressor

from sklearn.ensemble import RandomForestRegressor
forest_reg = RandomForestRegressor(n_estimators= 20,random_state=0)
forest_reg.fit(X_train,y_train)
predict_forest = forest_reg.predict(X_test)

forest_mse = mean_squared_error(y_test,predict_forest)
forest_rmse = np.sqrt(forest_mse)

example_forest = forest_reg.predict(example)




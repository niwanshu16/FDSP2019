# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:19:51 2019

@author: KIIT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
dataset = pd.read_csv('kc_house_data.csv')

def f(x):
    return int(x[0:4])

dataset['date']  = dataset['date'].map(f)
dataset['sqft_above']=dataset['sqft_above'].replace(np.nan,dataset['sqft_above'].mean())

corr_matrix = dataset.corr()
corr_matrix['price'].sort_values(ascending = False)

dataset.isnull().any(axis=0)

features = dataset.drop('price',axis = 1).values
labels = dataset['price'].values

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
features = scaler.fit_transform(features)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(features,labels,test_size = 0.2,random_state = 0)

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_train,y_train)
predict_reg = lin_reg.predict(X_test)

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test,predict_reg)
rmse = np.sqrt(mse)


# Regularization

from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
lin_lasso = Lasso()
lin_ridge = Ridge()
lin_net = ElasticNet()

lin_ridge.fit(X_train,y_train)
predict_ridge = lin_ridge.predict(X_test)

mse_ridge = mean_squared_error(predict_ridge,y_test)
rmse_ridge = np.sqrt(mse_ridge)

lin_lasso.fit(X_train,y_train)
predict_lasso = lin_lasso.predict(X_test)

mse_lasso = mean_squared_error(predict_lasso,y_test)
rmse_lasso = np.sqrt(mse_lasso)

lin_net.fit(X_train,y_train)
predict_net = lin_net.predict(X_test)

mse_net = mean_squared_error(predict_net,y_test)
rmse_net = np.sqrt(mse_net)

print('rmse {} \n rmse_Ridge {} \n rmse_lasso {} \n rmse_net {}'.format(rmse,rmse_ridge,rmse_lasso,rmse_net))



from sklearn.tree import DecisionTreeRegressor

tree_reg = DecisionTreeRegressor()
tree_reg.fit(X_train,y_train)
predict_tree = tree_reg.predict(X_test)

mse_tree = mean_squared_error(y_test,predict_tree)
rmse_tree = np.sqrt(mse_tree)


from sklearn.ensemble import RandomForestRegressor
forest_reg = RandomForestRegressor(n_estimators=20 , random_state=0)
forest_reg.fit(X_train,y_train)
predict_forest = forest_reg.predict(X_test)

mse_forest = mean_squared_error(y_test,predict_forest)
rmse_forest = np.sqrt(mse_forest)


# Applying Back elimination

features_opt = features[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]]

import statsmodels.api as sm
lin_reg2 = sm.OLS(endog = labels , exog = features_opt).fit()
lin_reg2.summary()

features_opt = features[:,[0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19]]

import statsmodels.api as sm
lin_reg2 = sm.OLS(endog = labels , exog = features_opt).fit()
lin_reg2.summary()

features_opt = features[:,[0,1,2,3,4,5,7,8,9,10,11,13,14,15,16,17,18,19]]

import statsmodels.api as sm
lin_reg2 = sm.OLS(endog = labels , exog = features_opt).fit()
lin_reg2.summary()

features_opt = features[:,[0,1,2,3,4,7,8,9,10,11,13,14,15,16,17,18,19]]

import statsmodels.api as sm
lin_reg2 = sm.OLS(endog = labels , exog = features_opt).fit()
lin_reg2.summary()

features_opt = features[:,[1,2,3,4,7,8,9,10,11,13,14,15,16,17,18,19]]

import statsmodels.api as sm
lin_reg2 = sm.OLS(endog = labels , exog = features_opt).fit()
lin_reg2.summary()

features_opt = features[:,[1,2,3,4,7,8,9,10,11,13,14,15,16,17,18]]

import statsmodels.api as sm
lin_reg2 = sm.OLS(endog = labels , exog = features_opt).fit()
lin_reg2.summary()


from sklearn.model_selection import train_test_split
X_train_ols,X_test_ols,y_train_ols,y_test_ols = train_test_split(features_opt,labels,test_size = 0.2,random_state = 0)

forest_reg_ols = RandomForestRegressor(n_estimators = 20,random_state =0)
forest_reg_ols.fit(X_train_ols,y_train_ols)
predict_forest_ols = forest_reg_ols.predict(X_test_ols)

mean_forest_ols = mean_squared_error(y_test_ols,predict_forest_ols)
rmse_forest_ols = np.sqrt(mean_forest_ols)
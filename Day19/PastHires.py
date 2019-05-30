# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:23:35 2019

@author: KIIT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('PastHires.csv')
features = dataset.iloc[:,0:-1].values
labels = dataset.iloc[:,-1].values


from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
features[:,1] = encoder.fit_transform(features[:,1])
features[:,3] = encoder.fit_transform(features[:,3])
features[:,4] = encoder.fit_transform(features[:,4])
features[:,5] = encoder.fit_transform(features[:,5])

features = np.array(features , dtype=np.int_)
d = {"BS":0,"MS":1,"PhD":2}
dataset["Level of Education"] = dataset["Level of Education"].map(d)

from sklearn.tree import DecisionTreeClassifier
tree_clf = DecisionTreeClassifier()
tree_clf.fit(features,labels)

'''
Predict employment of a currently employed 10-year veteran, 
    previous employers 4, went to top-tire school, having Bachelor's 
    Degree without Internship.
    Predict employment of an unemployed 10-year veteran, 
    ,previous employers 4, didn't went to any top-tire school, 
    having Master's Degree with Internship.
'''
random = np.array([10,1,4,1,0,1]).reshape(1,-1)
predict_tree = tree_clf.predict(random)



from sklearn.ensemble import RandomForestClassifier
random_clf = RandomForestClassifier(n_estimators=10,random_state=0)
random_clf.fit(features,labels)
predict_forest = random_clf.predict(random)
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:17:05 2019

@author: KIIT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('tshirts.csv')
features = dataset.iloc[:,[1,2]].values

plt.scatter(features[:,0] , features[:,1])

# How to choose how many clusters to used 

# 1st Method
#WCSS : within cluster sum of squares
from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init = 'k-means++',random_state=0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,11) , wcss)
plt.title('Elbow Method')

# Using silhouette coefficient
from sklearn.metrics import silhouette_score
for i in range(2,11):
    clusterer = KMeans(n_clusters=i)
    pred = clusterer.fit_predict(features)
    centers = clusterer.cluster_centers_
    
    score = silhouette_score(features,pred,metric='euclidean')
    print("For n_clusters =", i,
          "The average silhouette_score is :", score)


# So 2 clusters is quite good 
kmeans = KMeans(n_clusters=3,init = 'k-means++',random_state=0)
pred_cluster = kmeans.fit_predict(features)

# Visualize 
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Cluster 3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:19:35 2019

@author: KIIT
"""

# frequency of a child name 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.DataFrame()
for i in range(1880,2011):
    file_name = 'yob'+str(i)+'.txt'
    dataset = pd.read_csv(file_name,header=None)
    dataset.columns = ["Name","Gender","Count"]
    dataset["Year"] = i
    df= pd.concat([df,dataset])

# Display the top 5 names of boy and girl in 2010
boy_name = df["Name"][(df['Year']==2010) & (df['Gender']=='M')].head()
girl_name = df["Name"][(df["Year"]==2010) & (df['Gender']=='F')].head()
df[(df["Year"]==2010)&(df["Gender"]=="M")].head(5)

#  Calculate sum of the births column by sex as the total number of births 
 #   in that year(use pandas pivot_table method)

#table = pivot_table(df,values=['Gender','Count'],)
girl = []
boy = []
year=[]
for i in range(1880,2011):
    boy_birth = df['Count'][(df['Gender']=='M') &(df['Year']==i)].sum()
    girl_birth = df['Count'][(df['Gender']=='F') & (df['Year']==i)].sum() 
    girl.append(girl_birth)
    boy.append(boy_birth)
    year.append(i)
    
# New Dataset for boy girl and year
    
new_dataset = pd.DataFrame(columns=['Boy','Girl','Year'])
new_dataset['Boy']=boy
new_dataset['Girl']=girl
new_dataset['Year'] = year
new_csv = new_dataset.to_csv('new_csv.csv')
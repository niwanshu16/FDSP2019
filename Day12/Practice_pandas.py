# -*- coding: utf-8 -*-
"""
Created on Thu May 23 07:52:27 2019

@author: KIIT
"""

# Practising Pandas


# Creating an empty series

s = pd.Series()

list1 = ['Sentence1','Sentence2','Sentence3']
s = pd.Series(list1)
print(type(s))

# Customized index

s = pd.Series(list1,index=[100,101,102])

# Retrieving the element
s[0]
s[:3]
s[-3:]
s[::-1]

# Creating an empty dataframe

df = pd.DataFrame()


# Creating a dataframe with dictionary

df = pd.DataFrame({'one':pd.Series([1,2,3,4]),'two':pd.Series([4,5,6,7,8])})

# Creating by two list

list1 = [['Alex',20],['Bob',21],['Yen',20]]
df = pd.DataFrame(list1,columns=['Name','Age'])

# Dataframe with Dictionary
d = {'one':pd.Series([1,2,3],index = ['a','b','c']),
    'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df = pd.DataFrame(d)
df['one']
df['two']

print(df.iloc[1])

# Loading a csv file

import pandas as pd

dataset = pd.read_csv('Salaries.csv')

# Dataset information

dataset.info()

# Number of dimensions

dataset.ndim

# Return a tuple representing a dimension

dataset.shape

# Number of elements
dataset.size # 78*6

# Given index
dataset.index

# List first 5 records

dataset.head()
dataset.head(10)

# List last 5 records

dataset.tail()
dataset.tail(10)

# Giving the index
dataset.index

# Columns 

dataset.columns

# Giving both index and columns
dataset.axes

# Numpy representation of the values

dataset.values

#**** Gives the statistical value for every column ****
dataset.describe()

# In order to include particular columns

dataset.describe(include=['object','bool','int64'])


#return max/min values for each value
dataset.max()
dataset['salary'].max()
dataset.min()
dataset['salary'].min()

# Return mean/std/median values for all numeric values

dataset['salary'].mean()
dataset.median()
dataset.std()

# Mean of the first/last 50 values

dataset.head(50).mean()
dataset.tail(50).mean()


# Return the random 5 values

dataset.sample(5).mean().index[2]
type(dataset.sample(5).mean())


# DataFrame method loc[:,:]
# Index comma separated row,column

df = dataset.iloc[:,0:3]

# Separate the particulart column and rows using loc method using column name
df = dataset.loc[10:20,['rank','sex','salary']]

# If we want to add the rows and column 

df = dataset.iloc[:2,:]
# 21 inclusive in loc
dataset.loc[10:21]
# 21 exclusive
df = dataset.iloc[10:21,0:4]

# Selecting a column with all rows 

# Using loc

dataset.loc[:,['rank']]

# Using iloc

dataset.iloc[:,1:3]


# Select column rank and salary

dataset[['rank','salary']]


# Find unique values 

df['rank'].unique()
dataset['salary'].unique()

# How to change in a list

list1 = dataset['rank'].value_counts().to_list

# To show in percentage

dataset['rank'].value_counts(normalize= True)

# Find values in a column which are not nulll

dataset['salary'].count()
# Calculate all values including null

dataset['salary'].value_counts(dropna=True)

# Calculate the number of males 

dataset[dataset['sex']=='Male']

# Salary of males 

dataset['salary'][dataset['sex']=='Male']


# Find those rows which have null value

dataset[dataset['salary'].isnull()]
dataset['salary'].isnull()

# Using groupby
df = dataset.groupby(['rank'])
df = list(df.groups['AssocProf'])


# Filter using multiple columns

df_sub = dataset[(dataset['salary']>12000) &
                 (dataset['sex']=='Female')]



#****Handling the missing values

dataset[dataset['phd'].isnull()]
dataset[dataset['salary'].isnull()]

dataset.isnull()

# Select the rows that have atleast one nan

dataset[dataset.isnull().any(axis=0)]

# One way to drop all nun values 

new_dataset = dataset.dropna()
# Not a good way

# Second method to fill a hardcode value 

new1_dataset = dataset.fillna(1)
# Not a precise way 


# Fill all the missing values by mean of hat column

new2_dataset = dataset.fillna(round(dataset.mean()))
dataset[dataset['salary'].isnull()]

dataset['salary']=dataset['salary'].fillna(dataset['salary'].mean())


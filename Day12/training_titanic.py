# -*- coding: utf-8 -*-
"""
Created on Fri May 24 07:29:18 2019

@author: KIIT
"""

# Importing a file
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Reading a csv file
dataset = pd.read_csv('training_titanic.csv')

# How many survived the disaster
dataset['Survived'].value_counts()
survive = dataset['Survived'].value_counts()[1]

# How many died
total_died = dataset['Survived'].value_counts()[0]

# Print the survival rate in proportion

total_died_percent = dataset['Survived'].value_counts(normalize = True)[0]
total_survive_percent = dataset['Survived'].value_counts(normalize = True)[1]

# Males that survive vs males that passed away

males_survive = dataset['Survived'][(dataset['Sex']=="male")].value_counts()
female_survive = dataset['Survived'][(dataset['Sex']=="female")].value_counts()

# Creating a new column where age<18 = 1 

# Handling the missing values in age column

dataset['Age'] = dataset['Age'].fillna(round(dataset['Age'].mean()))

dataset['child'] = dataset['Age'].map(lambda x: 1 if x<18 else 0 )

# age<18 --> child, survived==1

child_survive = dataset['Survived'][(dataset['child'])==1].value_counts()[1]
child_dead = dataset['Survived'][(dataset['child'])==1].value_counts()[0]

child_survive_percent = dataset['Survived'][(dataset['child'])==1].value_counts(normalize = True)[1]
child_dead_percent =  dataset['Survived'][(dataset['child'])==1].value_counts(normalize = True)[0]

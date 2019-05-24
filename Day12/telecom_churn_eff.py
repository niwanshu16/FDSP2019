# -*- coding: utf-8 -*-
"""
Created on Fri May 24 08:47:49 2019

@author: KIIT
"""

# Telecom Churn effective way

import pandas as pd

# import contextlib to handle exceptions
import contextlib as clb

# importing the dataset
with clb.suppress((FileNotFoundError)):
    churn_df = pd.read_csv('telecom_churn.csv')
    
    # Filtering the churned customer ( Task-1)
    
    churned_df = churn_df[churn_df['churn']==True]
    
    # Count of churned customer availing both voice and international plan
    
    plans_count = churned_df[(churned_df['voice mail plan']=='yes')&(churned_df['international plan']=='yes')].shape
    plans_count = plans_count[0]
    
    # Task-2 Charges for international customer
    
    call_charge = churn_df.groupby('churn')['total intl charge'].sum()
    visual1 = call_charge.plot.pie(autopct='%1.1f%%')
    
    # Task-3 State having highest night call minutes
    
    night_call = churned_df['total night minutes'].max()
    
    # Task-4 Call analysis
    
    call_analysis = churned_df.iloc[:,7:19].sum().sort_index()
    visual2 = call_analysis.plot.bar()
    minimum_call_type = call_analysis.min()
    
    # Task-5 
    non_churn = churn_df['account length'][(churn_df['churn']==False)].max()
    churn = churn_df['account length'][(churn_df['churn']==True)].max()
    
    if churn>non_churn:
        print('Churn customer having highest account length')
    else:
        print('Non Churn customer having highest account length')
    
    
    # Task-5 
    
    customer_care = churn_df.groupby('churn')['customer service calls'].sum()
    customer_care_values = churned_df['customer service calls'].value_counts()
    visual3 = customer_care_values.plot.bar()
    
    # Task-6
    
    area1 = churn_df.groupby('area code')['international plan'].value_counts().unstack()
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:24:38 2019

@author: KIIT
"""

"""
encoding by sublime to load dataset


"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Telecom_churn.csv')

df['international plan']=df['international plan'].map(lambda x: 1 if x =='yes' else 0)
df['voice mail plan']=df['voice mail plan'].map(lambda x: 1 if x =='yes' else 0)
df['churn']=df['churn'].map(lambda x: 1 if x is True else 0)
count = df[(df['international plan']==1) & (df['voice mail plan']==1) &(df['churn']==1)]

churned_customer = df[df['churn']==1]

# Total charges for churned customer
churn_charge = sum(churned_customer['total intl charge'])
non_churn_charge = sum(df['total intl charge'])- churn_charge

l =[churn_charge,non_churn_charge]
label =['churn_charge','non_churn_charge']

plt.pie(l,labels = label ,explode =[0.2,0],autopct='%1.2f%%')
plt.show()


# Having highest total night charge and that state

df1 = churned_customer['state'][churned_customer['total night charge']==churned_customer['total night charge'].max()]

voice_mail = churned_customer['voice mail plan'].value_counts()
international_plan = churned_customer['international plan'].value_counts()

voice_mail_plan = voice_mail[1]
international = international_plan[1]

label=['voice_mail_plan','international']
list1 = [voice_mail_plan,international]

plt.pie(list1,labels = label , explode=[0.2,0] , autopct='%1.2f%%')
plt.show()
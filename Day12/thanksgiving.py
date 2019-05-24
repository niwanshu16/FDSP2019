# -*- coding: utf-8 -*-
"""
Created on Thu May 23 10:53:45 2019

@author: KIIT
"""

# Thanks Giving problem

import pandas as pd

dataset = pd.read_csv('thanksgiving.csv',encoding = 'Windows-1252')

'''Discover regional and income-based patterns in what Americans eat for 
    Thanksgiving dinner'''
    
dataset.info()
# Empty dataset
data = pd.DataFrame()

l = ['ID','celebrate?','MainDish_Dinner','MainDish_Dinner_others',
              'Cooked_main','cooked_main_others','Stuffing/dressing',
              'stuffing/dressing_others','cranberry_saucedo',
              'cranberry_saucedo_others','Having_gravy',
              'TS_BrusselSprouts','Typically_served_Carrots',
              'TS_cauliflower','TS_Corn','TS_Cornbread','TS_Fruit_SAlad',
              'TS_Green_beans','TS_macaroni','TS_MashedPotatoes',
              'TS_Rolls','TS_Squash','TS_VegetableSalad','TS_yams','TS_others',
              'TS_others_1','TS_Apple','TS_Buttermilk','TS_Cherry','TS_Chocolate',
              'TS_coconutcream','TS_keylime','TS_peach','TS_pecan','TS_pumpkin',
              'TS_sweetpotato','TS_none','TS_pie_others','TS_pie_others_1',
              'TS_AppleCobbler','TS_Blondies','TS_Brownies','TS_CarrotCake',
              'TS_CheeseCake','TS_Cookies','TS_Fudge','TS_IceCream',
              'TS_PeachCobbler','TS_Dessert_None','TS_Dessert_others',
              'TS_Dessert_others1','Pray_afterMeal','Travel',
              'Programs_MacyParade','AgeCutOff','HometownFriends?',
              'FriendsGiving','BlackFridaySale','Work_Retail','Emp_BlackFriday',
              'Address','Age','Gender','CombinedMoney','USRegion']


dataset = dataset.iloc[:,:]
data[l]=dataset.iloc[:,0:]




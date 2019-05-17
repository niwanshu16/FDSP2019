# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:26:29 2019

@author: KIIT
"""
# Check for positive and pallindromic 

def fx(x):
    x = str(x)
    y = x[::-1]
    return int(x)>0 and y==x


#t = list(filter(fx,[12, 9 ,61, 5, 14]))
 #t = list(map(lambda x:True if str(x)==str(x)[::-1] else False ,[12, 9 ,61, 5, 14]))
# Using List Comprehension and any
any([str(x)==str(x)[::-1] for x in [12, 9 ,61, 5, 14]])



# Random choice 
import random

def fx(names):
    code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
    for i in range(len(names)):
        names[i]=random.choice(code_names)
    return names
    
    
names = ['Mary', 'Isla', 'Sam']
fx(names)
list(map(fx,names))
 
# One line code for assigning name
list(map(lambda x:random.choice(code_names),names))
    
# Hash function
list(map(lambda x:hash(x),names))


# Calculate Average height
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

def fx(people):
    for i in range(len(people)):
        return people[i]['height']

def fx(people):
    return 'height' in people
    
    
people = list(filter(fx,people))
people1=list(map(lambda x: x['height'],people))
import functools
def fx1(a,b) :
    return a+b
    
a=functools.reduce(fx,people1)


"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop1.py
  Problem Statement:
    Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:
        
    Order Number  Book Title  Author Quantity  Price per Item
    34587 Learning Python, Mark Lutz  4 40.95
    98762 Programming Python, Mark Lutz 5 56.80
    77226 Head First Python, Paul Barry 3 32.95
    88112 Einführung in Python3, Bernd Klein  3 24.99    
    
    Write a Python program, You need to write a solution without using lambda,map,list comprehension first and then with lambda,map,reduce
    
    A) which returns Order Summary as a list with 2-tuples. 
       Each tuple consists of the order number and the product of the price per items 
       and the quantity. 
    
       The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.

  Hint: 
    Write a Python program using lambda and map.

"""

summary =[list(map(int,input().split())) for i in range(4)]


summary =[[34587, 'Learning Python','Mark Lutz',4, 40.95],
    [98762, 'Programming Python', 'Mark Lutz',5 ,56.80],
    [77226, 'Head First Python', 'Paul Barry',3, 32.95],
    [88112 ,'Einführung in Python3', 'Bernd Klein',3,24.99 ]]
s=()
list2 = []
list(map(lambda x: (x[0],x[3],x[3]*x[4]) if x[3]*x[4]>=100 else (x[0],x[3],x[3]*x[4]+10),summary))
    


# Population.csv
import csv
l=[]
dict1={}
with open('population.csv','r') as fp:
    csv_reader = csv.reader(fp)
    next(csv_reader)
    for i in csv_reader:
        l.append(i)
from collections import Counter
for i in l:
    i[2]=i[2].replace(',','')
    if i[3] in dict1:
        dict1[i[3]] +=int(i[2])
    else:
        dict1[i[3]] = int(i[2])
        
        
        
        

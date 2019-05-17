# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:05:43 2019

@author: KIIT
 4  
    4.000
    -1.00
    +4.54
"""

# Regex1.py
import re
l =['4','4.000','-1.00','+4.54','657','.4']
for i in l:
    if re.search(r'[+-.]{1}[0-9]',i):
        print('True')
    else:
        print('False')



# Regex2.py
valid_mail = ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com','2321','niwanshu16@gmail.com']
for i in valid_mail:
    if not re.search(r'^[a-zA-Z0-9_-]+@[a-z0-9]+\.[a-z]{2,4}$',i):
        valid_mail.remove(i)
print(sorted(valid_mail))

# Regex3.py
"""

    It must start with a '4', '5' or ' 6'.
    It must contain exactly 16 digits
    It must only consist of digits (0-9)
    It may have digits in groups of 4, separated by one hyphen "-"
    It must NOT use any other separator like ', ' , '_', etc
    It must NOT have 4 or more consecutive repeated digits
   (r'^[456]{1}+[0-9]{3}\-[0-9]{4}\-[0-9]{4}\-[0-9]{4}'
   
   card_no.replace('-','')
   
   patt=re.match()
   conse=re.search(r'(\d)\1{3,}',replace('-',''))
   
   if patt and not conse:
       print
    """



    
for i in range(int(input())):
    s = input()
    if re.search(r'^[a-zA-Z0-9_-]+@[a-z0-9]+\.[a-z]{2,4}$',s):
        print('Valid')
    else:
        print('Not Valid')



# regex5.py
        

with open('simpsons_phone_book.txt','r') as fp:
    s=fp.readlines()
#print(s)
for i in s:
    if re.match(r'J.* Neu',i):
        print(i)
        
        

        
        
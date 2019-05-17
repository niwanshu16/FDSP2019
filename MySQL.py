# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:59:04 2019

@author: KIIT
"""

import os
import sqlite3
from pandas import DataFrame

import mysql.connector

conn = mysql.connector.connect(user = 'niwanshu293', password ='458f5e30',
                               host = 'db4free.net',database = 'niwanshu293')


# Create a cursor

c = conn.cursor()

c.execute("""CREATE TABLE student(
          roll_no INTEGER,
          name TEXT,
          age INTEGER,
          branch TEXT
          )""")

c.execute("""INSERT INTO student VALUES (51,'Niwanshu',20,'CSE')""")
c.execute("""INSERT INTO student VALUES (52,'Nitesh',20,'CSE')""")
c.execute("""INSERT INTO student VALUES (53,'nidhi',20,'CSE')""")
c.execute("""INSERT INTO student VALUES (54,'Neha',20,'CSE')""")
c.execute("""INSERT INTO student VALUES (51,'Rajesh',20,'CSE')""")
c.execute("""INSERT INTO student VALUES (51,'Ram',20,'CSE')""")
c.execute("""INSERT INTO student VALUES (51,'Farah',20,'CSE')""")
c.execute("SELECT * from student ")

print(c.fetchmany(2))

from pandas import DataFrame

df = DataFrame(c.fetchall())



# Bid Data transfer into df4freenet
conn = mysql.connector.connect(user = 'niwanshu293', password ='458f5e30',
                               host = 'db4free.net',database = 'niwanshu293')

c = conn.cursor()

c.execute("""CREATE TABLE BidData(
        bidid TEXT,
        item TEXT,
        DeptName TEXT,
        Quantity TEXT,
        StartDate TEXT,
        EndDate TEXT
        )""")
for i in range(len(A)):
    c.execute("INSERT INTO BidData VALUES('{}','{}','{}','{}','{}','{}')".format(A[i],B[i],C[i],D[i],E[i],F[i]))
A

c.execute("SELECT * from BidData")
df = DataFrame(c.fetchall())
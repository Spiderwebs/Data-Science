# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 04:03:48 2018

@author: Spiderwebs
"""

import cx_Oracle

with open('GEODATASOURCE-COUNTRY.TXT') as f:
    content = f.readlines()
    
contList = []

for rows in content:
    row = rows.split(sep='\t')
    contList.append(row)

for x in range(0,len(contList)):
    contList[x][-1] = contList[x][-1][0:-1]


con = cx_Oracle.connect('Spiderwebs/9137@localhost:1521')

cur=con.cursor()

cur.executemany("INSERT INTO COUNTRIES VALUES(:1,:2,:3,:4)",contList[1:][:])

con.commit ()

cur.close()
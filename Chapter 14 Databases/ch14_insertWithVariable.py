# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:17:10 2019

@author: maggie
"""
import  sqlite3
import time
import datetime
import random

#ex1 create a table

conn = sqlite3.connect("task1b.db")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToBuild2(unix REAL , datestamp TEXT, keyword TEXT, value REAL)")
    
#def data_entry():
#    c.execute("INSERT INTO stuffToBuild2 VALUES(142233222, '2018-01-01', 'python', 5)")
#    conn.commit()
#    c.close()
#    conn.close()

#ex2 add data to your table with variables

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime("%Y-%m-%d %H:%M:%S"))
    keyword = "Python"
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToBuild2(unix, datestamp, keyword, value) VALUES(?, ?, ?, ?)", (unix, date, keyword, value))
    conn.commit()
    
create_table()    
    
for i in range(10):
    dynamic_data_entry()
    time.sleep(1)


#ex3  read and select data from a database
    
#def read_from_db_all():
#    c.execute("SELECT * FROM stuffToBuild2 WHERE value =8 ")
#    for row in c.fetchall():
#        print(row)
#        
#read_from_db_all()
       
def read_from_db2():
    c.execute("SELECT * FROM stuffToBuild2 WHERE value =8 and unix > 1547029131 and unix < 1547029134 ")
    for row in c.fetchall():
        print(row[0])
        
read_from_db2()

#data_entry()
c.close()
conn.close()

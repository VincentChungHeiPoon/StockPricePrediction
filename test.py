# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 23:41:27 2019

@author: boy19
"""

from utils import DataCollection
import pandas as pd
import numpy as np
import re

#data = DataCollection.save_data_as_csv() 

class RepeatedCol:
    def __init__(self, name, count):
        self.name = name
        self.count = count

data_df = pd.read_csv('Dataset/Data.csv')

temp = data_df

temp = temp.drop(1, axis = 0)

new_col_name = temp.columns.values
new_col_name[0] = 'Date'

temp.columns = new_col_name


#temp2 = temp['Adj Close'].append(temp['Adj Close.1'])

a = []
count = 1
for i in range(len(new_col_name)):
    
    current_col = new_col_name[i].split('.')[0]
    if(i < len(new_col_name) - 1):
        next_col = new_col_name[i + 1].split('.')[0]
        if(current_col == next_col):
            count = count + 1
        else:
            a.append(RepeatedCol(current_col, count))
            count = 1
    else:
        next_col = new_col_name[i - 1].split('.')[0]
        if(current_col == next_col):
            a.append(RepeatedCol(current_col, count))
        else:
            a.append(RepeatedCol(current_col, 1))

count = 0           
for item in a:
    print(item.name)
    for i in range(item.count - 1):
        print()
        #temp[] = temp[item.name].append(temp[new_col_name[count + i + 1]])
    count = count + item.count

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 23:41:27 2019

@author: boy19
"""

from utils import DataCollection
import pandas as pd


#data = DataCollection.save_data_as_csv() 

data_df = pd.read_csv('Dataset/Data.csv')

temp = data_df.T.melt(id_vars = ['0'])
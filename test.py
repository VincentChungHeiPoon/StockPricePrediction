# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 23:41:27 2019

@author: boy19
"""

from utils import DataCollection
from utils import DataFormat
import pandas as pd
import numpy as np
import re

#data = DataCollection.save_data_as_csv() 

#temp = DataFormat.formatYahooData(DataCollection.get_stock_data())

#DataCollection.save_data_as_csv()
a = DataCollection.get_stock_name('StockList.txt')

for item in a:
    print(item.name)
    print(item.symbol)
#df = DataFormat.format_yahoo_data(pd.read_csv('Dataset/data.csv'))


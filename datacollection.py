# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 22:13:39 2019

@author: boy19
"""
import yfinance as yf
import pandas as pd
import os
import re


class DataCollection:
    #list of stock that will be collected
    #read from file
            
    def get_stock_list_string():
        stock_string = ''
        start_date = ''
        end_date = ''
        try:
            file = open('TrackingStock.txt', 'r')
            print('List of tracking stocks are')
            
            #first line in file is start date
            start_date = file.readline().strip('\n')
            #second line in file is end date
            end_date = file.readline().strip('\n')
            for line in file:
                stock = line.strip('\n')
                print(stock)    
                stock_string = stock_string + ' ' + stock
            file.close()
            return start_date, end_date, stock_string
        except:
            print('Error at setting parameter')
            
    def get_stock_data():
        start_date, end_date, stock_list_string = DataCollection.get_stock_list_string()
        return yf.download(stock_list_string, start=start_date, end=end_date)        
    
    def save_data_as_csv():
        data = DataCollection.get_stock_data()
        #path might be differnt from computer to computer, so we will use OS path to get the right path on each device
        data.to_csv(path_or_buf  = os.path.join(os.path.dirname(os.path.realpath(__file__)),'Dataset\data.csv'))

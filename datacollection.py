# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 22:13:39 2019

@author: boy19
"""
import yfinance as yf

class DataCollection:
    #list of stock that will be collected
    #read from file
    stock_string = ''
    def __init__(self) :
        try:
            file = open('TrackingStock.txt', 'r')
            print('List of tracking stocks are')
            for line in file:
                stock = line.strip('\n')
                print(stock)    
                self.stock_string = self.stock_string + ' ' + stock
        except:
            print('Error at open TrackingStock.txt')
            
    def get_stock_data(self, start_date, end_date):
        return yf.download(self.stock_string, start=start_date, end=end_date)        


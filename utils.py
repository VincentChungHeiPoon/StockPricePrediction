# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 22:13:39 2019

@author: Vincent Poon
"""
import yfinance as yf
import pandas as pd
import os
import re

class SymbolNamePair:
    
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name
        

class DataCollection:
    #list of stock that will be collected
    #read from file
    
    #get parameter for get_stock_data()
    def __get_stock_list_string(filename):
        stock_string = ''
        start_date = ''
        end_date = ''
        try:
            file = open(filename, 'r')
            print('List of tracking stocks are')
            
            #first line in file is start date
            #index 1 is element 2 in the splited string
            #eg start day = 2019-12-10 after split produce ['start day', '2019-12-10']
            start_date = file.readline().strip('\n').split(' = ')[1]
            #second line in file is end date
            end_date = file.readline().strip('\n').split(' = ')[1]
            for line in file:
                stock = line.strip('\n').split(' = ')[1]     
                print(stock)    
                stock_string = stock_string + ' ' + stock
            file.close()
            return start_date, end_date, stock_string
        except:
            print('Error at setting parameter')
            
    def __get_stock_data(filename):
        start_date, end_date, stock_list_string = DataCollection.__get_stock_list_string(filename)
        return yf.download(stock_list_string, start=start_date, end=end_date)        
    
    #return list of name of tracking stocks in alias, GOOGL returns google
    def get_stock_name(filename):
        pair = []
        file = open(filename, 'r')
        #skipping over first 2 line
        file.readline()
        file.readline()
        for line in file:
            #appending company name
            split = line.strip('\n').split(' = ')        
            #position as in .txt
            pair.append(SymbolNamePair(symbol = split[1], name = split[0]))

        return pair
    #save data as a csv, please use a text file as input
    #default input file = 'StockList.txt', default output file will be named 'Data.csv'
    def save_data_as_csv(filename = "StockList.txt", targetFileName = 'Data.csv'):
        data = DataCollection.__get_stock_data(filename)
        loc = 'Dataset/' + targetFileName
        #path might be differnt from computer to computer, so we will use OS path to get the right path on each device
        data.to_csv(path_or_buf  = os.path.join(os.path.dirname(os.path.realpath(__file__)),loc))

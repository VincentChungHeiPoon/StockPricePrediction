# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 22:13:39 2019

@author: Vincent Poon
"""
import yfinance as yf
import pandas as pd
import os

class SymbolNamePair:
    
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name

class RepeatedCol:
    def __init__(self, name, count):
        self.name = name
        self.count = count        

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
        
class DataFormat:
    #function that returns a formatted version of the Yahoo data for easy process
    def format_yahoo_data(df):        
        #dropping date row (mostly nan)
        df.drop(1, axis = 0, inplace = True)
        #set Data as a column name istead of in the dropped row
        new_col_name = df.columns.values
        new_col_name[0] = 'Date'
        
        df.columns = new_col_name
        
        #row 0 contains all company name
        company_list = pd.Series(list(dict.fromkeys(df.iloc[0])))
        #drop na as the first one is data, company name nan
        company_list.dropna(inplace = True)
        
        new_df = pd.DataFrame()
        date_df = pd.Series()
        df.drop(0, axis = 0, inplace = True)
        for i in range(len(company_list)):
            date_df = date_df.append(df['Date'])
        new_df['Date'] = list(date_df)
        
        #appending company name       
        comp_df = pd.Series()
        for i in range(len(company_list)):
            comp_df = comp_df.append(pd.Series([company_list.iloc[i]] * len(df)))
        new_df['Company'] = list(comp_df)
        
        df.drop('Date', axis = 1, inplace = True)
        
        #appending the 6 featues
        for i in range(0, len(df.columns),len(company_list)):
            feat_df = pd.Series()
            for j in range(len(company_list)):
                feat_df = feat_df.append(df[df.columns[i + j]])
            new_df[df.columns[i]] = list(feat_df)
        
        return new_df

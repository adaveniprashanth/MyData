#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 21:14:41 2020

@author: pj
"""
#For reference --> https://pandas.pydata.org/docs/reference/index.html
#For reference --> https://pandas.pydata.org/pandas-docs/version/1.3.5/
import numpy as np
import pandas as pd
from pandasql import sqldf
import matplotlib.pyplot as plt
import re
# print(np.array([[1,2],[3,4]],dtype=np.float32).dtype)
if 1:#Series -->pd.Series(data,dtype,index)
    
    if 0: #1-D data -->pd.Series(data,dtype)
        series = pd.Series(dtype=np.int64)#defining dtype to avoid warning
        # print(series)
        
        series = pd.Series([1,2,3])
        # print(series)
        
        series = pd.Series([1,2.3])#upcasting
        # print(series)
        
        series = pd.Series([1,2],dtype=np.float32)# manual casting
        # print(series)
        
        series = pd.Series([[1,2],[3,4]]) # not an array it is like each one as object having [1,2]  and [3,4]
        # print(series)
        # print(series[0])
    
        # print(pd.Series(np.arange(30))) #1-D array pass
        # print(pd.Series(np.arange(30).reshape(5,6)))#2-D array fails
    # print(len([chr(97 +i) for i in range(26)]))
    # print(np.arange(26).shape)
    if 0:#Index -->pd.Series(data,index)
        series = pd.Series([1,2,3],index=['a','b','c'])
        # print(series) #we can use any hashable as index
        
        series = pd.Series(np.arange(26),index=[chr(97 +i) 
                                                for i in range(26)])
        # print(series) #we can use any hashable as index
        
        series = pd.Series([1,2,3],index=[1,'b',2.3])
        # print(series) #each individaul index element called as label i.e. 1, 'b',2.3
        
    if 0:#Dictionary input pd.Series(dictionary)
        d= {'a':1,'b':2,'c':3}
        series = pd.Series(d)
        # print(series)
        
        d= {'b':1,'a':2,'c':3}#key:value -->key as index(row), value as data
        series = pd.Series({'b':1,'a':2,'c':3})
        # print(series)
        
        # print(pd.Series([1,2,3],name='r3'))
    if 0:
        s1 = pd.Series([1,3,5.2])
        s2 = s1 *[0.1,0.2,0.3]
        s3 = pd.Series([1,3,8,np.nan],index=['a','b','c','d'],name='c1')
        s4 = pd.Series({'a':0,'b':1,'c':2})
        print(s1)
        print(s2)
        print(s3)
        print(s4)
        
if 1:#DataFrame -->pd.DataFrame(data,index,columns)
    
    if 0:#2-D data
        df=pd.DataFrame() 
        # print(df)
        
        df=pd.DataFrame([5,6]) #2 rows 1 column i.e. column matrix
        # print(df)
        
        df=pd.DataFrame([[5,6]]) #1 row 2 column i.e. row matrix
        # print(df)
        
        df = pd.DataFrame([5,6],index=['r1','r2'],columns=['c1'])
        # print(df)#index are rows and columns are columns
        
        df=pd.DataFrame([[1,2],[3,4]],index=['r1','r2'],
                        columns=['c1','c2'])
        # print(df)
        
        df = pd.DataFrame({'c1':[1,2],'c2':[3,4],'c3':[5,6]},
                          index=['r1','r2'])
        # print(df)#if we pass dictionary, key will be like column name
    if 0:#basic details of dataframe
        # df = pd.read_excel('Grouping.xls',index_col=0,sheet_name='Sheet3')
        df = pd.DataFrame({
        'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
        'year': [2016, 2018, np.nan, 2016, 2017],
        'team': ['BOS', 'SEA', 'SEA', 'BOS', np.nan],
        'Hits':[2516,8526,4625,2365,2345],
        'Runs':[1236,4236,2145,2356,2344],
        'HR': [31, 39, 43, 38, 39]},index=['r1','r2','r3','r4','r5',])
        print(df)
        # getting column names and row names
        print(df.columns)
        print(df.index)
        # getting the type of each column
        print(df.dtypes)
        # printing the first 4 rows
        print(df.head(4))
        # printing the last 3 rows
        print(df.tail(3))
        df1 = df[['year']]
        print(df1.dtypes)
        print(pd.isnull(df))#checking the null value positions




        
    if 0:#Upcasting it will be done per-column base
        df=pd.DataFrame([[1.0,2],[3,4]],index=['r1','r2'],
                        columns=['c1','c2'])
        print(df)#upcasting will be done based per column
        print(df.dtypes)
        
    if 0:#Appending rows #df.append(series/dataframe,ignore_index)
        df = pd.DataFrame([[1,2],[3,4]])
        # print(df)
        ser = pd.Series([1.0,3],name='r3')
        df_append=df.append(ser)#name will be considered as row/index
        # print(df_append)#while append with series, all columns will be upcasted
        
        df_append=df.append(ser,ignore_index=True)#name will be ignored and 
        # continued with the dataframe index
        # print(df_append)
        
        df2= pd.DataFrame([[5.0,6],[7,8]])
        df_append = df.append(df2)#while append with dataframe,
        # per-columns will be upcasted
        print(df_append)
        
        df_append = df.append(df2,ignore_index=True)
        print(df_append)#ignoring the index and continued with old dataframe

    if 0:
        df1 = pd.DataFrame([[0,1,2],[3,4,5]])
        print(df1)
        print()
        print(list(df1.iloc[0]))
    if 0:#Dropping data
        d = {'c1':[1,2],'c2':[3,4],'c3':[5,6]}#key will be column in DataFrame
        df= pd.DataFrame(d,index=['r1','r2'])
        print(df)
        print()
        
        df_drop=df.drop(labels='r1')#if we use labels we have to use axis
        print(df_drop)              #by default axis=0
        print()
        
        df_drop=df.drop(labels=['c1','c3'],axis=1)
        print(df_drop)
        print()
        
        #another method
        df_drop=df.drop(index='r1')
        print(df_drop)
        print()
        
        df_drop=df.drop(columns='c2')
        print(df_drop)
        print()
        
        df_drop = df.drop(index='r1',columns='c1')
        print(df_drop)
        print()
        
        df_drop = df.drop(index=['r1'],columns=['c1','c3'])
        print(df_drop)
        print()
        
        print(np.arange(27).reshape(3,3,3))
        print()
        df1= pd.DataFrame([
            [[ 0,  1,  2],
              [ 3,  4,  5],
              [ 6, 7,  8],],
            
             [[ 9, 10, 11],
              [12, 13, 14],
              [15, 16, 17],],
            
             [[18, 19, 20],
              [21, 22, 23],
              [24, 25, 26]]])
        print(df1)
    if 0:
        df = pd.DataFrame({'c1':[1,2,3,4],'c2':[5,6,7,8]},
                          index=['r1','r2','r3','r4'])
        print(df)
        row_df = pd.DataFrame([[9,9]],index=['r5'],columns=['c1','c2'])
        df_append= df.append(row_df)
        print(df_append)
        '''column_df = pd.DataFrame([1,2,3,4],index=['r1','r2','r3','r4'],
                                 columns=['c3'])
       df_append= df.append(column_df)
        print(df_append)'''
        df_drop = df_append.drop(labels='r2')
        print(df_drop)
        df_drop = df_append.drop(labels='c1',axis=1)#removing the columns
        print(df_drop)
        
        df_drop = df_append.drop(index=['r2','r3'])
        print(df_drop)

if 1:#Combining
    if 0:#Concatinate  rows/columns --> pd.concat([df1,df2,df3,.],axis))
        #append is using for concatinating rows only.
        df1 = pd.DataFrame({'c1':[1,2],'c2':[3,4]},index= ['r1','r2'])
        df2 = pd.DataFrame({'c1':[5,6],'c2':[7,8]},index= ['r1','r2'])
        df3 = pd.DataFrame({'c3':[5,6],'c4':[7,8]},index= ['r1','r2'])
        df4 = pd.DataFrame({'c1':[5,6],'c2':[7,8]},index= ['r3','r4'])
        df5 = pd.DataFrame({'c3':[5,6],'c4':[7,8]},index= ['r3','r4'])
        
        df_concat = pd.concat([df1,df2])#adding rows i.e. axis = 0
        print(df_concat)
        
        df_concat = pd.concat([df1,df2],axis=1)#adding columns i.e. axis = 1
        print(df_concat)
        
        df_concat = pd.concat([df1,df3],axis=0)#column labels are differ
        print(df_concat)
        
        df_concat = pd.concat([df1,df4],axis = 1)#row labels are differ
        print(df_concat)
        
        df_concat = pd.concat([df1,df5])#row and column labels are differ
        print(df_concat)
        
        df_concat = pd.concat([df1,df5],axis = 1)#row and column labels are differ
        print(df_concat)
        
    if 0:#Merging  -->pd.merge(df1,df2)
        #pd.merge joins two DataFrames using all their common column labels.
        mlb_df1 = pd.DataFrame({
            'name': ['john doe', 'al smith', 'sam black', 'john does'],
            'pos': ['1B', 'C', 'P', '2B'],
            'year': [2000, 2004, 2008, 2003]})
        mlb_df2 = pd.DataFrame({
            'name': ['john doe', 'al smith', 'jack lee'],
            'year': [2000, 2004, 2012],
            'rbi': [80, 100, 12]})
        
        print("df1 is \n{}\n".format(mlb_df1))
        print("df2 is \n{}".format(mlb_df2))
        
        df_merge = pd.merge(mlb_df1,mlb_df2)
        print(df_merge)
        
        df_merge = pd.merge(mlb_df2,mlb_df1)
        print(df_merge)
        
    if 0:#for merging 2 dataframes, column names and data in columns matched
        df1 = pd.DataFrame({'c1':[1,2],'c2':[3,4],'c3':[5,6],'c4':[7,8]})
        print(df1)
        df2 = pd.DataFrame({'c1':[0,1],'c6':[3,4],'c7':[5,6],'c8':[7,8]})
        print(df2)
        df_merge = pd.merge(df1, df2)
        print(df_merge)
    if 0:
        def concat_rows(df1,df2):
            row_concat = pd.concat([df1,df2])
            return row_concat
        def concat_cols(df1,df2):
            col_concat = pd.concat([df1,df2],axis=1)
            return col_concat
        def merge_df(df1,df2):
            merged_df = pd.merge([df1,df2])
            return merged_df
        
if 0:#Indexing
    if 0:#Direct Indexing #by this, we can retrieve columns only
        d= {'c1':[1,2,3],'c2':[4,5,6],'c3':[7,8,9]}#dict
        df = pd.DataFrame(d,index=['r1','r2','r3'])#dataframe
        print(df)
        
        col1 = df['c1']
        print(col1)
        print(type(col1))#it is a Series
        
        col1 = df[['c1']]
        print(col1)
        print(type(col1))#it is a dataframe
        
        col23 = df[['c1','c3']]
        print(col23)
        print(type(col23))
    if 0:
        d= {'c1':[1,2,3],'c2':[4,5,6],'c3':[7,8,9]}#dict
        df = pd.DataFrame(d,index=['r1','r2','r3'])#dataframe
        print(df)
        #Retrieving the rows by integer indexing
        row1 = df[0:1] #excluding end index i.e like lists
        print(row1)
        print(type(row1))#it is a dataframe since we are using slice
        
        #Retrieving the rows by index labels
        row12 = df['r1':'r2']#including end index
        print(row12)
        print(type(row12))
        # row1 = df['r1']#key error because of r1 treated as column label
    
    if 0:#Other indexing
        d= {'c1':[1,2,3],'c2':[4,5,6],'c3':[7,8,9]}#dict
        df = pd.DataFrame(d,index=['r1','r2','r3'])#dataframe
        print(df)
        
        # Accessing rows by their integer index
        row0 = df.iloc[0] #returns series
        print(row0)
        print(type(row0))
        
        row02=df.iloc[[0,2]]#accessing the multiple rows by using list of integer indexes
        print(row02)
        print(type(row02))#DataFrame
        
        bool_list = [True,False,True]
        rows = df.iloc[bool_list]
        print(rows)
        
    if 0:#Accessing the rows by using index variables
        d= {'c1':[1,2,3],'c2':[4,5,6],'c3':[7,8,9]}#dict
        df = pd.DataFrame(d,index=['r1','r2','r3'])#dataframe
        print(df)
        row1 = df.loc['r1']
        print(row1)
        print(type(row1))#Series
        
        row12 = df.loc[['r1','r2']]
        print(row12)
        print(type(row12))#DataFrame
        
        bool_list = [True,False,True]
        rows = df.loc[bool_list]
        print(rows)
        print(type(rows))
        
        #accessing single/multiple elements
        single = df.loc['r2','c1']#second row first column value
        print(single)
        print(type(single))
        
        multiple = df.loc[['r1','r2'],'c3']
        print(multiple)
        print(type(multiple))#Series
        
        multiple = df.loc[['r1'],['c1','c3']]
        print(multiple)
        print(type(multiple))#dataframe
        
        #changing the values in dataframe
        df.loc['r1','c1']=0
        print(df)
        df.loc[['r2','r3'],'c3'] = 0
        print(df)

    if 0:
        df=pd.DataFrame({'a':[1,2,3],'b':[4,5,np.nan],'c':[6,np.nan,8],'d':[np.nan,9,0]})
        print(df)
        # print(df['b'][0])
        # filling only single column nan values
        if 0:
            df['b']=df['b'].fillna(1000)
            print(df)
        # filling multiple columns nan values with different values
        if 0:
            fill_values={'a':100,'b':1000,'c':800,'d':450}
            df.fillna(fill_values,inplace=True)
            print(df)
#File I/O operations
if 0:
    # Reading data --> accessing csv/excel/json files
    if 1:
        pass
        # df = pd.read_csv('csv_sample1.csv')#considering the first row as column names
        # print("csv format \n{}\n".format(df))

        # df = pd.read_csv('csv_sample1.csv',header=None)#column names given by pandas
        # print(df)

        # column names given by user
        # df = pd.read_csv('csv_sample1.csv',names=['c1','c2','c3','c4','c5','c6'])
        # print(df)



        # consider the column as the index labels
        # df = pd.read_csv('csv_sample1.csv', index_col=0,header=None)
        # print(df)
        # *user cannot give the row names. either he has to choos the columns for index or default values
        # while reading the data from csv file

        #giving names to only some of the columns in data
        # df = pd.read_csv('csv_sample2.csv',names=['c1','c2','c3','c4'])
        # print(df)

        # providing the 2 column names for index labels(multi level indexing)
        # df = pd.read_csv('csv_sample2.csv',index_col=[0,1],header=None)
        # print(df)

        # skipping the rows in data
        # df = pd.read_csv('csv_sample3.csv',skiprows=[0,2,5],header=None)
        # print(df)

        #finding the positions of NaN
        # df = pd.read_csv('csv_sample3.csv', skiprows=[0, 2, 5], header=None)
        # print(df)
        # null_df = pd.isnull(df)
        # print(null_df)

        #Excel file access
        # df = pd.read_excel('excel_sample1.xlsx')#accessing first sheet
        # print("excel sheet is \n{}".format(df.loc[0:20]))

        # df = pd.read_excel('xls_sample.xls',sheet_name=[0,1],index_col=0)#accessing sheet by numbers
        # print("excel sheet is \n{}".format(df[0][0:20]))#printing first sheet
        # print("excel sheet is \n{}".format(df[1][0:20]))#printing second sheet
        
        # df = pd.read_excel('xls_sample.xls',sheet_name=['Sheet1','second_sheet'])#accessing sheet by numbers
        # print("excel sheet is \n{}".format(df['Sheet1'][0:20]))
        
        # df = pd.read_excel('xls_sample.xls',sheet_name=None)#accessing all sheets
        # print("excel sheet is \n{}".format(df.keys()))#printing sheet names
        # print("excel sheet is \n{}".format(df['Sheet1']))#printing data in sheet1
        # print("excel sheet is \n{}".format(df))#printing data in all sheets
        
        #JSON File access -->pd.read_json(filename,orient)
        # oreint is used to treat outer keys are treated as row labels and the inner keys are treated as column labels.
        # df = pd.read_json('json_sample.json')#outer keys are column labels and inner keys as index/row labels
        # print("json file is \n{}\n".format(df[0:1]))
        
        # df = pd.read_json('json_sample.json',orient='index')#outer keys are column labels and inner keys as index/row labels
        # print("json file is \n{}\n".format(df.loc['data']))

        # HTML page table access
        # ******* WORKs OUTSIDE OFFICE NETWORK ******
        # getting the data in list format. Because we can have multiple tables in single page
        # total_tables = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2015_totals.html')
        # print(len(total_tables))
        #accessng the each table by list index
        # print(total_tables[0])
        
        
    if 0:#writing to files
        #writing into csv files    
        # df = pd.read_csv('csv_sample.csv',encoding='latin1')
        # print(df)
        # df.to_csv('csv_result.csv')#storing the index labels as 1st column
        # df.to_csv('csv_result1.csv',index=False)#neglect the row labels
        
        #writing into excel files
        # df = pd.read_excel('xls_sample.xls',sheet_name=None)#return dict
        # print(df)
        # df['Sheet1'].to_excel('xls_result.xls')#by default result sheet name is sheet1
        # df['second_sheet'].to_excel('xls_result.xls')#over write sheet1
        
        #Avoiding overwrite
        # with pd.ExcelWriter('xls_result1.xls') as writer:
        #     df['Sheet1'].to_excel(writer,sheet_name='my_sheet1')
        #     df['second_sheet'].to_excel(writer,index=False,sheet_name='my_sheet2')#not storing the row indexes
            
        #Writing into JSON files
        df= pd.read_json('json_sample.json')
        print(df)
        df.to_json('json_result.json')
        df= pd.read_json('json_result.json')#column labels as outer keys
        print(df)
        df.to_json('json_result1.json',orient='index')#row labels as outer keys
        df= pd.read_json('json_result1.json')
        print(df)
        df= pd.read_json('json_result.json')
        print(df)
#Grouping
if 0:
    if 0:#Grouping by column --> df.groupby(column_label)
        df = pd.read_excel('Grouping.xls')
        print(df)
        
        # df_group = df.groupby('year') #<-- returns a object
        # for name,group in df_group: #getting all grooups
        #     print("year is {}".format(name))
        #     print("group \n{}\n".format(group))
            
        # group_2015 = df_group.get_group(2015)#collecting single group
        # print(group_2015)
        
        # print("sum is \n{}".format(df_group.sum()))#sums all other columns
        # print("mean is \n{}\n".format(df_group.mean()))
        
        #using the filter function
        # no_2015 = df_group.filter(lambda x: x.name> 2015)
        # print(no_2015)
    
    if 0:#Group by multiple columns
        df = pd.read_excel('pizza_data.xls',sheet_name='pizza_data')
        # print(df)
        
        df_group = df.groupby(['Team'])
        print(df_group)#returns a group
        # print(type(df_group))
        for name,group in df_group:
            print("Team is {}\n".format(name))
            print("group is \n{}\n".format(group))
        
        # print("sum is \n{}\n".format(df_group.sum()))
#Features
if 0:
    # Quantitative vs. categorical
    if 0:
        #We often refer to the columns of a DataFrame as the features of the dataset that it represents. These features can be quantitative or categorical.
        
        #A quantitative feature, e.g. height or weight, is a feature that can be measured numerically. These are features we could calculate the sum, mean, or other numerical metrics for.    
        
        #A categorical feature, e.g. gender or birthplace, is one where the values are categories that could be used to group the dataset. These are the features we would use with the groupby function from the previous chapter.
        pass
    
    if 0:#Quantitative Features
        df = pd.DataFrame({
            'T1': [10, 15, 8],
            'T2': [25, 27, 25],
            'T3': [16, 15, 10]},index=['p1','p2','p3'])
        print(df)
        
        # print(df.sum(axis=0))#doing sum by column wise/across the rows
        # print(df.sum(axis=1))#doing sum by row wise/across the columns
        
        print(df.mean())#doing mean by column wise/across the rows
        print(df.mean(axis=1))#doing mean by row wise/across the columns

    if 0:#Weighted Features--> df.multiply([list_of_weights],axis)
        #Along with aggregating quantitative features, we can also apply weights to them. We do this through the multiply function.
        
        df = pd.DataFrame({
          'T1': [0.1, 150.],
          'T2': [0.25, 240.],
          'T3': [0.16, 100.]},index=['p1','p2'])
        print(df)#p1 is taking in sec, p2 is taking in milli sec.
        
        # print("multipled is \n{}".format(df.multiply(2)))
        
        adjust_weights = df.multiply([1000, 1],axis=0)#multiply weights across the rows/multiply weights by column wise
        print(adjust_weights)
        
        adjust_weights1 = df.multiply([1,2,3])#multiplying weights by rows/multiplying weights across the columns/column axis
        print(adjust_weights1)
        
        adjust_weights1 = df.multiply([1,2,3],axis=1)#multiplying weights by rows/multiplying weights across the columns/column axis
        print(adjust_weights1)
        
    if 0:#usage of function
        def col_list_sum(df, col_list, weights=None):
            col_df = df[col_list]#df with rewuired columns
            if weights is not None:
                col_df = col_df.multiply(weights)#multiplying by weights
                print(col_df)
            return col_df.sum(axis=1) #sum of hits and runs
        
        data_frame = pd.DataFrame({
            'Team':['DET','BOS','CLE','FTC'],
            'Hits':[2516,8526,4625,2365],
            'Runs':[1236,4236,2145,2356]})
        # print(data_frame)
        # print(data_frame.keys())
        print(data_frame[['Hits','Runs']])
        column_list = ['Hits','Runs']
        weight=[1,2]
        
        hits_and_runs = col_list_sum(data_frame, column_list,weight)
        print(hits_and_runs)
        # print(type(hits_and_runs))
#Filtering
if 0:
    if 0:
        df = pd.DataFrame({
        'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
        'yearID': [2016, 2016, 2016, 2016, 2017],
        'teamID': ['BOS', 'SEA', 'SEA', 'BOS', np.nan],
        'HR': [31, 39, 43, 38, 39]})
        print('{}\n'.format(df))
        cruzne02 = df['playerID'] == 'cruzne02'
        print('{}\n'.format(cruzne02))
        hr40 = df['HR'] > 40
        print('{}\n'.format(hr40))
        notbos = df['teamID'] != 'BOS'
        print('{}\n'.format(notbos))
    
    if 0:
        print('{}\n'.format(df))
        print(df['playerID'])
        print(type(df['playerID']))
        str_f1 = df['playerID'].str.startswith('c')
        print('{}\n'.format(str_f1))
        str_f2 = df['teamID'].str.endswith('S')
        print('{}\n'.format(str_f2))
        str_f3 = ~df['playerID'].str.contains('o')
        print('{}\n'.format(str_f3))
    if 0:#Filter conditions
        # df = pd.read_excel('Grouping.xls',sheet_name='Sheet2')
        print(df)
        
        filter_players = df['playerID'] == 'canoro01'
        print(filter_players)#returns the boolaen list which passes the filter condition.
        HR_filter = df['HR'] > 35
        print(HR_filter)
        
    if 0:#Filter from functions
        # df = pd.read_excel('Grouping.xls',sheet_name='Sheet2')
        print(df)
        
        # players_filter =df['playerID'].str.startswith('c')
        # print(players_filter)
        
        # team_filter = df['teamID'].str.endswith('S')
        # print(team_filter)
        
        players_filter =df['playerID'].str.isalnum()
        print(players_filter)
        
        # isin_filter = df['playerID'].isin(['abc','def'])
        # print(isin_filter)
        
        isna_filter = df['teamID'].isna()#checking whether NaN is present
        print(isna_filter)
        
        notna_filter = df['teamID'].notna()
        print(notna_filter)
        
    if 0:#Feature Filtering --> df[filter_function] #getting whole rows based on feature value
        # df = pd.read_excel('Grouping.xls',sheet_name='Sheet2')
        # print(df)
        
        hr_40df = df[df['HR']>40]#it is not like retrieving column
        print(hr_40df)
        
        hr_40df = df[~(df['HR']>40)]
        print(hr_40df)
        
        player_filter = df[df['playerID'].str.startswith('c')]
        print(player_filter)
#Sorting
if 0:
    if 1:#Sorting by features --> df.sort_values(feature_name,ascending)
        # df = pd.read_excel('Grouping.xls',sheet_name='Sheet1')
        # print(df)
        df = pd.DataFrame({
        'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
        'year': [2016, 2018, 2015, 2016, 2017],
        'team': ['BOS', 'SEA', 'SEA', 'BOS', np.nan],
        'Hits':[2516,8526,4625,2365,2345],
        'Runs':[1236,4236,2145,2356,2344],
        'HR': [31, 39, 43, 38, 39]})
        print(df)
        print()
        #Sorting ascending
        sort_by_year = df.sort_values('year')
        # print(sort_by_year)
        
        #Sorting descending
        sort_by_year = df.sort_values('year',ascending=False)
        # print(sort_by_year)
        
        #Sorting by multiple Features
        sort_by_year_and_hits = df.sort_values(['year','Hits'],ascending=[True,False])
        print(sort_by_year_and_hits)#first sorted by year and next sorted internally by hits
#Metrics
if 0:
    if 0:#Numerical metrics/Quantative metrics
        # df = pd.read_excel('Grouping.xls',sheet_name='Sheet1')
        df = pd.DataFrame({
        'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
        'year': [2016, 2018, 2015, 2016, 2017],
        'team': ['BOS', 'SEA', 'SEA', 'BOS', np.nan],
        'Hits':[2516,8526,4625,2365,2345],
        'Runs':[1236,4236,2145,2356,2344],
        'HR': [31, 39, 43, 38, 39]})
        print(df)
        
        metrics= df[['Hits','Runs']].describe()#Provides the metrics for the features
        print(metrics)
        
        metrics1 = df[['Hits','Runs']].describe(percentiles=[.2,.8,.6])
        print(metrics1)
        
    if 0:#Categorical metrics
        # df = pd.read_excel('Grouping.xls',sheet_name='Sheet1')
        df = pd.DataFrame({
        'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
        'year': [2016, 2018, 2015, 2016, 2017],
        'Team': ['BOS', 'SEA', 'SEA', 'BOS', np.nan],
        'Hits':[2516,8526,4625,2365,2345],
        'Runs':[1236,4236,2145,2356,2344],
        'HR': [31, 39, 43, 38, 39]})
        print(df)
        
        print(df[['Hits','Runs']])
        quantities = df[['Hits','Runs']]
        categories = df[['year','Team']]#getting catagerocial features
        print(categories)
        
        print(categories['year'].value_counts())#returns the counts of categories appeared in a feature
        
        print(categories['year'].value_counts(normalize=True))#returns the 
        # percentage of categories appeared in a feature
        
        # print(categories['year'].value_counts(ascending=True))#returns the counts of categories appeared in a feature in ascending order
        
        # print(categories.value_counts())
        print(quantities['Hits'].value_counts())

    if 0:#Getting only categories from feature/column
        # df = pd.read_excel('Grouping.xls',sheet_name='Sheet1')
        df = pd.DataFrame({
        'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
        'year': [2016, 2018, 2015, 2016, 2017],
        'team': ['BOS', 'SEA', 'SEA', 'BOS', np.nan],
        'Hits':[2516,8526,4625,2365,2345],
        'Runs':[1236,4236,2145,2356,2344],
        'HR': [31, 39, 43, 38, 39]})
        # print(df)
        
        print(df['year'].unique())#getting only categories from feature in ndarray format
        
        print(df['Hits'].unique())
#Plotting
if 0:
    if 0:#Basics -->df.plot(),--> plt.show()
        # df = pd.read_excel('Grouping.xls',sheet_name='Sheet3')
        df = pd.DataFrame({
        'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
        'year': [2016, 2018, 2015, 2016, 2017],
        'team': ['BOS', 'SEA', 'SEA', 'BOS', np.nan],
        'Hits':[2516,8526,4625,2365,2345],
        'Runs':[1236,4236,2145,2356,2344],
        'HR': [31, 39, 43, 38, 39]},index=['r1','r2','r3','r4','r5',])
        print(df)
        
        df[['Hits','year']].plot()#plots against index labels
        plt.show()
        
        # df[['Hits','year']].plot(x='year',y='Hits')#plots X vs. Y
        # plt.title('year vs. hits')
        # plt.xlabel('year')
        # plt.ylabel('hits')
        # plt.show()
        # plt.savefig('year_vs_hits.png')#saing as png file
        
    if 0:#Other plots
        # df = pd.read_excel('Grouping.xls',sheet_name='Sheet3')
        # print(df)
        df[['Hits','year']].plot(x='year',y='Hits',kind='hist')#plots X vs. Y histograms chart
        plt.title('year vs. hits')
        plt.xlabel('year')
        plt.ylabel('hits')
        plt.show()
        
    if 0:#Multiple features i.e more features on 1 graph
        # df = pd.read_excel('Grouping.xls',index_col=0,sheet_name='Sheet3')
        # print(df)
        # df[['Hits','Runs']].plot()
        # plt.show()
        
        # df1 = pd.read_excel('Grouping.xls',sheet_name='Sheet3')
        print(df)
        df[['year','Hits','Runs']].plot(x='year')
        plt.show()
#To NumPy
if 0:
    if 0:#Machine learning
        # The DataFrame object is great for storing a dataset and performing data analysis in Python. However, most machine learning frameworks (e.g. TensorFlow), work directly with NumPy data. Furthermore, the NumPy data used as input to machine learning models must solely contain quantitative values.

        # Therefore, to use a DataFrame's data with a machine learning model, we need to convert the DataFrame to a NumPy matrix of quantitative data. So even the categorical features of a DataFrame, such as gender and birthplace, must be converted to quantitative values.
        pass

    if 0:#Indicator Features
        # When converting a DataFrame to a NumPy matrix of quantitative data, we need to find a way to modify the categorical features in the DataFrame.

        # The easiest way to do this is to convert each categorical feature into a set of indicator features for each of its categories. The indicator feature for a specific category represents whether or not a given data sample belongs to that category.
        
        # Note that an indicator feature contains 1 when the row has that particular category, and 0 if the row does not.
        pass

    if 0:#Converting categorical features to Indicator features
        # df = pd.read_excel('Grouping.xls',index_col=0,sheet_name='Sheet3')
        df = pd.DataFrame({
        'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
        'year': [2016, 2018, 2015, 2016, 2017],
        'team': ['BOS', 'SEA', 'SEA', 'BOS', np.nan],
        'Hits':[2516,8526,4625,2365,2345],
        'Runs':[1236,4236,2145,2356,2344],
        'HR': [31, 39, 43, 38, 39]},index=['r1','r2','r3','r4','r5',])
        print(df)
        print(df.columns)
        print(df.index)
        
        
        converted = pd.get_dummies(df)
        print(type(converted))
        print(converted)
        print(converted.columns)#getting all column names
        
        #Converting to NumPy
        n_matrix = converted.values
        print(n_matrix)
        print(type(n_matrix))

# generating the dates using pandas date_range function
# date_range(start_date,periods=<no.of dates>,freq=required <year/month/hour etc. difference >)
# frequence --> year y, month m, day d, hour h,minute T,second s,microsec us,nanosec ns
if 1:
    #series
    if 1:
        #generating dates
        if 0:
            # generating the 3 dates/periods in series with year difference
            if 0:
                df =pd.Series(pd.date_range("2020",periods=3,freq="y"))
                print(df)
                print(df.dt.year)#getting all years from series dates
            # generating the 3 dates/periods in series with month difference
            if 0:
                df =pd.Series(pd.date_range("2020",periods=3,freq="m"))
                print(df)
                print(df.dt.month)
            # generating the 3 dates/periods in series with day difference
            if 0:
                df = pd.Series(pd.date_range("2020", periods=3, freq="d"))
                print(df)
                print(df.dt.date)
            # generating the 5 dates/periods in series with hour difference
            if 0:
                df = pd.Series(pd.date_range("2020-01", periods=5, freq="h"))
                print(df)
                print(df.dt.hour)
            # generating the 5 dates/periods in series with minute difference
            if 0:
                df = pd.Series(pd.date_range("2020-01", periods=5, freq="T"))
                print(df)
                print(df.dt.minute)
        if 1:
            #getting numpy array with datetime.date objects
            if 1:
                if 0:
                    dates=pd.date_range("2020-12-31",periods=3,freq="d")
                    print(dates)
                    print(type(dates))
                    print(dates.month)
                    print(dates.dayofweek)# ---> monday=0 sunday=6
                    print(dates.day_name())
                    print(dates.quarter)
                    print(dates.tz) #returns None
                    print(dates.freqstr)#freq string means returns the type of the frequency
                    if 0:
                        print(dates.is_month_start)
                        print(dates.is_month_end)
                        print(dates.is_quarter_start)
                        print(dates.is_quarter_end)
                    if 0:
                        print(dates.year)
                        print(dates.dayofyear)
                        print(dates.is_year_start)
                        print(dates.is_year_end)

                if 0:
                    s = pd.Series(["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"])
                    s = pd.to_datetime(s)#converting series to datetime
                    print(s)
                    print(type(s.dt))
                    print(s.dt.date)
                    print(s.dt.time)
                    print(s.dt.timetz)
                    print(s.dt.dayofyear)
                    print(s.dt.tz)
                    # print(s.dt.freqstr)#not supported
                    print(s.dt.is_month_start)

                if 0:
                    #using datetimeindex
                    idx = pd.DatetimeIndex(["1/1/2020 10:00:00+00:00",
                                            "2/1/2020 11:00:00+00:00"])#creation of DateTimeIndex
                    print(idx)
                    print(idx.date)
                    print(idx.year)
                    print(idx.timetz)
                    print(idx.dayofyear)
                if 0:
                    df = pd.DataFrame({'inputDates': ['2015-01-07', '2015-12-02',
                                                        '2005-01-03', '2016-11-13',
                                                        '2020-06-03'],
                                         'inputVals': [1, 2, 3, 4, 5]})

                    df['inputDates'] = pd.to_datetime(df['inputDates'])
                    df['dayOfWeek'] = df['inputDates'].dt.day_name()
                    print(df['dayOfWeek'])





                #print(help(re.subn))
#print(type(re.subn("abc","xyz","abdabd")[1]))
# https://www.kaggle.com/code/abhi8923shriv/pandas-library-80-exercises
if 0:#pandas version
    print(pd.__version__)

#Section 1 - The Pandas Series Object
if 0:
    if 0:
        data=pd.Series([1,2.3,4])
        if 0:
            print(data)
        if 0:
            print(data.values)#prints the values
        if 0:
            print(data.shape)#prints the shape of series
        if 0:
            print(data.index)#prints the index values
        if 0:
            print(data[1])
            print(data[1:3])
    if 0:
        data1= pd.Series([1,2.3,4.],index=[2,3,4])
        if 0:
            print(data1)
        if 0:
            print(data1[4])
        if 0:
            print(data1[[2,4]])#accessing the data using index
        if 0:
            print(data1[2:4])#here it si  returning the last value only
    if 0:
        Population_dict = {'California': 123543, 'Texas': 87451, 'Boston': 986734, 'Newyork': 907856}
        population = pd.Series(Population_dict)
        if 0:
            print(population)
        if 0:
            print(population['California'])
            print(population['California':'Boston'])#not skips the last index
    if 0:#Constructing Series objects
        if 0:
            # pd.Series(data,index,name)#name is for column
            s1=pd.Series([2,3,4,8])
            s2=pd.Series({'a':1,'b':2,'c':3})
            s3=pd.Series([1,'a',2.3],index=['a','b','c'])
            s4=pd.Series(5,index=[1,3,7,6])#data will  be duplicated
            # s5=pd.Series([2,54,78],index=['a','b','c','d'])#Error because index values are more than data
            s6=pd.Series({1:1,2:4,3:9},name='c1')
            print(s1,s2,s3,s4,s6)

# Section 2 - The Pandas Dataframe Object
if 1:
    area_dict = {'California': 12345, 'Boston': 6745, 'newyork': 9078, 'newtown': 23126}
    Population_dict = {'California': 123543, 'Texas': 87451, 'Boston': 986734, 'Newyork': 907856}
    area = pd.Series(area_dict)
    population = pd.Series(Population_dict)
    # dataframe using series objects in dictionary
    if 0:
        print(area)
        print(population)
        states = pd.DataFrame({'population':population,'area':area})
        print(states)
    # row and column labels
    if 0:
        states = pd.DataFrame({'population': population, 'area': area})
        print(states.index)#row labels
        print(states.columns)#column labels
    # dataframe using series
    if 0:
        df=pd.DataFrame(population,columns=['population'])
        print(df)
    # create dataframe using list of dictionaries
    if 0:
        if 0:
            data=[{'a':i,'b':2*i} for i in range(1,5)]
            print(data)
            df=pd.DataFrame(data)
            print(df)
        if 0:
            data=[{'a':1,'b':3},{'b':4,'c':6}]
            df=pd.DataFrame(data)
            print(df)
    # dataframe using numpy array
    if 0:
        array=np.random.rand(3,2)
        print(array)
        df=pd.DataFrame(array,index=['a','b','c'],columns=['first','second'])
        print(df)
    # creating dataframe using zero array
    if 0:
        a=np.zeros(3)
        print(a)
        b=np.zeros(3,[('a',np.int8),('b',np.float32)])
        print(b)
        df=pd.DataFrame(b)
        print(df)

# Section 3 - The Pandas Index Object
if 0:
    if 0:
        ind=pd.Index([2,5,6,4,3])
        print(ind)
        print(ind[1])
        print(ind[::2])
        print(ind.size,ind.shape,ind.ndim,ind.dtype)
    if 0:
        s1=pd.Series({'a':1,'b':2,'c':3,'d':4},name='col1')
        if 0:#series as dictionary
            print(s1)
            print(s1['a'])
            s1['e']=5
            print('a' in s1)
            print(s1.keys())
            print(s1.keys) #returns a object
            print(s1.values)
        if 0:#series as list
            print(s1['a':'c'])#includes the last index label
            print(s1[0:3])#skips the last index value like normal list slicing
            res=s1[(s1>1) & (s1 <4)]#masking the unwanted data
            print(res)
            print(s1[['a','d']])#fancy indexing we can use index labels only

# Section 4 - Indexers: loc, iloc, and ix
if 0:
    s1=pd.Series(['a','b','c','d','e'],index=[1,3,5,7,9])
    area = pd.Series({'California': 423967, 'Texas': 695662, 'New York': 141297, 'Florida': 170312, 'Illinois': 149995})
    pop = pd.Series({'California': 38332521, 'Texas': 26448193, 'New York': 19651127, 'Florida': 19552860, 'Illinois': 12882135})
    data = pd.DataFrame({'area': area, 'pop': pop})
    if 0:
        print(s1)
        print(s1[1:3])#here 1,3 are not index labels. they are index positions
        print(s1[1])#explicit index, explicit indexing means label indexing
        # implicit index, implicit indexing means list indexing
        print(s1[1:3])#implicit indexing
    if 0:
        #explicit indexing
        s1 = pd.Series([1, 3, 5, 7, 9], index=['a', 'b', 'c', 'd', 'e'])
        print(s1.loc['a'])
        print(s1.loc['a':'d'])
    if 0:
        #implicit indexing
        s1 = pd.Series([1, 3, 5, 7, 9], index=['a', 'b', 'c', 'd', 'e'])
        print(s1.iloc[1])
        print(s1.iloc[1:4])
    if 0:
        print(data)
        print(data.area)
        print(data['area'])
        print(data.area is data['area'])
        print(data.pop)#here pop is a method not a column name
        print(data['pop'])
    if 0:#adding the column to the dataframe
        print(data)
        data['density']=data['pop']/data['area']
        print(data)
        print(data.values)
        print(data.size,data.ndim,data.shape)
    if 0:#transpose the dataframe
        print(data)
        print(data.T)
    if 0:#accessing the rows/columns
        data['density']=data['pop']/data['area']
        print(data)
        print(data.values[0])#accessing the rows
        print(data['area'])#accessing the columns
        print(data.loc['California':'Florida'])#accessing the specific rows
        print(data.loc['California':'Florida','area'])#accessing the specific rows and columns
        print(data.loc['California':'Florida', 'area':'pop'])
        # 'California': 38332521, 'Texas': 26448193, 'New York': 19651127, 'Florida'
        print(data.loc[['California','New York']])
        print(data.loc[['California', 'New York'],['area','pop']])

    if 1:#accessing the rows/columns
        data['density']=data['pop']/data['area']
        print(data)
        print(data.iloc[:3])
        print(data.iloc[:3,:2])
        print(data.iloc[[1,3,4],[0,2]])
    if 0:#masking the unwanted data
        print(data)
        data['density'] = data['pop'] / data['area']
        print(data[data['density']>100])

# Section 5 - Operating on Data in Pandas
if 0:
    s1 = pd.Series(np.random.randint(0, 10, 4))
    # print(s1)
    d1=pd.DataFrame(np.random.randint(0,10,(3,4)),columns=['c1','c2','c3','c4'])
    # print(d1)
    area = pd.Series({'Alaska': 23456, 'California': 89675, 'Boston': 89234, 'Jaandar': 12345}, name='area')
    population = pd.Series({'California': 38332521, 'Texas': 26448193, 'New York': 19651127}, name='population')
    if 0:#ufunction i.e utility function
        print(np.log(s1))
        print(np.exp(s1))
        print(np.sin(d1*np.pi/4))
    if 0:
        print(area,population)
        print(area/population)
        print(area.index)
        print(population.index)
        # print(area.index | population.index)#combining the 2 index objects NOT WORKING
    if 0:
        a=pd.Series([1,2,3],index=[0,1,2])
        b = pd.Series([4,6,5], index=[1, 2,3])
        print(a+b)#getting NaN values
        print(a.add(b,fill_value=0))#to avoid the NaN values
    if 0:
        a=pd.DataFrame(np.random.randint(0,10,(2,2)),columns=list('AB'))
        print(a)
        b = pd.DataFrame(np.random.randint(0, 10), (3, 3), columns=list('ABC'))#here (3,3) are index labels
        print(b)
        c = pd.DataFrame(np.random.randint(0, 10), (3, 2), columns=list('ABC'))#here (3,2) are index labels
        print(c)
        d= pd.DataFrame(np.random.randint(0, 10, (3, 3)), columns=list('ABC'))#here (3,3) are shape
        print(d)
        print(a+d)
    if 0:
        a=pd.DataFrame(np.random.randint(0,10,(3,3)),columns=list('ABC'))
        b = pd.DataFrame(np.random.randint(0,10),(1,1),columns=list('AB'))
        c=a+b
        print(c)
        print(a)
        print(a.mean())
        fill= a.stack()
        fill=a.stack().mean()
        print(fill)
        d=a.add(b,fill_value=fill)#filling b dataframe values with fill variable value
        print(d)
    if 1:#operations between dataframe and series
        if 0:
            b =pd.DataFrame(np.random.randint(0,10,(3,3)))
            a=pd.DataFrame(np.random.randint(10,size=(3,3)))#if we do not provide min value we have mention size parameter
            print(a)
            print(a[0])#accessing the column
            print(a.values[0])#accessing the row
            print(a-a[0])
        if 0:
            b = pd.DataFrame(np.random.randint(0, 10, (3, 4)))
            a = pd.DataFrame(np.random.randint(10, size=(3, 4)))# if we do not provide min value we have mention size parameter
            print(a)
            print(a[0])  # accessing the column
            print(a.values[0])  # accessing the row
            print(a - a[0])#will do the subtract operation on row by row
    if 0:
        a = pd.DataFrame(np.random.randint(0, 10, (3, 4)), columns=list('QRST'))
        print(a)
        if 0:
            row=a.iloc[-1]#accessing the last row
            print(row)
            print(a-row)
        if 0:
            half_row=a.iloc[0,::2]
            print(half_row)
            print(a-half_row)

# Section 6 - Handling Missing Data
if 0:
    if 0:#using None in the array instead of np.nan
        a=np.array([1,None,3,4])
        print(a)
        print(a.dtype)
    if 0:#using np.nan value instead of None
        a=np.array([1,np.nan,3,4])
        print(a)
        print(a.dtype)
    if 0:
        a = np.array([1, np.nan, 3, 4])
        print(1+np.nan)
        print(0*np.nan)
        print(a.sum(),a.min(),a.max())#returns nan,nan,nan
        print(np.nansum(a),np.nanmax(a),np.nanmin(a))#it will perform even with nan values also.
    if 1:#converting None to nan in pandas
        a=pd.Series(range(3),dtype=int)
        print(a)
        a[0]=None #assiging None
        print(a)

# Section 7 - Operating on Null Values
if 0:# checking the null values
    if 1:
        if 1:#series
            s1=pd.Series([1,2,np.nan,4,None,6])
            print(s1)
            if 0:
                print(s1.isnull())
                print(s1.isna())
                print(s1.notnull())
                print(s1.notna())
            # removing the nan values
            if 0:
                s2 = s1.dropna()
                print(s2)
            # replacing the nan values with required values
            if 0:
                s2 = s1.fillna(1000)
                print(s2)
            #adding the items in existing series
            if 0:
                s1['abc']=33
                print(s1)
            # filling nan values with previous values
            if 0:
                s2=s1.fillna(method='ffill')
                print(s2)
            # filling nan values with next values
            if 0:
                s2=s1.fillna(method='bfill')
                print(s2)

        if 1:#dataframe
            d1 = pd.DataFrame([[1, 2, 3], [3, None, 5], [7, np.nan, None]])
            print(d1)
            if 0:
                print(d1.isnull())
                print(d1.isna())
                print(d1.notnull())
                print(d1.notna())
            # drop rows which are having nan values
            if 0:
                d2=d1.dropna()
                print(d2)
            # dropping the columns which are having nan values
            if 0:
                d2=d1.dropna(axis='columns')
                print(d2)
            # dropping the columns which are having nan values
            if 0:
                d3=d1.dropna(axis=1)#dropping the columns
                print(d3)
            # adding the column to existing the dataframe
            if 0:
                d1[3]=np.nan
                print(d1)
            #dropping the columns which are nan values inplace
            if 0:
                d1[3]=np.nan
                d1.dropna(axis=1,inplace=True)
                print(d1)
            # it will drop the column which is having "ALL" null values
            if 0:
                d1[3]=np.nan
                print(d1)
                d3=d1.dropna(axis='columns',how='all')
                print(d3)
            # thresh will helps to check the non-null values in columns or rows and drops
            # if row/column doesnt have the threshold non-values
            if 0:
                d1[3]=4
                print(d1)
                d3=d1.dropna(axis='rows',thresh=4)
                print(d3)
            #forward filling in columns
            if 0:
                d2=d1.fillna(axis=1,method='ffill')
                print(d2)
            # forward filling in rows
            if 0:
                d2=d1.fillna(axis=0,method='ffill')
                print(d2)
            # backward filling in rows
            if 0:
                d2 = d1.fillna(axis=0, method='bfill')
                print(d2)

# Section 8 - Hierarchical Indexing (Multi Indexing)
# multindexed series
if 0:
    index = [('California', 2000), ('California', 2010), ('New York', 2000), ('New York', 2010), ('Texas', 2000),
             ('Texas', 2010)]
    populations = [33871648, 37253956, 18976457, 19378102, 20851820, 25145561]
    multi_index = pd.MultiIndex.from_tuples(index)
    s1 = pd.Series(populations, index=index)
    print(s1)
    if 0:
        print(s1.index)
    # reindexing the index values
    if 0:
        s1=s1.reindex(multi_index)
        print(s1)
        print(s1[:,2010])
    # unstacking the multi indexing series i.e converting the multi indexed series to dataframe
    # stacking the dataframe i.e converting the dataframe to multindexed series
    if 0:
        s2=s1.reindex(multi_index)
        print(s2)
        s3=s2.unstack()#converting the multi indexed series to dataframe
        print(s3)
        print(type(s3))
        s4=s3.stack()#converting the dataframe into multi ndexed series
        print(s4)
        print(type(s4))
    #creating dtatframe using multi indexed series
    if 0:
        d1=pd.DataFrame({'total':s1,'under18':[435435,4565473,657868,5657654,7654654,6887689]})
        # print(d1)
        d2 = pd.DataFrame({'total': s1.reindex(multi_index), 'under18': [435435, 4565473, 657868, 5657654, 7654654, 6887689]})
        print(d2)
    # multi indexed dataframe
    if 0:
        d1=pd.DataFrame(np.random.randint(2,8,(4,2)),index=[['a','a','b','b'],[1,2,1,2]],columns=['first','second'])
        print(d1)
        print(type(d1))
    # multi indexed series
    if 0:
        data = {('California', 2000): 33871648, ('California', 2010): 37253956, ('Texas', 2000): 20851820,
                ('Texas', 2010): 25145561, ('New York', 2000): 18976457, ('New York', 2010): 19378102}
        s1=pd.Series(data)
        print(s1)
    #multi indexed rows
    if 0:
        array_index= pd.MultiIndex.from_arrays([['a','a','b','b'],['1','2','1','2']])
        tuple_index = pd.MultiIndex.from_tuples([('a',1),('a',2),('b',1),('b',2)])
        product_index = pd.MultiIndex.from_product([['a', 'b'], [1, 2]])
    #multi indexed columns
    if 1:
        index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]], names=['year', 'visit'])
        columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']], names=['subject', 'type'])
        # print(index)
        # print(columns)
        data=np.random.randint(4,10,(4,6))
        df = pd.DataFrame(data,index=index,columns=columns)
        print(df)
        if 0:#accessing the columns
            print(df['Sue'])
            print(df['Sue']['HR'])
        # accessing the rows
        if 0:
            print(df.loc[2013])
            print(df.loc[2013,1])
            print(df.loc[[2013],['Bob']])

# Section 9 - Combining Datasets: Concat and Append
def make_df(cols,ind):
    """Quickly make a DataFrame"""
    data={c:[str(c)+str(i) for i in ind] for c in cols}
    return pd.DataFrame(data,ind)

if 0:
    if 0:
        #creation of dataframe using function
        df=make_df('ABC',range(10))
        print(df)
    #concatination of numpy arrays
    if 0:
        # 1-D array concatination
        if 0:
            x,y,z=[1,2,3],[4,5,6],[7,8,9]
            array=np.concatenate([x,y,z])
            print(array)
        # 2-D array concatination
        if 1:
            x=np.arange(4).reshape(2,2)
            print(x)
            # columns concatination
            if 0:
                array=np.concatenate([x,x],axis=1)
                print(array)
            if 0:
                array=np.concatenate([x,x],axis=0)
                print(array)
    #concatination of series/dataframe
    if 0:
        #series concatination
        if 0:
            a=pd.Series([1,2,3],index=['a','b','c'])
            b=pd.Series([10,20,30],index=['c','e','f'])
            combined_series=pd.concat([a,b])
            print(combined_series)
            print(combined_series.loc['c'])
        #dataframe concatination
        if 0:
            df1=make_df('AB',[1,2])
            df2=make_df('AB',[3,4])
            df3=make_df('AB',[0,1])
            df4=make_df('CD',[0,1])
            # combining the rows
            if 0:
                combined_df=pd.concat([df1,df2],axis=0)
                print(combined_df)
                combined_df1=pd.concat([df3,df4],axis=0)
                print(combined_df1)
            # combining the columns
            if 0:
                combined_df = pd.concat([df1, df2], axis=1)
                # print(combined_df)
                combined_df1 = pd.concat([df3, df4], axis=1)
                print(combined_df1)
            # duplicate indices
            if 0:
                df2.index=df1.index
                combined_df = pd.concat([df1, df2])
                print(combined_df)
            #ignoring the index while combining
            if 0:
                df2.index = df1.index
                combined_df=pd.concat([df1,df2])
                print(combined_df)
                df2.index=df1.index
                combined_df=pd.concat([df1,df2],ignore_index=True)
                print(combined_df)
            #adding the multiindex keys
            if 0:
                combined_df=pd.concat([df1,df2])
                print(combined_df)
                combined_df1=pd.concat([df1,df2],keys=['x','y'])#adding the multiindex to the dataframe
                print(combined_df1)
    #concatinating the dataframes with different columns
    if 0:
        df1=make_df('ABC',[1,2])
        df2=make_df('BCD',[3,4])
        # combining the 2 dataframes
        if 0:
            combined_df=pd.concat([df1,df2])
            print(combined_df)
        #INNER JOIN
        if 0:
            combined_df = pd.concat([df1, df2],join='inner')#
            print(combined_df)
        # OUTER JOIN
        if 0:
            combined_df = pd.concat([df1, df2], join='outer')  #it is like normal concatination
            print(combined_df)
    #appending the dataframes
    if 1:
        df1 = make_df('ABC', [0, 1])
        df2 = make_df('BCD', [3, 4])
        if 0:
            appended_df=df1._append(df2)#adding as rows
            print(appended_df)
        if 0:
            appended_df = df1._append(df2,ignore_index=True)
            print(appended_df)

# Section 10 - Combining Datasets: Merge and Join
#  Categories of Joins
# The pd.merge() function implements a number of types of joins: the one-to-one, many-to-one, and many-to-many joins.

if 0:
    df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                        'job': ['Accounting', 'Engineering', 'Engineering', 'HR']})
    df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                        'hire_date': [2004, 2008, 2012, 2014]})
    df4 = pd.DataFrame({'job': ['Accounting', 'Engineering', 'HR'],
                        'supervisor': ['carly', 'Guido', 'steve']})
    # Merge dataframes.
    # For merging 2 dataframes, 2 dataframes must have at least 1 common column name
    if 1:
        if 0:
            print(df1)
            print(df2)
            df3=pd.merge(df1,df2)
            print(df3)
        # many to one join
        if 0:
            # Many-to-one joins are joins in which one of the two key columns contains duplicate entries.
            # For the many-to-one case, the resulting DataFrame will preserve those duplicate entries as appropriate.
            df3 = pd.merge(df1, df2)
            print(df3)
            print(df4)
            merged_df=pd.merge(df3,df4)
            print(merged_df)
        # Many-to-many joins
        if 0:
            # Many-to-many joins are a bit confusing conceptually, but are nevertheless well defined.
            # If the key column in both the left and right array contains duplicates, then the result is a many-to-many merge
            df5=pd.DataFrame({'job':['Accounting','accounting','Engineering','Engineering','HR','HR'],
                              'skills':['math','spreadsheets','coding','linux','spreadsheets','organisation']})
            print(df1)
            print(df5)
            merged_df=pd.merge(df1,df5)
            print(merged_df)
        # Merge using on keyword
        if 0:
            # you can explicitly specify the name of the key column using the on key‐word,
            # which takes a column name or a list of column names
            # it means when we have 2 common column names, we can specify the specific column for merging
            print(df1)
            print(df2)
            merged_df=pd.merge(df1,df2,on='employee')
            print(merged_df)
        #merging the dataframes by common column names and using "on" concept
        if 1:
            df1 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'], 'rank': ['1', '4', '3', '7']})
            df2 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'], 'rank': ['3', '1', '2', '4']})
            if 0:
                merged_df=pd.merge(df1,df2,on='name')
                # print(merged_df)
                merged_df1=pd.merge(df1,df2,on='rank')
                print(merged_df1)
            if 0:
                merged_df=pd.merge(df1,df2,on='name',suffixes=['_L','_R'])
                print(merged_df)
        # Merge using left_on and right_on --> selecting the column names from left and right dataframes
        if 0:
            print(df1)
            df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                                'salary': [70000, 80000, 120000, 90000]})
            print(df3)
            merged_df= pd.merge(df1,df3,left_on='employee',right_on='name')
            print(merged_df)
            updated_merged=merged_df.drop('name',axis=1)
            print(updated_merged)
        # merging based on index values in dataframes
        if 0:
            # print(df1)
            # print(df2)
            df1a=df1.set_index('employee')
            df2a = df2.set_index('employee')
            print(df1a)
            print(df2a)
            merged_df=pd.merge(df1a,df2a,left_index=True,right_index=True)#merging based on index match
            print(merged_df)
        #merging based on column with index values
        if 0:
            print(df1)
            print(df2)
            df2a=df2.set_index('employee')
            merged_df = pd.merge(df1,df2a,left_on='employee',right_index=True)
            print(merged_df)
        # merging based on joins
        if 0:
            df6 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],
                                'food': ['fish', 'beans', 'bread']})

            df7 = pd.DataFrame({'name': ['Mary', 'Joseph'],
                                'drink': ['wine', 'beer']})
            print(df6)
            print(df7)
            #INNER JOIN
            if 0:
                merged_df=pd.merge(df6,df7)#default join is inner join
                # print(merged_df)
                inner_merged=pd.merge(df6,df7,how='inner')
                # print(inner_merged)
            #OUTER JOIN
            if 0:
                outer_merged = pd.merge(df6, df7, how='outer')
                print(outer_merged)
            # LEFT JOIN
            if 0:
                left_merged = pd.merge(df6, df7, how='left')
                print(left_merged)
            # RIGHT JOIN
            if 0:
                right_merged = pd.merge(df6, df7, how='right')
                print(right_merged)

# Section 14 - GroupBy: Split, Apply, Combine
# The split step involves breaking up and grouping a DataFrame depending on the value of the specified key.
# The apply step involves computing some function, usually an aggregate, transfor‐mation, or filtering, within the individual groups.
# The combine step merges the results of these operations into an output array.
if 0:
    df=pd.DataFrame({'key':['A','B','C','A','B','C'],'data':[1,2,3,4,5,6]})
    print(df)
    df1=pd.DataFrame({'key':['a','b','c','a','b','c'],'data1':[1,2,3,4,5,6],'data2':[10,20,30,40,50,60]})
    #group by
    if 0:
        df_group= df.groupby('key')
        print(df_group)# <-- it is a groupby object
        for name,group in df_group:
            print(group)
    if 0:
        df_group=df.groupby('key')
        for name,group in df_group:
            print(name,group)
        df_a = df.groupby('key')['data'].sum()
        print(df_a)
    #aggregate functions
    if 0:
        result_df=df1.groupby('key').aggregate([min,np.median,max])
        print(result_df)
        print(result_df.loc['a',['data1']])
        print(type(result_df.loc['a', ['data1']]))
# apply will work on axis wise but map will will on element wise
if 0:
    df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
    df1=df.apply(np.sqrt)

if 0:
    df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'], 'data': [1, 2, 3, 4, 5, 6]})
    # print(df)
    df1= df.map(lambda x: x*2)
    print(df1)

if 0:
    df =pd.DataFrame({'a':[1,2,3],'b':[4,5,6],'c':[7,8,9]})
    # print(df.iloc[0][1])#gives warning
    # print(df.iloc[0].get(1))#gives warning
    print(df.iloc[0].iloc[1])
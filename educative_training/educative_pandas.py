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
        
if 1:#Indexing
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
        single = df.loc['r2','c1']#first row index only
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

if 0:#File I/O operations
    if 0:#Reading data --> accessing csv/excel/json files
        # df = pd.read_csv('csv_sample.csv',encoding='latin1',index_col=0)
        # print("csv format \n{}\n".format(df))
        
        # df = pd.read_csv('csv_sample.csv',encoding='latin1',index_col=0)
        # print("csv format \n\n\n{}\n".format(df))#index_col means which column
                                    # should be used as index labels
        
        #Excel file access
        # df = pd.read_excel('xls_sample.xls')#accessing first sheet
        # print("excel sheet is \n{}".format(df.loc[0:20]))
        
        #df = pd.read_excel('xls_sample.xls',sheet_name=[0,1],index_col=0)#accessing sheet by numbers
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
        
        df = pd.read_json('json_sample.json',orient='index')#outer keys are column labels and inner keys as index/row labels
        print("json file is \n{}\n".format(df.loc['data']))
        
        
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
        
if 0:#Grouping
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
        
if 1:#Features
    if 0:#Quantitative vs. categorical
    
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

if 1:#Filtering
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

if 0:#Sorting
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

if 1:#Metrics
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
        
if 0:#Plotting
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
        
if 1:#To NumPy
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
        
#print(help(re.subn))
print(type(re.subn("abc","xyz","abdabd")[1]))







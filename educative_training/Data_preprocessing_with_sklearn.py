#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 06:49:30 2020

@author: pj
"""
import sklearn
import numpy as np
from sklearn.preprocessing import scale
import pandas as pd
df=pd.read_excel('Grouping.xls',index_col=0,sheet_name='Sheet3')
main_df = df[['Hits','Runs','HR']]  #will be used whole script
main_df = main_df.values
# print(main_df)
#print(type(main_df))
if 0:#Standardising the data
    if 1:#Standard data format
        # When data can take on any range of values, it makes it difficult to interpret. Therefore, data scientists will convert the data into a standard format to make it easier to understand. The standard format refers to data that has 0 mean and unit variance (i.e. standard deviation = 1), and the process of converting data into this format is called data standardization.
        # Data standardization is a relatively simple process. For each data value, x, we subtract the overall mean of the data, μ, then divide by the overall standard deviation, σ. The new value, z, represents the standardized data value. Thus, the formula for data standardization is: z = (x-μ)/σ
        pass
    
    if 1:#NumPy and scikit-learn -->scale(ndarray)
        print('{}\n'.format(repr(main_df)))
        
        # Standardizing each column of pizza_data
        col_standardized = scale(main_df)
        print('{}\n'.format(repr(col_standardized)))
        print(type(col_standardized))
        
        # Column mean values (rounded to nearest thousandth)
        col_means = col_standardized.mean(axis=0).round(decimals=3)
        print('{}\n'.format(repr(col_means)))
        
        # Column standard deviations
        col_stds = col_standardized.std(axis=0)
        print('{}\n'.format(repr(col_stds)))
        
        #row wise mean values and std. variations
        row_means = col_standardized.mean(axis=1).round(decimals=2)
        row_stds = col_standardized.std(axis=1).round(decimals=3)
        print(repr(row_means),row_stds)
        
if 0:#Data Range:
        from sklearn.preprocessing import MinMaxScaler
        if 1:#Range compression in scikit-learn
            default_scalar = MinMaxScaler()#default range is [0,1]
            transformed = default_scalar.fit_transform(main_df)
            print(main_df)
            print(transformed)
            
            custom_scalar = MinMaxScaler(feature_range=[-3,3])
            scaled_data = custom_scalar.fit_transform(main_df)
            print(main_df)
            print(scaled_data)
            
        if 0:#fit and transform separately  ***IMPORTANT
            data = np.array([[-2, -1, -2],
                             [ 0,  0,  0],
                             [-2, -1, -1],
                             [-1,  2,  0]])
            print(data)
            
            default_scalar=MinMaxScaler()
            default_scalar.fit(data)
            scaled_data = default_scalar.transform(main_df)
            print(scaled_data)
            
if 0:#Robust scaling
    from sklearn.preprocessing import RobustScaler
    if 1:#Data Outliers
        # In general terms, an outlier is a data point that is significantly further away from the other data points. For example, if we had watermelons of weights 5, 4, 6, 7, and 20 pounds, the 20 pound watermelon is an outlier.
        # The data scaling methods from the previous two chapters are both affected by outliers. Data standardization uses each feature's mean and standard deviation, while ranged scaling uses the maximum and minimum feature values, meaning that they're both susceptible to being skewed by outlier values.
        # We can robustly scale the data, i.e. avoid being affected by outliers, by using use the data's median and Interquartile Range (IQR). Since the median and IQR are percentile measurements of the data (50% for median, 25% to 75% for the IQR), they are not affected by outliers. For the scaling method, we just subtract the median from each data value then scale to the IQR.
        pass

    if 0:#Robust scaling with scikit-learn
        robust_scalar = RobustScaler()
        scaled_data = robust_scalar.fit_transform(main_df)
        print(scaled_data)
        
if 0:#Normalizing the data
    from sklearn.preprocessing import Normalizer
    if 1:#L2 Normalization
        #Normalization will be applied to the particular row(data observations) where as scaling applied to features/columns.
        # L2 norm of a row is just the square root of the sum of squared values for the row.
        
        df = pd.read_excel('Grouping.xls',index_col=0,sheet_name='Sheet3')
        main_df = df[['Hits','Runs','Matches']]
        print(main_df)
        
        normalizer = Normalizer()
        transformed = normalizer.fit_transform(main_df)
        print(transformed)
        
if 0:#Data Imputation -->filling the missed values 
    from sklearn.impute import SimpleImputer
    if 0:#Data Imputations methods
        arr = np.array([[ 1.,  2., np.nan,  2.],
                        [ 5., np.nan,  1.,  2.],
                        [ 4., np.nan,  3., np.nan],
                        [ 5.,  6.,  8.,  1.],
                        [np.nan,  7., np.nan,  0.]])
        print(arr)
        # print(np.arange(20).reshape(4,5))
        
        #replacing the missed data Using the mean value of columns
        impute_mean = SimpleImputer()
        result = impute_mean.fit_transform(arr)
        # print(result)
        
        #replacing the missed data Using the median value of columns
        impute_mean = SimpleImputer(strategy='median')
        result = impute_mean.fit_transform(arr)
        # print(result)
        
        #replacing the missed data Using the most frequent value of columns
        impute_mean = SimpleImputer(strategy='most_frequent')
        result = impute_mean.fit_transform(arr)
        # print(result)
        
        #replacing the missed data Using the constant value
        impute_mean = SimpleImputer(strategy='constant',fill_value=3)
        result = impute_mean.fit_transform(arr)
        print(result)
        
    if 1:#Other imputation methods
        # There are also more advanced imputation methods such as k-Nearest Neighbors (filling in missing values based on similarity scores from the kNN algorithm) and MICE (applying multiple chained imputations, assuming the missing values are randomly distributed across observations).
        pass
        
if 0:#Principal Component Analysis(PCA)
    from sklearn.decomposition import PCA
    if 0:#Dimensionality Reduction
        # Most datasets contain a large number of features, some of which are redundant or not informative.
        # When a dataset contains these types of correlated numeric features, we can perform principal component analysis (PCA) for dimensionality reduction (i.e. reducing the number of columns in the data array).
        # PCA extracts the principal components of the dataset, which are an uncorrelated set of latent variables that encompass most of the information from the original dataset.
        pass
        
    if 0:#PCA in scikit-learn PCA(n_components)
        # we can use the n_components keyword to specify the number of principal components. The default setting is to extract m - 1 principal components, where m is the number of features in the dataset.
        df = pd.read_excel('Grouping.xls',index_col=0,sheet_name='Sheet3')
        main_df = df[['Hits','Runs','HR','Matches']]
        print(main_df)
        
        pca_obj = PCA()#default n_components ==> columns-1
        result = pca_obj.fit_transform(main_df).round(3)
        # print(result)
        
        pca_obj = PCA(n_components=3)
        result = pca_obj.fit_transform(main_df)
        print(result)
        
if 1:#Labeled Data
    from sklearn.datasets import load_breast_cancer
    # A big part of data science is classifying observations in a dataset into separate categories, or classes. 
    if 0:#Class labels
        bc = load_breast_cancer()# collected the info.
        
        # Array contains size of tumors
        data_set = bc.data
        print(data_set)
        print(data_set.shape)#569 observations from 30 hospitals
        
        # Class labels i.e the tumors array will be classified by this array It means all the rows will be separated into groups(labels)
        labels_array = bc.target
        print(labels_array)
        print(labels_array.shape)
        
        # Labels names
        print(bc.target_names)#In labels array,0==> malignant,1 ==>benign
        
        # separating the tumors dataset into malignant dataset and benign datasets
        malignant_data_set = data_set[labels_array == 0]
        benign_data_set = data_set[labels_array == 1]
        
        # shapes of  labelled datasets
        print(malignant_data_set.shape) #212 observations from 30 hospitals considered as malignant
        print(benign_data_set.shape) #357 observations from 30 hospitals considered as benign
        
    if 1:# coding data
        def get_label_info(component_data, labels,
                   class_label, label_names):
          # getting malignant/benign names
          label_name = label_names[class_label]
          
          #separating the data baesd on class label represents label name
          label_data = component_data[labels == class_label]
          
          return  label_name,label_data
        
        def separate_data(component_data, labels,
                  label_names):
          separated_data = []
          #sending separate class ID to separate the dataset to the particluar ID
          for class_label in range(len(label_names)):
              a = get_label_info(component_data,labels,class_label,label_names)
              separated_data.append(a)
        
          return separated_data
    
        
        from sklearn.datasets import load_breast_cancer
        from sklearn.decomposition import PCA
        bc = load_breast_cancer()
        pca_obj = PCA(n_components=2)
        component_data = pca_obj.fit_transform(bc.data)
        labels = bc.target
        label_names = bc.target_names
        # Using the completed separate_data function
        separated_data = separate_data(component_data,
                                       labels, label_names)
        
        # Plotting the data
        import matplotlib.pyplot as plt
        # print(separated_data[0][1]) #represents malignant observations from 2 hospitals 
        # print(separated_data[1][1]) #represents benign observations from 2 hospitals 
        for label_name, label_data in separated_data:
          col1 = label_data[:, 0]  # 1st column (1st pr. comp.)
          col2 = label_data[:, 1]  # 2nd column (2nd pr. comp.)
          plt.scatter(col1, col2, label=label_name) # scatterplot
        plt.legend()  # adds legend to plot
        plt.title('Breast Cancer Dataset PCA Plot')
        plt.show()
        
        
        
        
        
        
        
        
        
        
        
        
        
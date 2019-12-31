# Import all packagees and set plots to be embedded inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# load Customer Data dataset into a pandas dataframe

# Data Wrangling (Data Munging)
# General Properties
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
# visually assess the data set
df.head()
# shape of data set
print(df.shape)
# summary
df.info()
# check data types of each column
df.dtypes
# check duplicates within data set
sum(df.duplicated())
# check null entries within data set
df.isnull().sum()
# Count how many churners and non-churners the dataset contains. 
"""df['Churn'].value_counts()
Discuss each column here:
- `customerID` - contains random values and has no effect on customer leaving telecommunications company.
- `gender` - may play a role in a customer leaving the company. This column will be included.
- `SeniorCitizen` - may play a role in a customer leaving the company. This column will be included.
- `Partner` - may play a role in a customer leaving the company. This column will be included.
- `Dependents` - may play a role in a customer leaving the company. This column will be included.
- `tenure` - refers to the number of years the customer has been a client of the company. It may play a role in a customer leaving the company. This column will be included.
- `PhoneService` - may play a role in a customer leaving the company. This column will be included.
- `MultipleLines` - may play a role in a customer leaving the company. This column will be included.
- `InternetService` - may play a role in a customer leaving the company. This column will be included.
- `OnlineSecurity` - may play a role in a customer leaving the company. This column will be included.
- `OnlineBackup` - may play a role in a customer leaving the company. This column will be included.
- `DeviceProtection` - may play a role in a customer leaving the company. This column will be included.
- `TechSupport` - may play a role in a customer leaving the company. This column will be included.
- `StreamingTV` - may play a role in a customer leaving the company. This column will be included.
- `StreamingMovies` - may play a role in a customer leaving the company. This column will be included.
- `Contract` - may play a role in a customer leaving the company. This column will be included.
- `PaperlessBilling` - may play a role in a customer leaving the company. This column will be included.
- `PaymentMethod` - may play a role in a customer leaving the company. This column will be included.
- `MonthlyCharges` - may play a role in a customer leaving the company. This column will be included.
- `TotalCharges` - may play a role in a customer leaving the company. This column will be included.
- `Churn` - whether or not the customer has left the company. This is what I will be predicting.
## Issues
- We have some non-numeric data"""

# Model Outcomes
## Two classes:
### yes = Customer will churn.
### no = Customer will not churn.
# Exploratory Analysis
## Differences between churners and non-churners
### Do churners call customer service more often?
### Does one state have more churners compared to another?
## Grouping and summarizing data
### .groupby()
# Total charges contain entries that are not floats. Use ‘coerce’ - invalid parsing will be set as NaN
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors = 'coerce')
df.loc[df['TotalCharges'].isna()==True]
# `tenure = 0` for `TotalCharges` columns. Convert TotalCharges to 0 for these entries.
df[df['TotalCharges'].isna()==True] = 0
# Unique values for categorical column entries
df.gender.unique()
df.Partner.unique()
# Group df by 'Churn' and compute the mean
df.groupby(['Churn']).mean()
df.groupby(['Churn']).median()
# Group df by 'Churn' and compute the standard deviation
df.groupby(['Churn']).std()
df.groupby('gender')['Churn'].value_counts()
df.groupby('SeniorCitizen')['Churn'].value_counts()

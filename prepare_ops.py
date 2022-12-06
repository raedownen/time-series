import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from env import user, password, host
import os
from acquire import wrangle_store_data
import warnings
warnings.filterwarnings("ignore")

# plotting defaults
plt.rc('figure', figsize=(13, 7))
plt.style.use('seaborn-whitegrid')
plt.rc('font', size=16)

def get_opsd_data():
    if os.path.exists('opsd.csv'):
        return pd.read_csv('opsd.csv')
    df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
    df.to_csv('opsd.csv', index=False)
    return df




def convert_datetime():
    df.Date = pd.to_datetime(df.Date)

def plot_univariate():
    # Univariate analysis of variable distributions
    for col in df.columns:
        print('Column: ' + col)
        plt.figure(figsize=(8,4))
        plt.hist(df[col], edgecolor='black')
        plt.show()

# Set the index as that date and then sort index (by the date)
df = df.set_index("Date").sort_index()
        
# make sure all time intervals are there        
def look_for_missing_time():
    print('Number of rows:', df.index.nunique())
    # timedeltabecause subtraction of a date range will be one less
    n_days = df.index.max() - df.index.min() + pd.Timedelta('1d')
    print(f"Number of days between first and last day:", n_days)
    
# fill in nulls or nan
def null_filler():
    df.fillna(df.mean(numeric_only=True).round(1), inplace=True)
        
def prep_ops_data(df):
    # Reassign the sale_date column to be a datetime type
    df.Date = pd.to_datetime(df.Date)

    # Sort rows by the date and then set the index as that date
    df = df.set_index("Date").sort_index()
    return df
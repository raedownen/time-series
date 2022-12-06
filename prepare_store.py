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


# convert the sale_date from object to date time
def convert_datetime():
    df.sale_date = pd.to_datetime(df.sale_date)


# plot the sale amount by date
def by_date():
    by_date = df.groupby(['sale_date']).sale_amount.sum().reset_index()
    by_date.plot(x='sale_date', y='sale_amount')

    
# set index by datetime variable
def set_index():
    df = df.set_index("sale_date").sort_index()


# add month and day of week to df columns
def dt_variable():
    df['month'] = df.index.month
    df['day_of_week'] = df.index.day_name

    
# add total sales column - multiply the price by amount
def tot_sales():
    df['sales_total'] =  df['sale_amount'] * df['item_price']
    
################################################
    
def prep_store_data(df):
    # Reassign the sale_date column to be a datetime type
    df.sale_date = pd.to_datetime(df.sale_date)

    # Sort rows by the date and then set the index as that date
    df = df.set_index("sale_date").sort_index()
    return df
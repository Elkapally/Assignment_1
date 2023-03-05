# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 19:13:08 2023

@author: 91905
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Loading the Data
sales = pd.read_csv("D:\\Datasets\\Dataset\\sales_data_sample.csv" ,encoding='latin1')
sales.sort_values(by=['ORDERNUMBER'])

# Rename columns in lowercase
sales.columns= sales.columns.str.lower()

# Checking null values
sales.isnull().sum()

# Checking duplicate values
len(sales) == len(sales.drop_duplicates())

# Determining Countries with null valued Territory
sales.loc[sales['territory'].isnull()]['country'].unique()

# Assigning North America Territory values
sales['territory'] = sales['territory'].fillna('NAM')
sales['territory'].unique()

# Removing the In Process and Cancelled orders
sales['status'].unique()

sales1 = sales[~((sales['status'] == 'Cancelled') | (sales['status'] == 'On Hold'))]
sales1['status'].unique()

# Monthly Revenue for 2003 - 2005
def plot_monthly_revenue(sales1):
    """
    Plots the monthly revenue for a given sales dataset.

    Parameters:
    -----------
    sales1: pandas.DataFrame
        A dataframe containing sales data

    Returns:
    --------
    None
    """
    plt.figure(figsize=(15,12))

    monthly_revenue = sales1.groupby(['year_id','month_id'])['sales'].sum().reset_index()

    plt.plot(monthly_revenue['month_id'], monthly_revenue['sales'][monthly_revenue['year_id'] == 2003], label='2003')
    plt.plot(monthly_revenue['month_id'], monthly_revenue['sales'][monthly_revenue['year_id'] == 2004], label='2004')
    plt.plot(monthly_revenue['month_id'], monthly_revenue['sales'][monthly_revenue['year_id'] == 2005], label='2005')
    plt.title('Monthly Revenue', fontsize = 20)
    plt.xlabel('Month', fontsize = 16)
    plt.ylabel('Sales', fontsize = 16)
    plt.legend()

plot_monthly_revenue(sales1)
plt.show()

# Number of Sale Lines for Regions barplot
def plot_sale_lines_by_region(sales1):
    """
    Plots the number of sale lines for each region in a given sales dataset.

    Parameters:
    -----------
    sales1: pandas.DataFrame
        A dataframe containing sales data, with a column "territory" representing the region for each sale.

    Returns:
    --------
    None
    """
    plt.figure(figsize=(20,10))
    sales1['territory'].value_counts().plot(kind='bar')
    plt.title('Number of Sale Lines for Regions', fontsize = 20)
    plt.ylabel('Number of Orderlines', fontsize = 16)
    plt.xlabel('Regions', fontsize = 16)

plot_sale_lines_by_region(sales1)
plt.show()

# Product line distribution pie chart
def plot_product_line_distribution(sales1):
    """
    Plots the distribution of product lines in a given sales dataset.

    Parameters:
    -----------
    sales1: pandas.DataFrame
        A dataframe containing sales data, with a column "productline" representing the product line for each sale.

    Returns:
    --------
    None
    """
    plt.figure(figsize=(15,12))
    sales1['productline'].value_counts().plot(kind='pie')
    plt.title('Product Line Distribution')
    plt.xlabel('Product Line')
    plt.ylabel('Number of Orderlines')

plot_product_line_distribution(sales1)
plt.show()
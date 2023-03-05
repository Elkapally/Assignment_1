#Importing Packages
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score

"""# Loading the Data"""

sales = pd.read_csv('/content/sales_data_sample.csv',encoding='latin1')
sales.sort_values(by=['ORDERNUMBER'])

# Rename columns in lowercase
sales.columns= sales.columns.str.lower()
sales.columns.values

sales.describe()

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

"""# Monthly Revenue for 2003 - 2005"""

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

    sns.lineplot(x="month_id", y="sales",hue="year_id", data=monthly_revenue)
    plt.title('Monthly Revenue', fontsize = 20)
    plt.xlabel('Month', fontsize = 16)
    plt.ylabel('Sales', fontsize = 16)

plot_monthly_revenue(sales1)
plt.show()

"""<span style="font-size:18px;">2005 sales for the first 5 months are higher than previous years except for April. The monthly sales trends at peaked on November.</span>

## Number of Sale Lines for Regions barplot
"""

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
    sns.countplot(x = sales1['territory'], order = sales1['territory'].value_counts().index )
    plt.title('Number of Sale Lines for Regions', fontsize = 20)
    plt.ylabel('Number of Orderlines', fontsize = 16)
    plt.xlabel('Regions', fontsize = 16)
  
plot_sale_lines_by_region(sales1)
plt.show()

"""<span style="font-size:18px;">The most of sales are happened at EMEA region. The NAM region which USA is in it is the second most sold region.</span>

#Product line distribution pie chart
"""

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

"""The most of the sales are belong Classic Cars category. Vintage Cars and Motorcycles are the second and third ones. 
The least of sales are happened in Trains category. """
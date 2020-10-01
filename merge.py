# pandas module needed
# https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html
# for reading excel files xlrd module also needed (probably)
# https://xlrd.readthedocs.io/en/latest/installation.html

import pandas as pd

# for reading in csv files
# dataframe1 = pd.read_csv('data1.csv')
# dataframe2 = pd.read_csv('data2.csv')

# for reading excels

dataframe1 = pd.read_excel('data1.xlsx')
dataframe2 = pd.read_excel('data2.xlsx')

# drop duplicate rows based on isbn column

dataframe1.drop_duplicates(subset=['isbn'],inplace=True)
dataframe2.drop_duplicates(subset=['isbn'],inplace=True)

# join the two datasets so you have all records from both datasets
# this is the how='outer' - it means outer join (you can google that if interested)
# indicator=True creates a new column 
# that shows if isbn value was in:
# both datasets, left dataset, right dataset

merged_df = pd.merge(dataframe1,dataframe2,how='outer',indicator=True)

# create new datasets that include out only rows that 
# were in left or right datasets

left_df = merged_df[merged_df['_merge'] == 'left_only']
right_df = merged_df[merged_df['_merge'] == 'right_only']

# save the dataframes to disk as csv files

left_df.to_csv('left_df.csv')
right_df.to_csv('right_df.csv')

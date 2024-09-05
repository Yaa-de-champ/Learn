# Importing relevant libraries 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# # PART 1: DATA LOADING AND CLEANING
# #Load the csv file
# df = pd.read_csv('sales_data.csv')

# # Check for missing values
# print(df.isnull().sum())
# print(df.isnull().any().any()) #answer: False


# # Convert Date to datetime
# df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
# df.head()


# # Ensure numeric columns have correct data types
# numeric_columns = ['Sales', 'Expenses', 'Profit']
# df[numeric_columns] = df[numeric_columns].astype(float)
# print(df.dtypes)


# # Part 2: DATA VISUALIATION AND GRAPH PLOTTING
# # Line Plot
# plt.figure(figsize=(12, 6))
# plt.plot(df['Date'], df['Sales'], label='Sales')
# plt.title('Sales over Time')
# plt.xlabel('Date')
# plt.ylabel('Sales')
# plt.title('Sales Over Time')
# plt.legend()
# plt.grid(True)
# plt.savefig('sales_over_time.png')
# plt.close()

# # Scatter Plot
# plt.figure(figsize=(10, 6))
# plt.scatter(df['Expenses'], df['Profit'])
# plt.title('Expenses vs Profit')
# plt.xlabel('Expenses')
# plt.ylabel('Profit')
# plt.title('Expenses vs Profit')
# plt.savefig('expenses_vs_profit.png')
# plt.grid(True)
# plt.close()

# # Histogram
# plt.figure(figsize=(10, 6))
# plt.hist(df['Sales'], bins=20, alpha=0.5)
# plt.title('Distribution of Sales')
# plt.xlabel('Sales')
# plt.ylabel('Frequency')
# plt.title('Histogram of Sales')
# plt.savefig('sales_histogram.png')
# plt.close()
# plt.grid(True)

# # Part 3: CORRELATION ANALYSIS
# # Correlation Matrix
# corr_matrix = df[numeric_columns].corr()
# plt.figure(figsize=(10, 8))
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
# plt.title('Correlation Matrix')
# plt.savefig('correlation_matrix.png')
# plt.close()

# # Correlation Coefficient
# sales_profit_corr = df['Sales'].corr(df['Profit'])
# print(f"Correlation between Sales and Profit: {sales_profit_corr}")
# # answer: Correlation between Sales and Profit: -0.01686665795541729


# # Part 4: ADVANCED VISUALIZATION AND ANALYSIS
# #Box Plot
# plt.figure(figsize=(12, 6))
# sns.boxplot(x='Region', y='Sales', data=df)
# plt.title('Distribution of Sales by Region')
# plt.savefig('sales_boxplot.png')
# plt.close()


# #Time Series Analysis
# #  Resample data to monthly frequency and plot the monthly average Sales
# df.set_index('Date', inplace=True)
# monthly_sales = df['Sales'].resample('ME').mean()
# plt.figure(figsize=(12, 6))
# plt.plot(monthly_sales.index, monthly_sales, label='Monthly Average Sales')
# plt.xlabel('Date')
# plt.ylabel('Average Sales')
# plt.title('Monthly Average Sales')
# plt.legend()
# plt.savefig('average_sales.png')
# plt.show()
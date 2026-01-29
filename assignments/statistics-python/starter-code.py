"""
Statistics with Python Starter Code

This starter code provides the basic structure for analyzing data using pandas and numpy.
Complete the tasks by implementing statistical calculations and visualizations.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# TODO: Load your CSV file
# df = pd.read_csv('your_dataset.csv')

# Task 1: Load and Explore Data
# TODO: Display dataset shape
# print(f"Dataset shape: {df.shape}")

# TODO: Display data types and missing values
# print(df.info())

# TODO: Display summary statistics
# print(df.describe())

# TODO: Check for missing values
# print(df.isnull().sum())

# TODO: Display first and last rows
# print("First 5 rows:")
# print(df.head())
# print("\nLast 5 rows:")
# print(df.tail())


# Task 2: Compute Descriptive Statistics
# TODO: Calculate mean, median, mode for each numerical column
# for column in df.select_dtypes(include=[np.number]).columns:
#     print(f"{column}:")
#     print(f"  Mean: {df[column].mean()}")
#     print(f"  Median: {df[column].median()}")
#     print(f"  Mode: {df[column].mode().values}")

# TODO: Calculate standard deviation and variance
# print(f"\nStandard Deviation:\n{df.std()}")
# print(f"\nVariance:\n{df.var()}")

# TODO: Calculate quartiles and IQR
# print(f"\nQuartiles (Q1, Q2, Q3):")
# for column in df.select_dtypes(include=[np.number]).columns:
#     q1 = df[column].quantile(0.25)
#     q2 = df[column].quantile(0.50)
#     q3 = df[column].quantile(0.75)
#     iqr = q3 - q1
#     print(f"{column}: Q1={q1}, Q2={q2}, Q3={q3}, IQR={iqr}")

# TODO: Identify outliers using IQR method
# for column in df.select_dtypes(include=[np.number]).columns:
#     Q1 = df[column].quantile(0.25)
#     Q3 = df[column].quantile(0.75)
#     IQR = Q3 - Q1
#     outliers = df[(df[column] < Q1 - 1.5*IQR) | (df[column] > Q3 + 1.5*IQR)]
#     print(f"Outliers in {column}: {len(outliers)}")

# TODO: Calculate correlation matrix
# correlation_matrix = df.corr()
# print(f"\nCorrelation Matrix:\n{correlation_matrix}")


# Task 3: Data Manipulation and Aggregation
# TODO: Filter data based on conditions
# filtered_df = df[df['column_name'] > value]

# TODO: Create new calculated columns
# df['new_column'] = df['column1'] + df['column2']

# TODO: Group and aggregate data
# grouped = df.groupby('category_column').agg({
#     'numeric_column': ['mean', 'sum', 'count']
# })
# print(grouped)

# TODO: Sort data
# sorted_df = df.sort_values(by=['column_name'], ascending=False)

# TODO: Create summary report
# summary = df.groupby('category').agg({
#     'numeric_col': ['count', 'mean', 'std', 'min', 'max']
# })
# print(summary)


# Task 4: Visualize Statistical Distributions
# TODO: Create histograms
# plt.figure(figsize=(10, 6))
# plt.hist(df['column_name'], bins=30, edgecolor='black')
# plt.xlabel('Column Name')
# plt.ylabel('Frequency')
# plt.title('Distribution of Column Name')
# plt.savefig('histogram.png')
# plt.show()

# TODO: Create box plots
# plt.figure(figsize=(10, 6))
# df.boxplot(column='numeric_column', by='category_column')
# plt.title('Box Plot by Category')
# plt.suptitle('')  # Remove default title
# plt.savefig('boxplot.png')
# plt.show()

# TODO: Create scatter plots
# plt.figure(figsize=(10, 6))
# plt.scatter(df['column1'], df['column2'], alpha=0.6)
# plt.xlabel('Column 1')
# plt.ylabel('Column 2')
# plt.title('Relationship between Column 1 and Column 2')
# plt.savefig('scatter_plot.png')
# plt.show()

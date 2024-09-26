# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# Load the dataset
df = pd.read_csv('dataset.csv')

# View dataset information
print(df.info())
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Univariate analysis
for col in df.columns:
    if df[col].dtype in ['int64', 'float64']:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[col], bins=50, kde=True)
        plt.title(f'Distribution of {col}')
        plt.show()

# Bivariate analysis
for col1 in df.columns:
    for col2 in df.columns:
        if df[col1].dtype in ['int64', 'float64'] and df[col2].dtype in ['int64', 'float64']:
         plt.figure(figsize=(8, 6))
        sns.scatterplot(x=df[col1], y=df[col2])
        plt.title(f'Relationship between {col1} and {col2}')
        plt.show()

# Multivariate analysis
corr = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Pairplot
sns.pairplot(df)
plt.show()


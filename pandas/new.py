import pandas as pd

# Load dataset (replace 'population.csv' with the path to your file)
df = pd.read_csv('population.csv')

# 1. Inspect the Data
print("First 5 rows of the dataset:")
print(df.head())

print("\nBasic Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# 2. Check for Missing Data
print("\nMissing Values per Column:")
print(df.isnull().sum())

# 3. Handle Missing Data (Example: Fill with mean or drop)
df_cleaned = df.fillna(df.mean())  # Fill missing values with column means
# Alternatively, drop rows with missing values
# df_cleaned = df.dropna()

# 4. Data Analysis - Grouping and Aggregation
# Example: Group by a column and calculate the mean of other columns
grouped_data = df_cleaned.groupby('Category').mean()
print("\nMean values by Category:")
print(grouped_data)

# 5. Filter Data
# Example: Filter rows where a column 'Sales' is greater than 500
filtered_data = df_cleaned[df_cleaned['Sales'] > 500]
print("\nFiltered Data (Sales > 500):")
print(filtered_data)

# 6. Correlation Analysis
print("\nCorrelation between numerical columns:")
print(df_cleaned.corr())

# 7. Save the cleaned data to a new CSV file
df_cleaned.to_csv('cleaned_data.csv', index=False)

# Optional: Plotting (if you want to visualize the data)
import matplotlib.pyplot as plt
df_cleaned['Sales'].hist(bins=20)
plt.title('Sales Distribution')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

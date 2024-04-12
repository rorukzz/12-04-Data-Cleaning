import pandas as pd
import matplotlib as plt

# Read the CSV file
df = pd.read_csv('annual-enterprise-survey-2021-financial-year-provisional-csv.csv')

# Convert the 'Value' column to numeric
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')  # 'coerce' will convert non-numeric values to NaN

# Group by 'Year' and 'Industry_name_NZSIOC' and sum the 'Value' column
grouped_df = df.groupby(['Year', 'Industry_name_NZSIOC']).agg({'Value': 'sum'}).sort_values(by='Year', ascending=False).reset_index()

# Rename the 'Value' column to 'Total_Value' if needed
grouped_df.rename(columns={'Value': 'Total_Value'}, inplace=True)

# Write the result to a CSV file
grouped_df.plot()

plt.show()

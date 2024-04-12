import pandas as pd

df = pd.read_csv('annual-enterprise-survey-2021-financial-year-provisional-csv.csv')

grouped_df = df.groupby('Industry_name_NZSIOC')

print(grouped_df)
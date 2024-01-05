import pandas as pd
import os

def load_data():
 data = []
 directory = os.getcwd() # Get the current working directory
 for filename in os.listdir(directory):
     if filename.endswith(".csv"):
         df = pd.read_csv(os.path.join(directory, filename), usecols=['Status', 'Original estimate'])
         print(f"Columns in {filename}: {df.columns}")
         if 'Status' in df.columns and 'Original estimate' in df.columns:
             df = df.sort_values('Status')
             print(df[['Status', 'Original estimate']].head())
             data.append(df[['Status', 'Original estimate']])
 if data:
     result = pd.concat(data, ignore_index=True)
     result.to_csv('result.csv', index=False)
     grouped = result.groupby('Status')['Original estimate'].sum().div(8).div(3600).reset_index()
     grouped.to_csv('grouped.csv', index=False)
 else:
     print("No CSV files found with 'Status' and 'Original estimate' columns.")

load_data()

import pandas as pd
import os

def efforts_by_status():
 data = []
 directory = os.getcwd() # Get the current working directory
 for filename in os.listdir(directory):
     if filename.endswith(".csv"):
         df = pd.read_csv(os.path.join(directory, filename), usecols=['Status', 'Original estimate'])
         if 'Status' in df.columns and 'Original estimate' in df.columns:
             df = df.sort_values('Status')
             data.append(df[['Status', 'Original estimate']])
 if data:
     result = pd.concat(data, ignore_index=True)
     grouped = result.groupby('Status')['Original estimate'].sum().div(8).div(3600).round(3).reset_index()
     grouped.to_csv('grouped.csv', index=False)
     print(grouped)
 else:
     print("No CSV files found with 'Status' and 'Original estimate' columns.")

def count_sprint_columns():
 directory = os.getcwd() # Get the current working directory
 for filename in os.listdir(directory):
     if filename.endswith(".csv") and filename != "grouped.csv":
         df = pd.read_csv(os.path.join(directory, filename))
         sprint_columns = sum([col.startswith('Sprint') for col in df.columns])
         print(f"File {filename} has {sprint_columns} 'Sprint' columns.")

efforts_by_status()
count_sprint_columns()

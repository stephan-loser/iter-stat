import pandas as pd
import os

def make_directory():
    directory = os.getcwd() # Get the current working directory
    results_dir = os.path.join(directory, 'results')
    os.makedirs(results_dir, exist_ok=True)  # Ensure the 'results' directory exists
    return results_dir

def efforts_by_status():
    data = []
    directory = os.getcwd() # Get the current working directory
    for filename in os.listdir(directory):
        if filename.endswith(".csv") and not filename.startswith(("blacklisted")):
            print(filename)
            df = pd.read_csv(os.path.join(directory, filename), usecols=['Status', 'Original estimate'])
            if 'Status' in df.columns and 'Original estimate' in df.columns:
                df = df.sort_values('Status')
                data.append(df[['Status', 'Original estimate']])
    if data:
        result = pd.concat(data, ignore_index=True)
        grouped = result.groupby('Status')['Original estimate'].sum().div(8).div(3600).round(3).reset_index()
        # grouped.fillna(0, inplace=True)  # Ensure all statuses have an entry

        # Calculate 'unfinished' and 'finished'
        unfinished = grouped.loc[grouped['Status'].str.lower() == 'to do', 'Original estimate'].sum() + \
                     + grouped.loc[grouped['Status'].str.lower() == 'backlog', 'Original estimate'].sum() + \
                     0.5 * grouped.loc[grouped['Status'].str.lower() == 'in progress', 'Original estimate'].sum()
        finished = grouped.loc[grouped['Status'].str.lower() == 'done', 'Original estimate'].sum() + \
                   grouped.loc[grouped['Status'].str.lower() == 'in review', 'Original estimate'].sum() + \
                   0.5 * grouped.loc[grouped['Status'].str.lower() == 'in progress', 'Original estimate'].sum()

        # Create a DataFrame with values for finished and unfinished
        un_finished = pd.DataFrame({
            'Status': ['unfinished', 'finished'],
            'Original estimate': [unfinished, finished]
        })
        results_dir = make_directory()
        grouped.to_csv(os.path.join(results_dir, 'grouped.csv'), index=False)
        print(grouped)
        un_finished.to_csv(os.path.join(results_dir, 'un_finished.csv'), index=False)
        print(un_finished)
    else:
        print("No CSV files found with 'Status' and 'Original estimate' columns.")

def count_sprint_columns():
 directory = os.getcwd() # Get the current working directory
 for filename in os.listdir(directory):
     if filename.endswith(".csv") and not filename.startswith(("blacklisted")):
         df = pd.read_csv(os.path.join(directory, filename))
         sprint_columns = sum([col.startswith('Sprint') for col in df.columns])
         print(f"File {filename} has {sprint_columns} 'Sprint' columns.")

efforts_by_status()
count_sprint_columns()

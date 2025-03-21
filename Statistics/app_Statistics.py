### main_Statistics.py
This file will contain the backend logic to compute statistics for the provided input.


import pandas as pd

def process_input(input_data):
    # Split the input data by comma and strip any extra spaces
    data = [item.strip() for item in input_data.split(',')]
    return data

def generate_statistics(data):
    # Convert the data into a DataFrame
    df = pd.DataFrame(data, columns=['Observations'])

    # Determine if data is numerical or not
    try:
        df['Observations'] = pd.to_numeric(df['Observations'])
        is_numeric = True
    except ValueError:
        is_numeric = False

    # Generate statistics
    if is_numeric:
        stats = {
            'Count': df['Observations'].count(),
            'Mean': df['Observations'].mean(),
            'Standard Deviation': df['Observations'].std(),
            'Minimum': df['Observations'].min(),
            'Maximum': df['Observations'].max(),
            '25th Percentile': df['Observations'].quantile(0.25),
            '50th Percentile (Median)': df['Observations'].median(),
            '75th Percentile': df['Observations'].quantile(0.75)
        }
    else:
        stats = {
            'Count': df['Observations'].count(),
            'Unique': df['Observations'].nunique(),
            'Most Frequent': df['Observations'].mode()[0]
        }

    return stats


###
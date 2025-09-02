import pandas as pd
import os

def load_data(file_path):
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        return df
    else:
        raise FileNotFoundError(f"The file {file_path} does not exist.")

def clean_data(df):
    df.dropna(inplace=True)
    # Additional cleaning steps can be added here
    return df

def process_data(file_path):
    df = load_data(file_path)
    df = clean_data(df)
    # Additional processing steps can be added here
    return df

def prepare_data_for_visualization(df):
    # Example of preparing data for visualization
    df['DATE'] = pd.to_datetime(df['APPOINTMENT_MONTH'], format='%b%Y')
    return df
import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df[['trip_duration']]

def split_data(df, fraction):
    return df.sample(frac=fraction, random_state=42)

def sort_and_filter(df):
    # Misalnya filter durasi lebih dari 1000 detik, lalu sort naik
    return df[df['trip_duration'] > 1000].sort_values(by='trip_duration')

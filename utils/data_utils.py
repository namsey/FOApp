import pandas as pd


# Example utility function to clean financial data (if necessary)
def clean_data(df):
    # Removing rows with NaN values
    df = df.dropna()
    return df


# Example utility to split train and test data
def split_data(df, test_size=0.2):
    split_index = int(len(df) * (1 - test_size))
    train_data = df[:split_index]
    test_data = df[split_index:]
    return train_data, test_data

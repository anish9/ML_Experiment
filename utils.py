import pandas as pd


def pandas_label_encode(series: pd.Series):
    unique_vals = sorted(series.unique()) 
    val_to_encoded = {val: i for i, val in enumerate(unique_vals)}
    encoded_series = series.map(val_to_encoded)
    return encoded_series, val_to_encoded


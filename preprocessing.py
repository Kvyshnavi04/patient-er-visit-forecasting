
import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df.fillna(method='ffill', inplace=True)
    return df

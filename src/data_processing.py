import pandas as pd
import numpy as np

def load_data(filepath):
    return pd.read_csv(filepath)

def clean_data(df):
    cols_with_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    df[cols_with_zero] = df[cols_with_zero].replace(0, np.nan)
    df.fillna(df.mean(), inplace=True)
    return df

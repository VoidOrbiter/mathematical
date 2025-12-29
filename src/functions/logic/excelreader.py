import pandas as pd


def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df

def read_excel(file_path, sheet_name=0):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df

def df_to_numpy(df, columns=None):
    if columns:
        return df[columns].to_numpy()
    return df.to_numpy()
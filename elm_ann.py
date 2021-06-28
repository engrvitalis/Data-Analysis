import pandas as pd

def get_file(files):
    df = []
    for f in files:
        df.append(pd.read_csv(f))
    
    return df

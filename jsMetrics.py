import numpy as np
import pandas as pd

def boxplot(df,column):
    pass


if __name__ == "__main__":
    df = pd.read_excel('results-javascript.xlsx',nrows=1000)
    for col in df.columns:
        if df.dtypes[col] == 'int64':
            boxplot(df,col)
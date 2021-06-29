import pandas as pd
import matplotlib.pyplot as plt

def get_file(files):
    df = []
    for f in files:
        df.append(pd.read_csv(f))
    
    return df


def explore(df, ntarget):
    '''
    Plot the predictor variables against the target variables.
    It is assumed that the target variables is/are the last column(s).

    Input: Dataframe (df) and number of target variables (ntarget).
    Output: Subplots of each predictor variable against each target variable.
    Return: None
    '''
    pos = 1
    ncols = len(df.columns)-1

    plt.figure(figsize=[15, 5])
    for i in range(0, ncols):
        plt.subplot(1, ncols, pos)
        plt.scatter(df.iloc[:, i], df.iloc[:, -1])
        plt.ylabel(df.columns[-1])
        plt.xlabel(df.columns[i])
        pos += 1
    plt.tight_layout()
    plt.show()
    print('\n')
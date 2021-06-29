import pandas as pd
import matplotlib.pyplot as plt

def get_file(files):
    df = []
    for f in files:
        df.append(pd.read_csv(f))
    
    return df

def disp_subplot(df, ncols, ntarget, pos, i):
    for j in range(0, ncols):
        # Specify plot location in subplot.
        plt.subplot(1, ncols*ntarget, pos)
        # Plot predictor vs target.
        plt.scatter(df.iloc[:, j], df.iloc[:, -i])
        # Label the axis.
        plt.ylabel(df.columns[-i])
        plt.xlabel(df.columns[j])

        pos += 1
    return pos

def explore(df, ntarget=1):
    '''
    Plot the predictor variables against the target variables.
    It is assumed that the target variables is/are the last column(s).

    Input: Dataframe (df) and number of target variables (ntarget).
    Output: Subplots of each predictor variable against each target variable.
    Return: None
    '''
    # Initialize variables.
    pos = 1
    ncols = len(df.columns)-ntarget

    # Check if number of target variables is greater than 1.
    if ntarget < 2:
        i = ntarget
        # Set figure size for subplot.
        plt.figure(figsize=[10, 5])

        # Plot predictor vs target variables on a subplot for each file.
        for j in range(0, ncols):
            disp_subplot(df, ncols, ntarget, pos, i)
    else:
        # Set figure size for subplot.
        plt.figure(figsize=[15, 5])
        # Plot predictor vs target variables on a subplot for each file.
        for i in range(ntarget, 0, -1):
            pos = disp_subplot(df, ncols, ntarget, pos, i)
    plt.tight_layout()
    plt.show()
    print('\n')
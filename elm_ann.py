from numpy.core.fromnumeric import shape
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from scipy.linalg import pinv2
import numpy as np
import time

def get_file(files):
    df = []
    for f in files:
        df.append(pd.read_csv(f))
    
    return df

def disp_subplot(df, ncols, ntarget, pos, i):
    '''
    Displays the subplot of single or multiple predictor and target variables.

    Input: Dataframe (df), number of predictor variable columns (ncols), number of target variable(s) columns, (ntarget),
           plot position in a subplot (pos) and target variable column number (i).

    Output: A subplot containing all the predictor variable(s) against the target variable(s).
    Return: None.
    '''
    for j in range(0, ncols):
        # Specify plot location in subplot.
        plt.subplot(1, ncols*ntarget, pos)
        # Plot predictor vs target.
        plt.scatter(df.iloc[:, j], df.iloc[:, -i])
        # Label the axis.
        plt.ylabel(df.columns[-i])
        plt.xlabel(df.columns[j])

        pos += 1
    plt.suptitle('Predictor(s) vs Target(s)')
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

def generate_train_test(df, ntarget=1):
    '''
    Divide test data into test and training.
    '''
    X = df.iloc[:, :-ntarget]
    y = df.iloc[:, -ntarget:]

    return train_test_split(X, y,random_state=1, test_size=0.2)

def scale_data(X_train, X_test):
    '''
    Scale data for better prediction.
    '''
    sc_X = StandardScaler()
    X_trainscaled=sc_X.fit_transform(X_train)
    X_testscaled=sc_X.transform(X_test)

    return X_trainscaled, X_testscaled

def ann_analysis(X_train, y_train, X_test, y_test):
    '''
    Train, test and predict using ANN.
    '''
    X_trainscaled, X_testscaled = scale_data(X_train, X_test)
    reg = MLPRegressor(hidden_layer_sizes=(64, 64, 64), activation='relu', random_state=1, max_iter=5000).fit(X_trainscaled, y_train)

    y_pred = reg.predict(X_testscaled)
    r2 = r2_score(y_pred, y_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)

    return r2, rmse, mae, y_pred, reg

def elm_analysis(X_train, y_train, X_test, y_test, hidden_size=5000):
    '''
    Train, test and predict using ELM.
    '''
    input_size = X_train.shape[1]
    hidden_size = hidden_size
    input_weights = np.random.normal(size=[input_size,hidden_size])
    biases = np.random.normal(size=[hidden_size])

    def relu(x):
        return np.maximum(x, 0, x)

    def hidden_nodes(X):
        G = np.dot(X, input_weights)
        G = G + biases
        H = relu(G)
        return H

    output_weights = np.dot(pinv2(hidden_nodes(X_train)), y_train)

    def predict(X):
        out = hidden_nodes(X)
        out = np.dot(out, output_weights)
        return out

    y_pred = predict(X_test)
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)

    return r2, rmse, mae, y_pred

def disp_matrics(r2, rmse, mae, start, stop, title):
    '''
    Display important metrics for data.
    '''
    print(title)
    print('===============================================')
    print(f'R^2:\t\t{r2}')
    print(f'rmse:\t\t{rmse}')
    print(f'mae:\t\t{mae}')
    print(f'time(s)\t\t{stop - start}')
    print('\n')

def disp_graphs(i, y_test, y_ann_pred, y_elm_pred):
    '''
    Display graphs.
    '''
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.scatter(y_ann_pred, y_test)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=3)
    plt.title('ANN')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')

    plt.subplot(1, 2, 2)
    plt.scatter(y_elm_pred, y_test)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=3)
    plt.title('ELM')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')

    plt.suptitle('Visualizing Models Predictive Ability', x=.506, y=1.03, fontsize=16)
    plt.tight_layout()
    plt.show()

def disp_compare_graphs(ann_r2, ann_rmse, ann_mae, ann_time, elm_r2, elm_rmse, elm_mae, elm_time):
    '''
    Display comparison graphs.
    '''
    plt.figure(figsize = (10, 5))

    x = np.arange(4)
    ann = [ann_r2*100, ann_rmse, ann_mae, ann_time]
    elm = [elm_r2*100, elm_rmse, elm_mae, elm_time]
    width = 0.40

    # plot data in grouped manner of bar type
    plt.bar(x-0.2, ann, width, color='green')
    plt.bar(x+0.2, elm, width, color='red')
    plt.xticks(x, ['R^2', 'RMSE', 'MAE', 'TIME(S)'])
    plt.title("Visualizing Models Data Metrics")
    plt.xlabel("Metrics")
    plt.ylabel("Values")
    plt.legend(["ANN", "ELM"])
    plt.show()
"""Import the required modules"""
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from scipy.linalg import pinv2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def get_tables(file1, file2):
    
  # Reads in files.
  dfs = [pd.read_csv(file1), pd.read_csv(file2)]

  # Create dummies.
  for i, df in enumerate(dfs):
    dfs[i] = pd.get_dummies(df, drop_first=True)

  # Rearrange columns.
  dfs[0] = pd.concat([dfs[0].iloc[:, :4], dfs[0].iloc[:, -4:], dfs[0].iloc[:, 4:8]], axis=1)
  dfs[1] = pd.concat([dfs[1].iloc[:, :4], dfs[1].iloc[:, -3:], dfs[1].iloc[:, 4:9]], axis=1)

  return dfs

file1 = 'welding_data_by_properties.csv'
file2 = 'welding_data_by_welding_type.csv'


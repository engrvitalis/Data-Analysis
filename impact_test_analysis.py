"""Import the required modules"""
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from scipy.linalg import pinv2
import matplotlib.pyplot as plt
import numpy as np
import time

import elm_ann as ea

file = ('impact1.csv', 'impact2.csv')
df = ea.get_file(file)

print(df[0])
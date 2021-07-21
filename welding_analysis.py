"""Import the required modules"""
import time
import pandas as pd

import elm_ann as ea

# Read in files for analysis.
file = ('welding_data_by_welding_types.csv',)
df = ea.get_file(file)
df2 = pd.get_dummies(df).drop('heat_input', axis=1)

# # Explore the each file variables.
# for i in range(0, len(file)):
#     print('\nData Statistical Summary')
#     print(df[i].describe())
#     print('')

#     print('\nData Visualization')
#     ea.explore(df[i])

print('MODEL MATRICS.')
print('===============================================')

for i in range(0, len(file)):
    print('Welding Data:')
    print(df[i].iloc[:, :])
    # print(f'ANALYSIS OF FIBRE TABLE.')
    X_train, X_test, y_train, y_test = ea.generate_train_test(df[i])
    print('Test data')
    print(X_test)

    # for model in ['ANN', 'ELM']:

    #     if model == 'ANN':
    #         print('ANN modeling')
    #         start = time.time()
    #         ann_r2, ann_rmse, ann_mae, y_ann_pred, reg = ea.ann_analysis(X_train, y_train, X_test, y_test)
    #         stop = time.time()
    #         ann_time = stop - start

    #         print(f'Predicted values using ANN')
    #         print(y_ann_pred)
    #         ea.disp_matrics(ann_r2, ann_rmse, ann_mae, start, stop, 'The ANN model performance for testing set')
    #     else:
    #         print('ELM modeling')
    #         start = time.time()
    #         elm_r2, elm_rmse, elm_mae, y_elm_pred = ea.elm_analysis(X_train, y_train, X_test, y_test, hidden_size=5000)
    #         stop = time.time()
    #         elm_time = stop - start

    #         print(f'Predicted values using ELM')
    #         print(y_elm_pred)
    #         ea.disp_matrics(elm_r2, elm_rmse, elm_mae, start, stop, 'The ELM model performance for testing set')

    # print('\n')

    # ea.disp_graphs(i, y_test, y_ann_pred, y_elm_pred)
    # ea.disp_compare_graphs(ann_r2, ann_rmse, ann_mae, ann_time, elm_r2, elm_rmse, elm_mae, elm_time)
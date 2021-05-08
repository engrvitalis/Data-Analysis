import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

def get_prob(factors):
    data = []
    data1 = []
    data2 = []

    for factor, sub_factors in factors.items():
        print('------------------------------')
        print(f'{factor}: 1/{len(factors)}')
        print('------------------------------')

        # Create building collapse rating dataframe
        data.append([factor, sub_factors[1]])
        df = pd.DataFrame(data, columns=['Causes', 'Rating']).set_index('Causes')

        if sub_factors[1] == 1:
            data1.append([factor, 1, 0, 0])
        elif sub_factors[1] == 2:
            data1.append([factor, 0, 1, 0])
        else:
            data1.append([factor, 0, 0, 1])
        df1 = pd.DataFrame(data1, columns=['Causes', 'Low', 'Moderate', 'High']).set_index('Causes')

        length = len(sub_factors[0])
        num = 0
        while True:
            step = 0.001
            z = num**2 * length
            if sub_factors[1]-0.1 < z <= sub_factors[1]:
                break
            num += step
        
        if sub_factors[1] == 1:
            data2.append([factor, 'Low'])
        elif sub_factors[1] == 2:
            data2.append([factor, 'Moderate'])
        else:
            data2.append([factor, 'High'])

        df2 = pd.DataFrame(data2, columns=['Causes', 'Rating']).set_index('Causes')

        # Map rating to description.
        if z <= 1:
            rating = 'Low'
        elif z <= 2:
            rating = 'Moderate'
        else:
            rating = 'High'

        # Print sub factor's metrics
        for sub_factor in sub_factors[0]:
            print(f'{sub_factor} value: {round(num, 2)/10*100}%')
        print(f'Rating: {rating}')
        print('\n')
    
    # Display causes and their rating.
    print('Building collapse causes and their ratings: 1=Low, 2=Moderate and 3=High')
    display(df)
    print('\n')
    display(df1)
    print('\n')
    display(df2)

    plt.figure(figsize=(10,5))
    cbar_kws = {'ticks':[1, 2, 3]}
    sns.heatmap(df, cmap='coolwarm', annot=True, linewidths=4, cbar_kws=cbar_kws).set(title='Building Collapse and their Ratings')
    plt.tight_layout
    plt.show()
    
    plt.figure(figsize=(10,5))
    cbar_kws = {'ticks':[0, 1]}
    sns.heatmap(df1, cmap='coolwarm', annot=False, linewidths=4, cbar = True, cbar_kws=cbar_kws).set(title='Building Collapse Sensitivity Matrix')
    plt.tight_layout
    plt.show()


factors = {'Design': (['Load factor', 'Calculator error', 'Wrong use of code'], 1),
'Construction': (['Salty sand', 'Sub-standard Reinforcement', 'Alternative structures','Decayed formwork'], 2),
'Foundation': (['Lack of soil test', 'Inappropriate foundation type', 'Design error'], 3),
'Detailing and Specification': (['Faulty dimensioning', 'Inconsistent bar marks'], 1),
'Quality Control': (['Poor quality material', 'Wrong manufacturing of construction material', 'Poor installation'], 2),
'Engagement of Quacks': (['Quacks', 'Semi skilled workers', 'Skilled workers'], 3),
'Development Control': (['Approval', 'Supervision', 'Certification at each stage'], 2),
'Extra Ordinary Load': (['Working load', 'Natural disaster'], 3),
'Procedural': (['Procedural'], 1)}

get_prob(factors)
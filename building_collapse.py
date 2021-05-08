import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def get_prob(factors):
    data = []
    for factor, sub_factors in factors.items():
        print('------------------------------')
        print(f'{factor}: 1/{len(factors)}')
        print('------------------------------')

        # Create building collapse rating dataframe
        data.append([factor, sub_factors[1]])
        df = pd.DataFrame(data, columns = ['Causes', 'Rating'])

        length = len(sub_factors[0])
        num = 0
        while True:
            step = 0.001
            z = num**2 * length
            if sub_factors[1]-0.1 < z <= sub_factors[1]:
                break
            num += step
        
        # Map rating to description.
        if z <= 1:
            rating = 'Low'
        elif z <= 2:
            rating = 'Moderate'
        else:
            rating = 'High'

        # Print sub factor's metrics
        for sub_factor in sub_factors[0]:
            print(f'{sub_factor} value: {num}')
        print(f'Rating: {rating}')
        print('\n')
    
    # Display causes and their rating.
    print('Building collapse causes and their ratings: 1=Low, 2=Moderate and 3=High')
    print(df)





factors = {'design': (['Load factor', 'Calculator error', 'Wrong use of code'], 1),
'construction': (['Salty sand', 'Sub-standard Reinforcement', 'Alternative structures','Decayed formwork'], 2),
'foundation': (['Lack of soil test', 'Inappropriate foundation type', 'Design error'], 3),
'detailing_and_specification': (['Faulty dimensioning', 'Inconsistent bar marks'], 1),
'quality_control': (['Poor quality material', 'Wrong manufacturing of construction material', 'Poor installation'], 2),
'engagement_of_quacks': (['Quacks', 'Semi skilled workers', 'Skilled workers'], 3),
'development_control': (['Approval', 'Supervision', 'Certification at each stage'], 2),
'Extra ordinary load cause': (['Working load', 'Natural disaster'], 3),
'procedural': (['Procedural'], 1)}


  
# Create the pandas DataFrame
# df = pd.DataFrame(data, columns = ['Name', 'Age'])

get_prob(factors)
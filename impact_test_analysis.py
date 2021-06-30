"""Import the required modules"""


import elm_ann as ea

# Read in files for analysis.
file = ('impact1.csv', 'impact2.csv')
df = ea.get_file(file)

# Explore the each file variables.
for i in range(0, len(file)):
    print('\nData Statistical Summary')
    print(df[i].describe())
    print('')

    print('\nData Visualization')
    ea.explore(df[i])
import pandas as pd

d = pd.read_csv('Inshorts.csv')
print('Original Length', len(d))
d.drop(d[d['Headline'] == 'Headline'].index, inplace=True)
d.drop_duplicates(inplace=True)
d.reset_index(drop=True, inplace=True)
print('Modified Length', len(d))
d.to_csv('Inshorts.csv', index=False)
print('Python script executed')
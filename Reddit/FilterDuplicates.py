import pandas as pd
import os

subreddits = os.listdir()
subreddits = list(filter(lambda x: x.endswith('.csv'), subreddits))

for i, sub in enumerate(subreddits):
    print(i+1, sub)
    d = pd.read_csv(sub)
    print('Original Length', len(d))
    d.drop(d[d['title'] == 'title'].index, inplace=True)
    d.drop_duplicates(subset=['title'], inplace=True)
    d.reset_index(drop=True, inplace=True)
    print('Modified Length', len(d))
    d.to_csv(sub, index=False)
    print('\n')


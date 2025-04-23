import pandas as pd
import os
from glob import glob

def summary(dir):
    csvPaths = glob(os.path.join(dir, '*.csv'))
    relevantCSV = [i for i in csvPaths if all(x not in i.lower() for x in ['practice', 'soundcheck', 'test'])]

    dfs = []
    for i in relevantCSV:
        dfs.append(pd.read_csv(i))

    participantDF = pd.concat(dfs, ignore_index=True)[['Order', 'Type', 'key_press.corr', 'key_press.rt']]

    df = participantDF.dropna()

    df = df[df['Type'] != 'fixation']

    summary = df.groupby(['Order', 'Type']).agg({
        'key_press.corr':'mean',
        'key_press.rt':'mean'
    }).reset_index()

    summary['Order'] = summary['Order'].replace({
        'First_Order':'FO',
        'Second_Order':'SO'
    })

    summary['Condition'] = summary['Order'] + '_' + summary['Type']
    summary = summary.set_index('Condition')
    summary = summary.drop(columns=['Order', 'Type'])

    summary = summary.rename(columns={
        'key_press.corr':'accuracy',
        'key_press.rt':'RT'
    })

    return summary
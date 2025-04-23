import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

import subprocess
import sys
import os
sys.path.append(os.path.abspath('..'))

from src.GetSummary import summary

participants = []
baseDir = '../data/participantdata'

for folder in os.listdir(baseDir):
    path = os.path.join(baseDir, folder)
    if os.path.isdir(path):
        try:
            summ = summary(path).reset_index()
            summ['participant'] = folder
            summ = summ.set_index('participant')
            participants.append(summ)
        except Exception as e:
            print(f"Skipping {folder}: {e}")

summDF = pd.concat(participants)

pivot = summDF.pivot_table(
    index='participant',
    columns=['Condition'],
    values=['accuracy', 'RT']
)

pivot.columns = [f'{condition}_{stat}' for stat, condition in pivot.columns]
df = pivot

accCols = [i for i in df.columns if i.endswith('_accuracy')]
df = df[df[accCols].min(axis=1) >= 0.5]

df.to_csv('../data/preprocessed_vectors.csv', index=False)

subprocess.run(['Rscript', '../src/NBClustEval.R'], check=True)

with open('../data/optimal_k.txt', 'r') as f:
    optimalK = int(f.read())

scaled = StandardScaler().fit_transform(df)

kmeans = KMeans(n_clusters=optimalK, n_init='auto')
labels = kmeans.fit_predict(scaled)

clusteredDf = df.copy()

clusteredDf['cluster'] = labels

clusteredDf.to_csv('../data/clustered_data.csv')
import pandas as pd
import numpy as np

data = pd.read_csv('./data/Nowcoder_pandas_noindex.csv')
# print(data.head())

"""data.iloc[1, -1] = None
data.iloc[2, 5] = None
print(data.dropna(axis=0, how='any'))

print(data)
data['Language'].fillna('Python',inplace=True)
print(data.Language)"""

"""print(data.query('index == 2'))
data_p = pd.concat([data, data.query('index == 2')], axis=0)
print(data_p)

data_p.index = list(range(len(data_p)))
print(data_p)

print(data_p.duplicated())
print(data_p.drop_duplicates())"""

print(data)
print(data.dtypes)
print(data.info())

data[['Nowcoder_ID', 'Level']] = data[['Nowcoder_ID', 'Level']].astype('int')
print(data.info())

data['Last_submission_time'] = pd.to_datetime(data['Last_submission_time'], format='%Y-%m-%d')
print(data[['Nowcoder_ID', 'Level', 'Last_submission_time']])

data.to_json('./data/Nowcoder.json')
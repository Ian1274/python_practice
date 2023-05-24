import pandas as pd

"""df = pd.read_csv('./data/Nowcoder1.csv')
df['year-month-day'] = pd.to_datetime(df['date']).dt.date
print(df)
"""
"""
print(df.groupby(['result', 'year-month-day'])['question_id'].count())
"""

"""print(list(df.groupby(['result', 'year-month-day'])))"""

"""a = df.groupby(["result","year-month-day"])
print(a["year-month-day"].size())"""

"""a = df.groupby('result')
print(a.size())"""

df = pd.read_csv('./data/Nowcoder_pandas_noindex.csv')
"""print(df)
print(df.columns)"""

"""gy = list(df['Graduate_year'].unique())
for i in gy:
    df_gy = df[df['Graduate_year'] == i]
    print(i, 'year  ', df_gy['Achievement_value'].max())"""

print(df.groupby(['Graduate_year']).Achievement_value.max())
print(df.groupby(['Language', 'Level']).Language.count())
print(df.groupby(['Level', 'Language']).Language.count())
print(df.groupby('Level').Level.count())
print(df.groupby(['Level'])['Nowcoder_ID'].count()>5)
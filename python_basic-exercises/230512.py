import pandas as pd

"""df =pd.read_csv("./data/Nowcoder_pandas.csv")
print(df)
df.pop('Unnamed: 0')

df['Continuous_check_in_days'] = [120, 1, 2, 1, 45]
df['Number_of_submissions'] = [1230, 10, 45, 564, 1349]
df['Last_submission_time'] = ['2022/5/6', '2021/5/7', '2022/4/8', '2022/6/9', '2020/7/10']

print(df)

df.to_csv("./data/Nowcoder_pandas.csv")"""

"""df =pd.read_csv("./data/Nowcoder_pandas.csv")
# print(df)
df1 = df.drop([5], axis=0)
# print(df1)
df2 = df1.drop(df1.columns[0], axis=1)
# print(df2)

df2.to_csv("./data/Nowcoder_pandas_noheader.csv", header=False)
df2.to_csv("./data/Nowcoder_pandas_noindex.csv", index=False)
df2.to_csv("./data/Nowcoder_pandas_noall.csv", index=False, header=False)

df11 = pd.read_csv("data/Nowcoder_pandas_noheader.csv")
df22 = pd.read_csv("data/Nowcoder_pandas_noindex.csv")
df33 = pd.read_csv("data/Nowcoder_pandas_noall.csv")
print(df11)
print(df22)
print(df33)
"""

df = pd.read_csv("data/Nowcoder_pandas_noindex.csv")

"""print(df.Continuous_check_in_days)
print(df.Continuous_check_in_days.max())
print(df.Continuous_check_in_days.min())"""

"""print(df["Language"])
print(df.query("Language == 'CPP'")["Number_of_submissions"].mean())
avg = df[df["Language"] == 'CPP']["Number_of_submissions"].mean()
print(avg)"""

"""print(df.query('Num_of_exercise >= 10')["Level"].median())"""

"""print(df["Language"].unique())
print(df["Language"].nunique())"""

"""print(
    df["Level"].mode()
)"""

"""print(
    df[['Achievement_value', 'Continuous_check_in_days']].quantile(q=0.25)
)"""


"""print(df.query('Level == 7')['Achievement_value'])
maxav = df.query('Level == 7')['Achievement_value'].max()
mixav = df.query('Level == 7')['Achievement_value'].min()
print(type(maxav))
print(int(maxav - mixav))"""

"""print(df["Num_of_exercise"].var())
print(df.loc[:,'Num_of_exercise'].var())
print(df.loc[:,'Num_of_exercise'].std())"""


"""print(
    df[df['Level']==7]['Achievement_value']/df['Achievement_value'].sum()
)"""

"""df_d10 = df.query('Num_of_exercise >= 10')
roght = df_d10['Num_of_exercise']/df_d10['Number_of_submissions']
print(f'最高的正确率:{roght.max():.3f}')"""


"""print(
    df['Last_submission_time'].str.len()
)"""
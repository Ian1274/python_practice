import pandas as pd

Nowcoder_ID = [178372, 989717, 783650, 723570, 456568]
Level = [7, 1, 2, 6, 7]
Achievement_value = [8711, 12,120, 5666, 11234]
Num_of_exercise = [500, 3, 32, 433, 899]
Graduate_year = [2017, 2016, 2010, 2019, 2017]
Language = ['CPP', 'Java', 'CPP', 'C', 'Python']

newcode = pd.DataFrame({'Nowcoder_ID':Nowcoder_ID,
                        'Level':Level,
                        'Achievement_value':Achievement_value,
                        'Num_of_exercise':Num_of_exercise,
                        'Graduate_year':Graduate_year,
                        'Language':Language})
newcode.to_csv("./data/Nowcoder_pandas.csv")
data = pd.read_csv('./data/Nowcoder_pandas.csv')
# print(data.head())
data.pop('Unnamed: 0')
# print(data.head())
# print(data.shape)
# print(data.loc[3])
# print(data.loc[1:3, 'Language'])
"""data.loc['Language',0]=None
print(data.head())
print(data.isna().any())"""


"""print(data.loc[data['Language']=='Python'])
print(data)
data.iloc[0, 5]=None
print(data)"""


"""print(data[data['Language']=='Python'])
print(data[data['Language']=='Python']['Achievement_value'])
print(data[data['Language']=='Python'].loc[:, 'Achievement_value'])
print(data['Achievement_value'][data['Language']=='Python'])"""
"""
输出行：
df.loc[2:6]   第2到6行
输出列：
df['列名']  输出列名为引号内的某列，默认第一行索引"""


"""print(data.iloc[-4:-1,[0,1,2,5]])
print(data[['Nowcoder_ID', 'Level', 'Achievement_value', 'Language']].loc[2:4])  # 这里列索引记得是一个列表
print(data.loc[2:4][['Nowcoder_ID', 'Level', 'Achievement_value', 'Language']])"""


"""pd.set_option("display.width", 300)  # 设置字符显示宽度
pd.set_option("display.max_rows", None)  # 设置显示最大行
pd.set_option("display.max_columns", None)
print(data.loc[(data["Graduate_year"] == 2016) & (data["Language"] == "Java")])
print(data[(data["Graduate_year"] == 2016) & (data["Language"] == "Java")])
print(data.query('Graduate_year == 2016 & Language == "Java"'))"""


"""print(data.query('Language == "Java" or Language == "Python"'))
print(data.query('Language in ("Java", "Python")'))
print(data[data['Language'].isin(["Java", "Python"])])"""
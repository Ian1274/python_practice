import pandas as pd

data = {'user_id': [1, 2, 3, 4, 5, 6, 7],
        'question_id': [101, 102, 103, 104, 105, 107, 106],
        'result': ['wrong', 'right', 'wrong', 'wrong', 'wrong', 'wrong', 'right'],
        'date': ['2022-12-11', '2022-12-11', '2022-12-12', '2022-12-13', '2022-12-14', '2022-12-15', '2022-12-16']
        }

df = pd.DataFrame(data)

# print(df.groupby('date')['question_id'].count())

data_p = {'user_id': [1, 2, 8, 4, 5, 6, 9],
        'question_id': [101, 103, 109, 104, 108, 107, 106],
        'result': ['wrong', 'right', 'wrong', 'wrong', 'wrong', 'wrong', 'right'],
        'date': ['2022-12-12', '2022-12-13', '2022-12-12', '2022-12-13', '2022-12-14', '2022-12-15', '2022-12-16']
        }

df_p = pd.DataFrame(data_p)
# print(df_p)

df2 = pd.concat([df, df_p], axis=0)
print(df2)

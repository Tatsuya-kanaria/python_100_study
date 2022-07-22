# %%
import pandas as pd
import re


# 不要部分を削る　
data = pd.read_excel('./data/1-2-2020.xlsx', skiprows=4, header=None)

data.head()

data.drop(data.tail(4).index, inplace=True)

col_data = pd.read_excel('data/1-2-2020.xlsx', skiprows=1, header=None)
col_data = col_data.head(3)

# 下のNanを埋める
col_data.iloc[1, 1:].fillna(col_data.iloc[0, 1:], inplace=True)
col_data.iloc[1, 1:] = col_data.iloc[1, 1:].str.replace('発電所', '')

# 右隣のNanを埋める
for i in col_data.columns:
    if i < col_data.columns.max():
        col_data[i + 1].fillna(col_data[i], inplace=True)

# 正規表現
col_data.replace('^\〔(.+?)\〕$', r'\1', regex=True, inplace=True)

# col_data.replace({'〔バイオマス〕': 'バイオマス', '〔廃棄物〕': '廃棄物'}, inplace=True)
col_data

# tg_col = '_'.join(list(col_data[0].dropna()))
# tg_col = '_'.join(list(col_data[1].dropna()))

cols = []
for i in col_data.columns:
    tg_col = '_'.join(list(col_data[i].dropna()))
    cols.append(tg_col)
cols

data.columns = cols
data.head()
# %%

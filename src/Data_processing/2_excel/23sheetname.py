# %%
import pandas as pd
import re


# 不要部分を削る　
data = pd.read_excel('./data/1-2-2020.xlsx', skiprows=4, header=None)

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

# 正規表現　〔〕取り除く
col_data.replace('^\〔(.+?)\〕$', r'\1', regex=True, inplace=True)

cols = []
for i in col_data.columns:
    tg_col = '_'.join(list(col_data[i].dropna()))
    cols.append(tg_col)

data.columns = cols

# ExcelFile を使うと全ての情報が取得できる
# シート名取得
xl = pd.ExcelFile('./data/1-2-2020.xlsx')
sheets = xl.sheet_names

# シート毎にリスト化する
datas = []
for sheet in sheets:
    data = xl.parse(sheets[0], skiprows=4, header=None)
    data.drop(data.tail(4).index, inplace=True)
    data.columns = cols
    data['年月'] = sheet
    datas.append(data)

# 全データ結合　ignore_index: 縦に結合した際のindexを振り直す
datas = pd.concat(datas, ignore_index=True)

datas.head()
# %%

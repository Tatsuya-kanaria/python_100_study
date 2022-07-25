# %%
from cv2 import dft
import pandas as pd
import re

# 読み込んで確認する
capacity_data = pd.read_excel('./data/2-2-2020.xlsx')
# display(capacity_data.head())
# display(capacity_data.tail())

# 先頭行をなくす
col_ca_data = pd.read_excel('./data/2-2-2020.xlsx', skiprows=1, header=None)
col_ca_data = col_ca_data.head(3)
# 1行目がNaなら0行目をコピーする
col_ca_data.iloc[1, 1:].fillna(col_ca_data.iloc[0, 1:], inplace=True)
# 発電機を取り除く
col_ca_data.iloc[1, 1:] = col_ca_data.iloc[1, 1:].str.replace('発電所', '')

# 右隣のNaをコピーする
for i in col_ca_data.columns:
    if i < col_ca_data.columns.max():
        col_ca_data[i + 1].fillna(col_ca_data[i], inplace=True)

# 正規表現 〔〕取り除く
col_ca_data.replace('^\〔(.+?)\〕$', r'\1', regex=True, inplace=True)

# 先頭カラム配列
cols_ca = []
for i in col_ca_data.columns:
    tg_col = '_'.join(list(col_ca_data[i].dropna()))
    cols_ca.append(tg_col)
# print("cols_ca: ", cols_ca)

# .ExcelFile: エルセルの全てのデータ取得可能
xl_ca = pd.ExcelFile('./data/2-2-2020.xlsx')
# シートネーム取得
sheets = xl_ca.sheet_names
ca_datas = []
# 各シートの整形、年月追加
for sheet in sheets:
    capacity_data = xl_ca.parse(sheet, skiprows=4, header=None)
    capacity_data = capacity_data.head(47)
    capacity_data.columns = cols_ca
    capacity_data['年月'] = sheet
    ca_datas.append(capacity_data)

ca_datas = pd.concat(ca_datas, ignore_index=True)


def pat_matcher(list_, pattern):
    '''Returns a list of patterns that the string contains from the list'''

    pattern = "^.*" + pattern + ".*$"
    list_val = [val for val in list_ if re.match(pattern, val)]
    return None if list_val == [] else list_val


fire_list = pat_matcher(cols_ca,
                        "_火力_")
bio_list = pat_matcher(cols_ca,
                       "_バイオマス_")
waste_list = pat_matcher(cols_ca,
                         "_廃棄物_")

# 重複項目を引く
for fire, bio, waste in zip(fire_list, bio_list, waste_list):
    ca_datas[fire] = ca_datas[fire] - ca_datas[bio] - ca_datas[waste]

drop_list = pat_matcher(cols_ca, "_計_")
drop_list.extend(pat_matcher(cols_ca, "_合計_"))
# 不要な項目列を消す
ca_datas.drop(drop_list, axis=1, inplace=True)

# 縦持ちデータ
ca_datas_v = pd.melt(ca_datas, id_vars=[
                     '都道府県', '年月'], var_name="変数名", value_name="値")
var_data = ca_datas_v['変数名'].str.split('_', expand=True)
var_data.columns = ['発電所種別', '発電種別', '項目']
ca_datas_v = pd.concat([ca_datas_v, var_data], axis=1)
ca_datas_v.drop(['変数名'], axis=1, inplace=True)
ca_datas_v.head()
# %%

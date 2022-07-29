# %%
from cv2 import dft
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

# 全データ結合 ignore_index: 縦に結合した際のindexを振り直す
datas = pd.concat(datas, ignore_index=True)


def pat_matcher(list_, pattern):
    '''Returns a list of patterns that the string contains from the list'''

    pattern = "^.*" + pattern + ".*$"
    list_val = [val for val in list_ if re.match(pattern, val)]
    return None if list_val == [] else list_val


fire_list = pat_matcher(cols,
                        "_火力_")
bio_list = pat_matcher(cols,
                       "_バイオマス_")
waste_list = pat_matcher(cols,
                         "_廃棄物_")

# print(list(zip(fire_list, bio_list, waste_list)))
# [('火力発電所_火力_発電所数', '新エネルギー等発電所_バイオマス_発電所数', '新エネルギー等発電所_廃棄物_発電所数'),
#  ('火力発電所_火力_最大出力計', '新エネルギー等発電所_バイオマス_最大出力計', '新エネルギー等発電所_廃棄物_最大出力計')]

# 火力にバイオマスと廃棄物が含まれているために差し引く(発電所数、最大出力計)
for fire, bio, waste in zip(fire_list, bio_list, waste_list):
    datas[fire] = datas[fire] - datas[bio] - datas[waste]

drop_list = pat_matcher(cols, "合計")
drop_list.extend(pat_matcher(cols, "_計_"))
drop_list
# 必要なカラムだけに絞り込む
# axis=1:列削除 0:行
datas.drop(drop_list, axis=1, inplace=True)

# 縦持ちデータ
datas_v = pd.melt(datas,
                  id_vars=["都道府県", "年月"],
                  var_name="変数名", value_name="値")

datas_v.head()
# %%

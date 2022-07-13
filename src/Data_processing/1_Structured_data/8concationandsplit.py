# %%
from glob import glob
import pandas as pd
import os
import re


# データ読み込み
data = pd.read_csv('./data/22_shizuoka_all_20210331.csv',
                   encoding='shift-jis', header=None, dtype=object)

# 差分データ読み込み
diff_files = glob('data/diff*.csv')
diff_files
# ソート
diff_files.sort()
diff = pd.read_csv(
    diff_files[0], encoding='shift-jis', header=None, dtype=object)

# ヘッドテキストの読み込み
mst = pd.read_csv('./data/mst_column_name.txt', encoding='shift-jis', sep='\t')
columns = mst.column_name_en.values

# ヘッダ行を設定
data.columns = columns
diff.columns = columns
# 絞り込み
diff = diff.loc[diff['prefectureName'] == '静岡県']

'データ追加'
for f in diff_files:
    diff = pd.read_csv(f, encoding='shift-jis', header=None, dtype=object)
    diff.columns = columns
    diff = diff.loc[diff['prefectureName'] == '静岡県']
    data = pd.concat([data, diff])

'重複データの削除'
data.drop_duplicates(subset='corporateNumber', keep='last', inplace=True)

# print(data.describe())

'列の追加'
'''法人種別, 検索対象区分, 処理区分, 最新履歴区分, 閉鎖事由区分, 訂正区分'''
# print(os.listdir('data'))

mst_list = glob('data/mst*.csv')
pattern = '(data/mst)|(corp)|(kbn)|(_+)|(\.+\w*)'

for mst in mst_list:
    on_mst = re.sub(pattern, '', mst)
    if on_mst == 'correct':
        mst = pd.read_csv(mst, encoding='shift-jis', dtype=object)
    else:
        mst = pd.read_csv(mst, dtype=object)

    data = data.merge(mst, on=on_mst, how='left')

'連結の前に欠損がないか確認する'
data[['prefectureName', 'cityName', 'streetNumber']].isna().sum()

'アドレスに連結した住所追加'
data['address'] = data['prefectureName'] + \
    data['cityName'] + data['streetNumber']
print(len(data.columns))

''
data.loc[data['streetNumber'].isna()].head(3)

'番地が欠損している場合の処理'
data['address'].loc[data['streetNumber'].isna()] = data['prefectureName'] + \
    data['cityName']


print('欠損データ:', data['address'].isna().sum())
data.loc[data['streetNumber'].isna()].head(3)
data.head(3)

'郵便番号を分割して追加'
data['postCode_head'] = data['postCode'].str[:3]
data['postCode_tail'] = data['postCode'].str[-4:]
print(len(data.columns))
data.head(3)


# %%

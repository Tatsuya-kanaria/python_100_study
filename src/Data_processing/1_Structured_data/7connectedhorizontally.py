# %%
from glob import glob
import pandas as pd
import os


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

print(os.listdir('data'))

'追加項目'
mst_process_kbn = pd.read_csv(
    './data/mst_process_kbn.csv', dtype=object)

data = data.merge(mst_process_kbn, on='process', how='left')

print(len(data.columns))

'訂正区分'
mst_correct_kbn = pd.read_csv(
    './data/mst_correct_kbn.csv', encoding='shift-jis', dtype=object)

data = data.merge(mst_correct_kbn, on='correct', how='left')
print(len(data.columns))

'法人種別'
mst_corp_kind = pd.read_csv('./data/mst_corp_kind.csv', dtype=object)

data = data.merge(mst_corp_kind, on='kind', how='left')
print(len(data.columns))

'閉鎖事由区分'
mst_close_cause = pd.read_csv('./data/mst_closeCause.csv', dtype=object)

data = data.merge(mst_close_cause, on='closeCause', how='left')
print(len(data.columns))

'最新履歴区分'
mst_latest = pd.read_csv('./data/mst_latest.csv', dtype=object)
data = data.merge(mst_latest, on='latest', how='left')
print(len(data.columns))

'検索対象除外区分'
mst_hihyoji = pd.read_csv('./data/mst_hihyoji.csv', dtype=object)
data = data.merge(mst_hihyoji, on='hihyoji', how='left')
print(len(data.columns))

data.head(3)
# %%

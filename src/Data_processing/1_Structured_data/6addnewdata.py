# %%
from glob import glob
import pandas as pd
import os

os.listdir('data')

# データ読み込み
data = pd.read_csv('./data/22_shizuoka_all_20210331.csv', encoding='shift-jis')

# 差分データ読み込み
diff_files = glob('data/diff*.csv')
diff_files
#　ソート
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

print('len(diff): {}'.format(len(diff)))
# diff.head(3)

data_test = data
print('data_test:', len(data_test))

print(len(data_test) == len(data))
print(len(diff))
# data_test = data_test.append(diff)
# append使用不可になるためこちらを使う
data_test = pd.concat([data, diff])
print(len(data_test))
data_test.tail(3)
# %%

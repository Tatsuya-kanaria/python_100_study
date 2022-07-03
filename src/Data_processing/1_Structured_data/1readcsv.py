"""csvの読み込み"""
import pandas as pd


data = pd.read_csv('./data/22_shizuoka_all_20210331.csv',
                   encoding='shift-jis', header=None)

print(data.head(5))
print('len: {}'.format(len(data)))

print('columns: {} len: {}'.format(data.columns, len(data.columns)))

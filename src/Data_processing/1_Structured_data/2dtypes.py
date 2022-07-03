"""csvの読み込み"""
import pandas as pd


data = pd.read_csv('./data/22_shizuoka_all_20210331.csv',
                   encoding='shift-jis', header=None, dtype=object)

print(data.head())
print(data.dtypes)

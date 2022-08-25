# %%
import pandas as pd
import csv


# 大容量データの場合。OOMエラーでプログラムが終了する。
# df = pd.read_csv('./data/person_count_out_0001_2021011509.csv')

# df

# 512行毎に読み込み
# for df in pd.read_csv('./data/person_count_out_0001_2021011509.csv', chunksize=512):
#     print(df.shape)

i = 0
for df in pd.read_csv('./data/person_count_out_0001_2021011509.csv', chunksize=64):
    df['processd_per_chunk'] = True
    df.to_csv('./data/processed_big_data.csv',
              mode='a', index=False, header=i == 0)
    i += 1

df = pd.read_csv('./data/processed_big_data.csv')

df

# %%

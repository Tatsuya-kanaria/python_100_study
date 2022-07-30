# %%
from glob import glob
import pandas as pd


files = glob('./data/person_count_1sec/out_0001/*.csv')
files.sort()
files[:5]

# parse_dates: datetime型で読み込む項目指定
data = []

for f in files:
    tmp = pd.read_csv(f, parse_dates=["receive_time"])
    data.append(tmp)
data = pd.concat(data, ignore_index=True)

display(data.head())
len(data)


# %%

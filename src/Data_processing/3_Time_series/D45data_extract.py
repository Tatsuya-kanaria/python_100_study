# %%
from glob import glob
import pandas as pd
import datetime as dt


files = glob('./data/person_count_1sec/out_0001/*.csv')
files.sort()
# print(files[:5])

data = []

# parse_dates: datetime型で読み込む項目指定
for f in files:
    tmp = pd.read_csv(f, parse_dates=["receive_time"])
    data.append(tmp)
data = pd.concat(data, ignore_index=True)


# dt.date 年月日
data['receive_date'] = data['receive_time'].dt.date

daily_count = data[['receive_date', 'id']].groupby(
    'receive_date', as_index=False).count()

# dt.dayofweek 曜日
data['dayofweek'] = data['receive_time'].dt.dayofweek

# dt.day_name() 曜日名
data['day_name'] = data['receive_time'].dt.day_name()
data.head()

# .drop_duplicates: 重複を削除
data[['receive_date',
      'dayofweek',
      'day_name']].drop_duplicates(subset='receive_date').head(10)

data_extract = data.loc[(data['receive_time'] >= dt.datetime(2021, 1, 20)) & (
    data['receive_time'] < dt.datetime(2021, 1, 23))].copy()

display(data_extract.head())
display(data_extract.tail())

# %%

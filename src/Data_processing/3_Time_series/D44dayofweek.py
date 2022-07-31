# %%
from glob import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


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

data[['receive_date', 'dayofweek', 'day_name']
     ].drop_duplicates(subset='receive_date').head(10)

# %%

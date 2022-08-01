# %%
from glob import glob
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns


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
# data[['receive_date',
#       'dayofweek',
#       'day_name']].drop_duplicates(subset='receive_date').head(10)

data_extract = data.loc[(data['receive_time'] >= dt.datetime(2021, 1, 20)) & (
    data['receive_time'] < dt.datetime(2021, 1, 23))].copy()

# # 四捨五入
# data_extract['receive_time_sec'] = data_extract['receive_time'].dt.round('s')

# # 切り捨て
data_extract['receive_time_sec'] = data_extract['receive_time'].dt.floor('s')

# 重複データの確認
# data_extract[data_extract['receive_time_sec'].duplicated(keep=False)].head()

# 重複削除
data_extract = data_extract.drop_duplicates(subset=['receive_time_sec'])
min_receive_time = data_extract['receive_time_sec'].min()
max_receive_time = data_extract['receive_time_sec'].max()

# データフレーム作成
base_data = pd.DataFrame({'receive_time_sec': pd.date_range(
    min_receive_time, max_receive_time, freq='S')})

# データの結合
data_base_extract = pd.merge(
    base_data, data_extract, on='receive_time_sec', how='left')

# 欠損データの確認
# display(data_base_extract.isna().sum())
data_base_extract.sort_values('receive_time_sec', inplace=True)
# ffill: 前方のデータで埋める
# bfill: 後方のデータで埋める
data_base_extract = data_base_extract.fillna(method='ffill')
# 線形補完 interpolate()

data_analytics = data_base_extract[['receive_time_sec', 'in1', 'out1']].copy()

data_before_1sec = data_analytics.shift(1)
# data_before_1sec.head()

# カラム名を変更しないと同じになる
data_before_1sec.columns = [
    'receive_time_sec_b1sec', 'in1_b1sec', 'out1_b1sec']
data_analytics = pd.concat([data_analytics, data_before_1sec], axis=1)

# 秒あたりの人の出入り数
data_analytics['in1_calc'] = data_analytics['in1'] - \
    data_analytics['in1_b1sec']
data_analytics['out1_calc'] = data_analytics['out1'] - \
    data_analytics['out1_b1sec']

# 時間単位で集計するため
data_analytics['data_hour'] = data_analytics['receive_time_sec'].dt.strftime(
    '%Y%m%d%H')

viz_data = data_analytics[['data_hour', 'in1_calc', 'out1_calc']].groupby(
    'data_hour', as_index=False).sum()

viz_data_rolling = viz_data[['in1_calc', 'out1_calc']].rolling(3).mean()
viz_data_rolling.head(10)

viz_data_rolling['data_hour'] = viz_data['data_hour']
viz_data_rolling = pd.melt(viz_data_rolling, id_vars='data_hour', value_vars=[
                           'in1_calc', 'out1_calc'])

plt.figure(figsize=(15, 5))
plt.xticks(rotation='90')
sns.lineplot(x=viz_data_rolling['data_hour'],
             y=viz_data_rolling['value'], hue=viz_data_rolling['variable'])

# %%

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

# display(data.head())
# len(data)

# 経過日数の確認
# min_receive_time = data['receive_time'].min()
# max_receive_time = data['receive_time'].max()
# print("min:", min_receive_time)
# print("max:", max_receive_time)
# print("progress:", max_receive_time - min_receive_time)

# dt.year, dt.hour
data['receive_data'] = data['receive_time'].dt.date


daily_count = data[['receive_data', 'id']].groupby(
    'receive_data', as_index=False).count()
daily_count.head()

plt.figure(figsize=(15, 5))
plt.xticks(rotation=90)
sns.barplot(x=daily_count['receive_data'], y=daily_count["id"])

# %%

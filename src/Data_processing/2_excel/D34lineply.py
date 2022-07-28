# %%
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
import pandas as pd


import D29pivaot_table as D29

datas_v_all = D29.datas_v_all

plt.figure(figsize=(15, 5))
# データ整形
viz_data = datas_v_all[['発電種別', '年月', '値']].loc[(datas_v_all['項目'] == '電力量')]
viz_data = viz_data.groupby('年月', as_index=False).sum()
# データ型の変換
viz_data['年月'] = pd.to_datetime(viz_data['年月'])
# 棒グラフを描画
sns.lineplot(x=viz_data['年月'], y=viz_data['値'])

plt.figure(figsize=(15, 5))
# データ整形
viz_data = datas_v_all[['発電種別', '年月', '値']].loc[(datas_v_all['項目'] == '電力量')]
# データ型の変換
viz_data['年月'] = pd.to_datetime(viz_data['年月'])

sns.lineplot(x=viz_data['年月'], y=viz_data['値'], hue=viz_data['発電種別'])


# %%

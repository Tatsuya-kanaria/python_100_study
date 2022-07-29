# %%
from tokenize import group
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
import pandas as pd


import D29pivaot_table as D29

datas_v_all = D29.datas_v_all


# datetime型に変換
def pd_to_datetime(data, col_value):
    data[col_value] = pd.to_datetime(data[col_value]).dt.date


# カラム名変更
def rename_col(data, before, after):
    data = data.rename(columns={before: after}, inplace=True)


def data_loc(data, extract_list, loc_col_name, loc_value):
    data = data[extract_list].loc[(data[loc_col_name] == loc_value)]
    return data

# グループ化して足す


def data_groupby_sum(data, extract_list, group_list):
    data = data[extract_list].groupby(group_list, as_index=False).sum()
    return data


# データ整形
extract_list = ['都道府県', '年月', '値']

viz_data = data_loc(datas_v_all, extract_list, '項目', '電力量')

group_list = ['年月', '都道府県']

viz_data = data_groupby_sum(viz_data, extract_list, group_list)

pd_to_datetime(viz_data, '年月')

viz_data = viz_data.pivot_table(values='値', columns='年月', index='都道府県')

viz_data.head(5)

plt.figure(figsize=(10, 10))
sns.heatmap(viz_data)
# %%

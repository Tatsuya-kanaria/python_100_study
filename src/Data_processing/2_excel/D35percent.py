# %%
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
import pandas as pd


import D29pivaot_table as D29

datas_v_all = D29.datas_v_all

# データ整形
viz_data = datas_v_all.loc[(datas_v_all['項目'] == '電力量')
                           & (datas_v_all['年月'] == '2021.1')]
viz_data = viz_data[['発電種別', '値']].groupby('発電種別').sum()
viz_data['割合'] = viz_data['値'] / viz_data['値'].sum()
# T 転置（列、行）
viz_data.T.loc[['割合']].plot(kind='bar', stacked=True)

# %%

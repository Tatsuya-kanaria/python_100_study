# %%
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns


import D29pivaot_table as D29

datas_v_all = D29.datas_v_all

viz_data = datas_v_all[['発電種別', '年月', '値']].loc[(datas_v_all['項目'] == '電力量')]

viz_data = viz_data.groupby(['発電種別', '年月'], as_index=False).sum()
viz_data.head()


viz_data_date = (
    viz_data['年月'] == '2020.12') | (viz_data['年月'] == '2021.1')

viz_data = viz_data.loc[viz_data_date]

sns.barplot(x=viz_data['発電種別'], y=viz_data['値'], hue=viz_data['年月'])

# %%

# %%
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns


import D29pivaot_table as D29

viz_data = D29.datas_v_all[['発電種別', '値']].loc[(
    D29.datas_v_all['項目'] == '電力量') & (D29.datas_v_all['年月'] == '2021.1')]

viz_data = viz_data.groupby('発電種別', as_index=False).sum()
viz_data

sns.barplot(x=viz_data['発電種別'], y=viz_data['値'])
# %%

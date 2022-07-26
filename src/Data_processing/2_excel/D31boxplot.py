# %%
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns


import D29pivaot_table as D29

plt.figure(figsize=(10, 10))
viz_data = D29.datas_v_all.loc[(
    D29.datas_v_all['項目'] == '発電所数') & (D29.datas_v_all['値'] != 0)]
sns.boxplot(y=viz_data['値'])

plt.figure(figsize=(30, 10))
sns.boxplot(x=viz_data['発電種別'], y=viz_data['値'])

# %%

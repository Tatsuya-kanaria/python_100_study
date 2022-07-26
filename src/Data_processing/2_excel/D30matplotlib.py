# %%
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns


import D29pivaot_table as D29

plt.figure(figsize=(20, 10))
sns.histplot(D29.datas_v_all.loc[D29.datas_v_all['項目'] == '発電所数'])

fig, axes = plt.subplots(1, 3, figsize=(30, 10))
viz_data = D29.datas_v_all.loc[D29.datas_v_all['値'] != 0]

items = ['発電所数', '最大出力計', '電力量']
for cnt, item in enumerate(items, start=0):
    sns.histplot(viz_data.loc[viz_data['項目'] == item], ax=axes[cnt])


# %%

# %%
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
import pandas as pd


import D29pivaot_table as D29

datas_v_all = D29.datas_v_all


# datetime型に変換
def pd_to_datetime(data, col_value):
    data[col_value] = pd.to_datetime(data[col_value])


# カラム名変更
def rename_col(data, before, after):
    data = data.rename(columns={before: after}, inplace=True)


def data_loc(data, extract_list, loc_col_name, loc_value):
    data = data[extract_list].loc[(data[loc_col_name] == loc_value)]
    return data


# データ整形
viz_data = datas_v_all.loc[datas_v_all['項目'] == '電力量']
viz_data = viz_data[['都道府県', '値']].groupby('都道府県', as_index=False).sum()

viz_data.sort_values('値', inplace=True, ascending=False)
viz_data.head(5)

plt.figure(figsize=(15, 5))

extract_list = ['都道府県', '年月', '値']

viz_data = data_loc(datas_v_all,
                    extract_list,
                    '項目',
                    '電力量')

viz_data = viz_data.loc[((
    datas_v_all['都道府県'] == '神奈川県') | (datas_v_all['都道府県'] == '千葉県'))]

viz_data = viz_data.groupby(['年月', '都道府県'], as_index=False).sum()

pd_to_datetime(viz_data, '年月')

sns.lineplot(x=viz_data['年月'], y=viz_data['値'], hue=viz_data['都道府県'])

viz_data_num = data_loc(datas_v_all,
                        extract_list,
                        '項目',
                        '発電所数')

viz_data_num = viz_data_num.loc[((
    datas_v_all['都道府県'] == '神奈川県') | (datas_v_all['都道府県'] == '千葉県'))]

viz_data_num = viz_data_num.groupby(['年月', '都道府県'], as_index=False).sum()

pd_to_datetime(viz_data＿num, '年月')

rename_col(viz_data, '値', '電力量')
rename_col(viz_data_num, '値', '発電所数')

viz_data_join = pd.merge(viz_data, viz_data_num, on=['年月', '都道府県'], how='left')
viz_data_join.head()

sns.relplot(x=viz_data_join['年月'],
            y=viz_data_join['電力量'],
            hue=viz_data_join['発電所数'],
            size=viz_data_join['発電所数'],
            alpha=0.5, height=5, aspect=2)

# %%

# %%
from tokenize import group
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
import pandas as pd


import D29pivaot_table as D29

datas_v_all = D29.datas_v_all

writer = pd.ExcelWriter('./data/detail_data.xlsx', mode='w')

with writer as w:
    for target in datas_v_all['都道府県'].unique():
        tmp = datas_v_all.loc[datas_v_all['都道府県'] == target]
        tmp = tmp.pivot_table(values='値',
                              columns=['発電種別', '項目'],
                              index=['年月'], aggfunc='sum')
        tmp.to_excel(w, sheet_name=target)

# %%

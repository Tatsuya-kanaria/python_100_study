# %%
from tokenize import group
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
import pandas as pd


import D29pivaot_table as D29

datas_v_all = D29.datas_v_all

output = datas_v_all.pivot_table(values='値', columns='項目', index=[
                                 '年月', '都道府県'], aggfunc='sum')
output.head()

output.to_excel('./data/summary_data.xlsx')

# %%

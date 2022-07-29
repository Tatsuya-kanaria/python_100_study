# %%
from tokenize import group
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
import pandas as pd


import D25needcolumns as D25

datas = D25.datas

viz_data = datas.drop(['都道府県', '年月'], axis=1)
viz_data.head(5)

water_plant = D25.pat_matcher(D25.cols, '_水力_')

plant, output = water_plant

# 散布図
sns.scatterplot(x=viz_data[plant], y=viz_data[output],)

# ジョイントプロット
sns.jointplot(x=viz_data[plant], y=viz_data[output])

sns.pairplot(viz_data.iloc[:, 0:4])
# %%

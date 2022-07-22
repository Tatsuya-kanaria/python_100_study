# %%
import pandas as pd


# 不要部分を削る　
data = pd.read_excel('./data/1-2-2020.xlsx', skiprows=4, header=None)

data.head()

data.drop(data.tail(4).index, inplace=True)

data.tail()
# %%

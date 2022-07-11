# %%
import pandas as pd

data = pd.read_csv('./data/22_shizuoka_all_20210331.csv', encoding='shift-jis')

mst = pd.read_csv('./data/mst_column_name.txt', encoding='shift-jis', sep='\t')

columns = mst.column_name_en.values

data.columns = columns

data.describe()
# %%
data.isna().sum()

# %%

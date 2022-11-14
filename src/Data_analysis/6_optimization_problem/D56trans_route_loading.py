# %%
import pandas as pd


# データの読み込み
df_tr = pd.read_csv('./data/trans_route.csv', index_col="工場")
df_tr.head()

# %%

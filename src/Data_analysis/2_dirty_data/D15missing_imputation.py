# %%
import pandas as pd

import D11read_csv as D11
import D14shake_correction as D14

# 欠損値があるか確かめる
D11.uriage_data.isnull().any(axis=0)
'''
purchase_date    False
item_name        False
item_price        True
customer_name    False
dtype: bool
'''

# 欠損値を補う
flg_is_null = D11.uriage_data["item_price"].isnull()
for trg in list(D11.uriage_data.loc[flg_is_null, "item_name"].unique()):
    price = D11.uriage_data.loc[(~flg_is_null) & (
        D11.uriage_data["item_name"] == trg), "item_price"].max()
    D11.uriage_data["item_price"].loc[(flg_is_null) & (
        D11.uriage_data["item_name"] == trg)] = price

D11.uriage_data.head()
D11.uriage_data.isnull().any(axis=0)

# 確認`
for trg in list(D11.uriage_data["item_name"].sort_values().unique()):
    max_price = str(
        D11.uriage_data.loc[D11.uriage_data["item_name"] == trg]["item_price"].max())
    # skipna=False NaNデータが存在する場合　NaNに指定する。
    min_price = str(
        D11.uriage_data.loc[D11.uriage_data["item_name"] == trg]["item_price"].min(skipna=False))
    print("{} 最大値：{} 最小値：{}" .format(trg, max_price, min_price))

# %%

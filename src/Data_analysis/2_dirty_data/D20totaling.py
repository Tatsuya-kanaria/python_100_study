# %%
import pandas as pd

import D11read_csv as D11
import D18merge

import_data = pd.read_csv("./data/dump_data.csv")
import_data

# fill_value :欠損値補完
byItem = import_data.pivot_table(
    index="purchase_month", columns="item_name", aggfunc="size", fill_value=0)
byItem

byPrice = import_data.pivot_table(
    index="purchase_month", columns="item_name", values="item_price", aggfunc="sum", fill_value=0)
byPrice

byCustomer = import_data.pivot_table(
    index="purchase_month", columns="顧客名", aggfunc="size", fill_value=0)
byCustomer

byRegion = import_data.pivot_table(
    index="purchase_month", columns="地域", aggfunc="size", fill_value=0)
byRegion

# 集計期間に購入していない
away_data = pd.merge(D11.uriage_data, D11.kokyaku_data,
                     left_on="customer_name", right_on="顧客名", how="right")
away_data[away_data["purchase_date"].isnull()][["顧客名", "メールアドレス", "登録日"]]

# %%

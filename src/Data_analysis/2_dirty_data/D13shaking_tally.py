# %%
import pandas as pd

import D11read_csv as D11

# データの揺れがあるまま集計してみる
D11.uriage_data["purchase_date"] = pd.to_datetime(
    D11.uriage_data["purchase_date"])
D11.uriage_data["purchase_month"] = D11.uriage_data["purchase_date"].dt.strftime(
    "%Y%m")

# 26商品が99商品として扱われる
res = D11.uriage_data.pivot_table(
    index="purchase_month", columns="item_name", aggfunc="size", fill_value=0)

res = D11.uriage_data.pivot_table(
    index="purchase_month", columns="item_name", values="item_price", aggfunc="sum", fill_value=0)

res

# %%

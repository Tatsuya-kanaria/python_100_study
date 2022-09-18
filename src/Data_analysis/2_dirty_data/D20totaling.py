# %%
import pandas as pd


import_data = pd.read_csv("./data/dump_data.csv")
import_data

# fill_value :欠損値補完
byItem = import_data.pivot_table(
    index="purchase_month", columns="item_name", aggfunc="size", fill_value=0)
byItem

byPrice = import_data.pivot_table(
    index="purchase_month", columns="item_name", values="item_price", aggfunc="sum", fill_value=0)
byPrice



# %%

# %%
import pandas as pd

import D1pd_read_csv as D1


tbl_order_5 = pd.read_csv('./data/tbl_order_202005.csv')
tbl_order_5

order_all = pd.concat([D1.tbl_order_4, tbl_order_5], ignore_index=True)

order_all

len(order_all) == len(D1.tbl_order_4) + len(tbl_order_5)

# %%

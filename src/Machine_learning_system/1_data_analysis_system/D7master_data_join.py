# %%
import pandas as pd

import D1pd_read_csv as D1
import D6excluding_unnecessary_data as D6


order_data = pd.merge(D6.order_data, D1.m_store, on='store_id', how='left')

order_data = pd.merge(order_data, D1.m_area, on='area_cd', how='left')

order_data

# %%

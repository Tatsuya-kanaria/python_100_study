# %%
import pandas as pd
import D1read_csv as D1
import D3merge as D3


join_data = pd.merge(D3.join_data,
                     D1.customer_master,
                     on="customer_id", how="left")

join_data = pd.merge(join_data,
                     D1.item_master,
                     on="item_id", how="left")

join_data.head()

# %%

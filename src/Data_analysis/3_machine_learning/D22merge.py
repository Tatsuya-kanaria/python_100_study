# %%
import pandas as pd

import D21read as D21


customer_join = pd.merge(
    D21.customer, D21.class_master, on="class", how="left")
customer_join = pd.merge(
    customer_join, D21.campaign_master, on="campaign_id", how="left")

customer_join.head()

# 欠損値の確認
customer_join.isnull().sum()

# %%

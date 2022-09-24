# %%
import pandas as pd

import D22merge as D22
import D25uselog_aggregation as D25
import D26subscription_flag as D26

D22.customer_join["start_date"] = pd.to_datetime(
    D22.customer_join["start_date"])
D22.customer_join["end_date"] = pd.to_datetime(D22.customer_join["end_date"])

customer_join = pd.merge(
    D22.customer_join, D25.uselog_customer, on="customer_id", how="left")
customer_join = pd.merge(customer_join, D26.uselog_weekday[[
                         "customer_id", "routine_flg"]], on="customer_id", how="left")

customer_join.head()
customer_join.isnull().sum()

# %%

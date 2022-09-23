# %%
import pandas as pd

import D22merge as D22
import D23basic_aggregation


D22.customer_join["end_date"] = pd.to_datetime(D22.customer_join["end_date"])
# 最新月に退会した顧客と退会していない顧客
customer_newer = D22.customer_join.loc[(D22.customer_join["end_date"] >= pd.to_datetime(
    "20190331")) | (D22.customer_join["end_date"].isna())]

if __name__ == '__main__':
    print("customer_newer: ", len(customer_newer))

customer_newer["end_date"].unique()
columns_list = list(D22.customer_join.columns)

agg_list = ["class_name", "campaign_name", "gender", "is_deleted"]

for col_name in columns_list:
    if col_name not in agg_list:
        continue
    print(customer_newer.groupby(col_name).count()["customer_id"])


# %%

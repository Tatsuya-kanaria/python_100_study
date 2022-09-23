# %%
import pandas as pd

import D22merge as D22


columns_list = list(D22.customer_join.columns)

agg_list = ["class_name", "campaign_name", "gender", "is_deleted"]


D22.customer_join["start_date"] = pd.to_datetime(
    D22.customer_join["start_date"])
customer_start = D22.customer_join.loc[D22.customer_join["start_date"] > pd.to_datetime(
    "20180401")]

if __name__ == '__main__':
    for col_name in columns_list:
        if col_name not in agg_list:
            continue
        print(D22.customer_join.groupby(col_name).count()["customer_id"])

    print(len(customer_start))

# %%

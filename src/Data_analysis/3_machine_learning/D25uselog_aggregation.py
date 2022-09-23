# %%
import pandas as pd

import D21read as D21


D21.uselog["usedate"] = pd.to_datetime(D21.uselog["usedate"])
D21.uselog["年月"] = D21.uselog["usedate"].dt.strftime("%Y%m")
uselog_months = D21.uselog.groupby(
    ["年月", "customer_id"], as_index=False).count()
uselog_months.rename(columns={"log_id": "count"}, inplace=True)
del uselog_months["usedate"]
uselog_months.head()

# 平均値、中央値、最大値、最小値
uselog_customer = uselog_months.groupby("customer_id").agg(
    ["mean", "median", "max", "min"])["count"]

uselog_customer = uselog_customer.reset_index(drop=False)
uselog_customer.head()

# %%

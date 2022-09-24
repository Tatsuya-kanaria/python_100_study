# %%
import pandas as pd
from dateutil.relativedelta import relativedelta

import D27log_customer_merge as D27


D27.customer_join["calc_date"] = D27.customer_join["end_date"]
D27.customer_join["calc_date"] = D27.customer_join["calc_date"].fillna(
    pd.to_datetime("20190430"))
D27.customer_join["membership_period"] = 0

# 会員期間計算
for i in range(len(D27.customer_join)):
    delta = relativedelta(
        D27.customer_join["calc_date"].iloc[i], D27.customer_join["start_date"].iloc[i])
    D27.customer_join["membership_period"].iloc[i] = delta.years * \
        12 + delta.months

D27.customer_join.head()

# %%

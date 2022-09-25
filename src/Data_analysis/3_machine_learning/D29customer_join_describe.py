# %%
import D28membership_period
import D27log_customer_merge as D27

import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline


D27.customer_join[["mean", "median", "max", "min"]].describe()

D27.customer_join.groupby("routine_flg").count()["customer_id"]

plt.hist(D27.customer_join["membership_period"])


# %%

# %%
import D43continue_customer as D43
import D44predict_add_enrolled

import pandas as pd


D43.predict_data.isna().sum()

D43.predict_data = D43.predict_data.dropna(subset=["count_1"])

D43.predict_data.isna().sum()

# %%

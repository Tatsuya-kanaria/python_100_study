# %%
import pandas as pd

from D57load_all_data import store_all
from D58create_target_variable import y


y.rename(columns={'year_month': 'target_year_month'}, inplace=True)
y = y[[
    'store_name',
    'target_year_month',
    'one_month_ago',
    'y_weekday',
    'y_weekend'
]].copy()
ml_data = pd.merge(
    y, store_all,
    left_on=['store_name', 'one_month_ago'],
    right_on=['store_name', 'year_month'],
    how='left'
).copy()

ml_data.head()

del ml_data["target_year_month"]
del ml_data["one_month_ago"]
ml_data.head()

# %%

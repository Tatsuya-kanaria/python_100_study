# %%
from D72data_read import tg_ym
from D73aggregation_by_store import actual_data


target_cols = [
    'store_name',
    'order',
    'order_fin',
    'order_cancel',
    'order_delivery',
    'order_takeout',
    'order_weekday',
    'order_weekend',
    'delta_avg',
]

actual_data = actual_data[target_cols]
actual_cols = ['store_name']
rename_cols = [
    x + f'_{tg_ym}' for x in actual_data.columns if x != 'store_name']
actual_cols.extend(rename_cols)
actual_data.columns = actual_cols
actual_data.head(3)

# %%

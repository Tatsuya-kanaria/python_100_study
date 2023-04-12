# %%
import os
import pandas as pd

from D81folder_creation_and_initial_variables import store_monthly_dir, store_monthly_file
from D82store_data_from_update_data import store_data

store_monthly_data = pd.read_csv(
    os.path.join(store_monthly_dir, store_monthly_file))

print(f'更新前：{len(store_monthly_data)}件')

store_monthly_data = pd.concat(
    [store_monthly_data, store_data], ignore_index=True)

store_monthly_data['year_month'] = store_monthly_data['year_month'].astype(str)

store_monthly_data.drop_duplicates(
    subset=['store_name', 'year_month'], inplace=True, keep='last')

print(f'更新後：{len(store_monthly_data)}件')
store_monthly_data.to_csv(os.path.join(
    store_monthly_dir, store_monthly_file), index=False)

# %%

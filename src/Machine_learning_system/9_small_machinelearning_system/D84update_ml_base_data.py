# %%
from dateutil.relativedelta import relativedelta
import os
import pandas as pd

from D81folder_creation_and_initial_variables import ml_base_dir, ml_base_file
from D83update_store_monthly_data import store_monthly_data


y = store_monthly_data[[
    'store_name',
    'year_month',
    'order_weekday',
    'order_weekend'
]].copy()

y['one_month_ago'] = pd.to_datetime(y['year_month'], format='%Y%m')
y['one_month_ago'] = y['one_month_ago'].map(
    lambda x: x - relativedelta(months=1))
y['one_month_ago'] = y['one_month_ago'].dt.strftime('%Y%m')

y_one_month_ago = y.copy()
y_one_month_ago.rename(columns={
    'order_weekday': 'order_weekday_one_month_ago',
    'order_weekend': 'order_weekend_one_month_ago',
    'year_month': 'year_month_for_join'
}, inplace=True)

y = pd.merge(
    y,
    y_one_month_ago[[
        'store_name',
        'year_month_for_join',
        'order_weekday_one_month_ago',
        'order_weekend_one_month_ago',
    ]],
    left_on=['store_name', 'one_month_ago'],
    right_on=['store_name', 'year_month_for_join']
)

y.dropna(inplace=True)

# y.loc[y['order_weekday'] - y['order_weekday_one_month_ago'] > 0, 'y_weekday'] = 1
# y.loc[y['order_weekday'] - y['order_weekday_one_month_ago'] <= 0, 'y_weekday'] = 0
# y.loc[y['order_weekend'] - y['order_weekend_one_month_ago'] > 0, 'y_weekend'] = 1
# y.loc[y['order_weekend'] - y['order_weekend_one_month_ago'] <= 0, 'y_weekend'] = 0

# astype(int):True->1, False->0
y['y_weekday'] = (
    y['order_weekday'] -
    y['order_weekday_one_month_ago'] > 0
).astype(int)
y['y_weekend'] = (
    y['order_weekend'] -
    y['order_weekend_one_month_ago'] > 0
).astype(int)


y.rename(columns={
    'year_month': 'target_year_month',
}, inplace=True)
y = y[[
    'store_name',
    'target_year_month',
    'one_month_ago',
    'y_weekday',
    'y_weekend',
]].copy()

ml_data = pd.merge(
    y,
    store_monthly_data,
    left_on=['store_name', 'one_month_ago'],
    right_on=['store_name', 'year_month'],
    how='left')

del ml_data['target_year_month']
del ml_data['one_month_ago']
ml_data.head(3)

ml_base_data = pd.read_csv(os.path.join(ml_base_dir, ml_base_file))

print(f'更新前：{len(ml_base_data)}件')

ml_base_data = pd.concat([ml_base_data, ml_data], ignore_index=True)
ml_base_data['year_month'] = ml_base_data['year_month'].astype(str)
ml_base_data.drop_duplicates(
    subset=['store_name', 'year_month'], inplace=True, keep='last')

print(f'更新後：{len(ml_base_data)}件')

ml_base_data.to_csv(os.path.join(ml_base_dir, ml_base_file), index=False)

# %%

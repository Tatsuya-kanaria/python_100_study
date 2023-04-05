# %%
import pandas as pd
from dateutil.relativedelta import relativedelta

from D57load_all_data import store_all


y = store_all[[
    'store_name',
    'year_month',
    'order_weekday',
    'order_weekend'
]].copy()

y['one_month_ago'] = pd.to_datetime(y['year_month'], format='%Y%m')

y['one_month_ago'] = y['one_month_ago'].map(
    lambda x: x - relativedelta(months=1))

y['one_month_ago'] = y['one_month_ago'].dt.strftime('%Y%m')

y.head(3)

y_one_month_ago = y.copy()
y_one_month_ago.rename(columns={
    'order_weekday': 'order_weekday_one_month_ago',
    'order_weekend': 'order_weekend_one_month_ago',
    'year_month': 'year_month_for_join'
}, inplace=True)
y = pd.merge(y, y_one_month_ago
             [[
                 'store_name',
                 'year_month_for_join',
                 'order_weekday_one_month_ago',
                 'order_weekend_one_month_ago'
             ]],
             left_on=['store_name', 'one_month_ago'],
             right_on=['store_name', 'year_month_for_join'],
             how='left'
             )

y.loc[y['store_name'] == 'あきる野店']

y.dropna(inplace=True)
y.loc[y['order_weekday'] - y['order_weekday_one_month_ago'] > 0, 'y_weekday'] = 1
y.loc[y['order_weekday'] - y['order_weekday_one_month_ago'] <= 0, 'y_weekday'] = 0

y.loc[y['order_weekend'] - y['order_weekend_one_month_ago'] > 0, 'y_weekend'] = 1
y.loc[y['order_weekend'] - y['order_weekend_one_month_ago'] <= 0, 'y_weekend'] = 0

y.head(3)

# %%

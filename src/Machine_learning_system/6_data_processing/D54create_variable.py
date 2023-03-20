# %%
import pandas as pd

from D53basic_data_processing import order_data


def calc_delta(t):
    t1, t2 = t
    delta = t2 - t1
    return delta.total_seconds() / 60


# 配達時間計算
order_data['order_accept_datetime'] = pd.to_datetime(
    order_data['order_accept_date'])
order_data['delivered_datetime'] = pd.to_datetime(order_data['delivered_date'])
order_data['delta'] = order_data[
    ['order_accept_datetime', 'delivered_datetime']].apply(calc_delta, axis=1)

# 時間、曜日
order_data['order_accept_hour'] = order_data['order_accept_datetime'].dt.hour
order_data['order_accept_weekday'] = order_data['order_accept_datetime'].dt.weekday

order_data.loc[order_data['order_accept_weekday'] >= 5, 'weekday_info'] = '休日'
order_data.loc[order_data['order_accept_weekday'] < 5, 'weekday_info'] = '平日'

order_data.head(3)

# %%

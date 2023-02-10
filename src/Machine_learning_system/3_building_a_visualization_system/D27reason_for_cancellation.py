# %%
import pandas as pd

from D26build_from_story import order_all


def calc_delta(t):
    t1, t2 = t
    delta = t2 - t1
    return delta.total_seconds()/60


# order_all.loc[:, 'order_accept_datetime'] = pd.to_datetime(order_all['order_accept_date'])
order_all['order_accept_datetime'] = pd.to_datetime(
    order_all['order_accept_date'])
# order_all.loc[:, 'delivered_datetime'] = pd.to_datetime(order_all['delivered_date'])
order_all['delivered_datetime'] = pd.to_datetime(order_all['delivered_date'])
# order_all.loc[:, 'delta'] = order_all[['order_accept_datetime', 'delivered_datetime']].apply(calc_delta, axis=1)
order_all['delta'] = order_all[['order_accept_datetime',
                                'delivered_datetime']].apply(calc_delta, axis=1)

delivery_df = order_all.loc[(order_all['status'] == 2) & (
    order_all['store_id'].isin([8, 122]))]
delivery_df.groupby(['store_id'])['delta'].mean()

# %%

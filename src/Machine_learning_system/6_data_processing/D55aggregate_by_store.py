# %%
import pandas as pd

from D54create_variable import order_data


store_data = order_data.groupby(['store_name']).count()[['order_id']]
store_f = order_data.loc[
    (order_data['status_name'] == 'お渡し済') | (order_data['status_name'] == 'お支払済')].groupby(['store_name']).count()[['order_id']]
store_c = order_data.loc[
    order_data['status_name'] == 'キャンセル'].groupby(['store_name']).count()[['order_id']]
store_d = order_data.loc[
    order_data['takeout_name'] == 'デリバリー'].groupby(['store_name']).count()[['order_id']]
store_t = order_data.loc[
    order_data['takeout_name'] == 'お持ち帰り'].groupby(['store_name']).count()[['order_id']]

store_weekday = order_data.loc[
    order_data['weekday_info'] == '平日'].groupby(['store_name']).count()[['order_id']]
store_weekend = order_data.loc[
    order_data['weekday_info'] == '休日'].groupby(['store_name']).count()[['order_id']]

times = order_data['order_accept_hour'].unique()
store_time = []
for time in times:
    time_tmp = order_data.loc[order_data['order_accept_hour'] == time].groupby(
        ['store_name']).count()[['order_id']]
    time_tmp.columns = [f'order_time_{time}']
    store_time.append(time_tmp)
store_time = pd.concat(store_time, axis=1)
store_time.head(3)

store_delta = order_data.loc[(order_data['status_name'] != 'キャンセル')].groupby([
    'store_name']).mean()[['delta']]
store_data.columns = ['order']
store_f.columns = ['order_fin']
store_c.columns = ['order_cancel']
store_d.columns = ['order_delivery']
store_t.columns = ['order_takeout']
store_weekday.columns = ['order_weekday']
store_weekend.columns = ['order_weekend']
store_delta.columns = ['delta_avg']
store_data = pd.concat(
    [store_data,
     store_f,
     store_c,
     store_d,
     store_t,
     store_weekday,
     store_weekend,
     store_time,
     store_delta
     ], axis=1)

store_data.head(3)

# %%

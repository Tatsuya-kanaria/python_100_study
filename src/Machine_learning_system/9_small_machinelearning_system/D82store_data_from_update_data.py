# %%
import datetime
import os
import numpy as np
import pandas as pd

from D81folder_creation_and_initial_variables import master_dir, input_dir, m_area_file, m_store_file, target_file, tg_ym


m_area = pd.read_csv(os.path.join(master_dir, m_area_file))
m_store = pd.read_csv(os.path.join(master_dir, m_store_file))
target_data = pd.read_csv(os.path.join(input_dir, target_file))

max_date = pd.to_datetime(target_data["order_accept_date"]).max()
min_date = pd.to_datetime(target_data["order_accept_date"]).min()

max_str_date = max_date.strftime("%Y%m")
min_str_date = min_date.strftime("%Y%m")
if tg_ym == min_str_date and tg_ym == max_str_date:
    print("日付が一致しました")
else:
    raise Exception("日付が一致しません")


def calc_delta(t):
    t1, t2 = t
    delta = t2 - t1
    return delta.total_seconds() / 60


def count_by_column(df, column, value, new_column):
    count_df = df.loc[df[column] == value].groupby(
        ['store_name']).count()[['order_id']]
    count_df = count_df.rename(columns={'order_id': new_column})
    count_df = count_df.rename_axis('store_name')
    return count_df


def data_processing(order_data):
    order_data = order_data.loc[
        order_data['store_id'] != 999]

    merge_configs = [
        {'right': m_store, 'on': 'store_id', 'how': 'left'},
        {'right': m_area, 'on': 'area_cd', 'how': 'left'}
    ]
    for config in merge_configs:
        order_data = order_data.merge(**config)

    takeout_map = {0: 'デリバリー', 1: 'お持ち帰り'}
    order_data['takeout_name'] = order_data['takeout_flag'].map(takeout_map)

    status_map = {0: '受付', 1: 'お支払済', 2: 'お渡し済', 9: 'キャンセル'}
    order_data['status_name'] = order_data['status'].map(status_map)

    # 配達時間計算
    order_data['order_accept_datetime'] = pd.to_datetime(
        order_data['order_accept_date'])
    order_data['delivered_datetime'] = pd.to_datetime(
        order_data['delivered_date'])
    order_data['delta'] = order_data[
        ['order_accept_datetime', 'delivered_datetime']].apply(calc_delta, axis=1)

    # 時間、曜日
    order_data['order_accept_hour'] = order_data['order_accept_datetime'].dt.hour
    order_data['order_accept_weekday'] = order_data['order_accept_datetime'].dt.weekday

    order_data['weekday_info'] = np.where(
        order_data['order_accept_weekday'] >= 5, '休日', '平日')

    store_data = order_data.groupby(['store_name']).count()[['order_id']]
    store_data.columns = ['order']

    store_f = count_by_column(order_data, 'status_name', 'お渡し済', new_column='order_fin') + \
        count_by_column(order_data, 'status_name',
                        'お支払済', new_column='order_fin')

    store_c = count_by_column(
        order_data, 'status_name', 'キャンセル', new_column='order_cancel')
    store_d = count_by_column(
        order_data, 'takeout_name', 'デリバリー', new_column='order_delivery')
    store_t = count_by_column(
        order_data, 'takeout_name', 'お持ち帰り', new_column='order_takeout')
    store_weekday = count_by_column(
        order_data, 'weekday_info', '平日', new_column='order_weekday')
    store_weekend = count_by_column(
        order_data, 'weekday_info', '休日', new_column='order_weekend')

    times = order_data['order_accept_hour'].unique()
    store_time = []
    for time in times:
        time_tmp = order_data.loc[order_data['order_accept_hour'] == time].groupby(
            ['store_name']).count()[['order_id']]
        time_tmp.columns = [f'order_time_{time}']
        store_time.append(time_tmp)
    store_time = pd.concat(store_time, axis=1)

    store_delta = order_data.loc[(order_data['status_name'] != 'キャンセル')].groupby([
        'store_name']).mean(numeric_only=True)[['delta']]

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
    return store_data


store_data = data_processing(target_data)
store_data.reset_index(drop=False, inplace=True)
store_data['year_month'] = tg_ym
store_data.head(1)

# %%

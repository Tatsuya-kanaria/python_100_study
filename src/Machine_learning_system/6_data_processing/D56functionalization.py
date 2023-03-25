# %%
import os
import pandas as pd

from D51preparation_for_data_processing import master_dir, tbl_order_paths


m_area_file = 'm_area.csv'
m_store_file = 'm_store.csv'
m_area = pd.read_csv(os.path.join(master_dir, m_area_file))
m_store = pd.read_csv(os.path.join(master_dir, m_store_file))


def calc_delta(t):
    t1, t2 = t
    delta = t2 - t1
    return delta.total_seconds() / 60


def data_processing(order_data):
    order_data = order_data.loc[
        order_data['store_id'] != 999]
    order_data = pd.merge(
        order_data, m_store, on='store_id', how='left')
    order_data = pd.merge(
        order_data, m_area, on='area_cd', how='left')

    order_data.loc[
        order_data['takeout_flag'] == 0, 'takeout_name'] = 'デリバリー'
    order_data.loc[
        order_data['takeout_flag'] == 1, 'takeout_name'] = 'お持ち帰り'

    order_data.loc[
        order_data['status'] == 0, 'status_name'] = '受付'
    order_data.loc[
        order_data['status'] == 1, 'status_name'] = 'お支払済'
    order_data.loc[
        order_data['status'] == 2, 'status_name'] = 'お渡し済'
    order_data.loc[
        order_data['status'] == 9, 'status_name'] = 'キャンセル'

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

    order_data.loc[order_data['order_accept_weekday']
                   >= 5, 'weekday_info'] = '休日'
    order_data.loc[order_data['order_accept_weekday']
                   < 5, 'weekday_info'] = '平日'

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

    store_delta = order_data.loc[(order_data['status_name'] != 'キャンセル')].groupby([
        'store_name']).mean(numeric_only=True)[['delta']]
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
    return store_data


if __name__ == '__main__':
    tbl_order_path = tbl_order_paths[0]
    print(f'読み込みデータ:{tbl_order_path}')
    order_data = pd.read_csv(tbl_order_path)
    store_data = data_processing(order_data)
    store_data.head(3)

# %%

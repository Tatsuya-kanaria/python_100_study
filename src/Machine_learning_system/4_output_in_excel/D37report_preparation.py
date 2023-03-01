# %%
from D31output_in_excel import order_all, m_store, store_df

import pandas as pd


# キャンセル率ランキングデータを準備
cancel_df = pd.DataFrame()
cancel_cnt = order_all.loc[order_all['status'] == 9].groupby(['store_id'])[
    'store_id'].count()
order_cnt = order_all.loc[order_all['status'].isin(
    [1, 2, 9])].groupby(['store_id'])['store_id'].count()
cancel_rate = (cancel_cnt / order_cnt) * 100
cancel_df['cancel_rate'] = cancel_rate
cancel_df = pd.merge(cancel_df, m_store, on='store_id', how='left')
cancel_rank = cancel_df.sort_values(
    'cancel_rate', ascending=True).reset_index()


def calc_delta(t):
    t1, t2 = t
    delta = t2 - t1
    return delta.total_seconds() / 60


def check_store_cancel_rank(trg_id):
    tmp = cancel_rank.loc[cancel_rank['store_id'] == trg_id].index + 1
    return tmp[0]


def get_area_df(trg_id):
    # 該当店舗が属する、地域別データの集計と売上ランク
    area_df = pd.DataFrame()
    area_df = order_all.loc[
        order_all['area_cd'] == store_df['area_cd'].unique()[0]]
    area_df = area_df.loc[
        area_df['status'].isin([1, 2])]

    return area_df


def get_area_rank_df(trg_id):
    area_df = get_area_df(trg_id)
    area_rank = area_df.groupby(
        ['store_id'])['total_amount'].sum().sort_values(ascending=False)
    area_rank = pd.merge(
        area_rank, m_store, on='store_id', how='left')

    return area_rank


def check_store_sales_rank(trg_id):
    area_rank = get_area_rank_df(trg_id)

    tmp = area_rank.loc[area_rank['store_id'] == trg_id].index + 1
    return tmp[0]


def make_store_daily(trg_id):
    # 該当店舗の日毎売上データ
    tmp_store_df = order_all.loc[
        (order_all['store_id'] == trg_id) & (order_all['status'].isin([1, 2]))]
    tmp = tmp_store_df[
        ['order_accept_date', 'total_amount']].copy()
    tmp['order_accept_date'] = pd.to_datetime(tmp['order_accept_date'])
    tmp.set_index('order_accept_date', inplace=True)
    tmp = tmp.resample('D').sum().reset_index()

    return tmp


def get_area_delivery(trg_id):
    # 該当店舗が属する、地域別データの配達完了までの時間ランク
    area_delivery = pd.DataFrame()
    area_df = get_area_df(trg_id)
    area_delivery = area_df.loc[area_df['status'] == 2].copy()

    area_delivery['order_accept_datetime'] = pd.to_datetime(
        area_delivery['order_accept_date'])
    area_delivery['delivered_datetime'] = pd.to_datetime(
        area_delivery['delivered_date'])
    area_delivery['delta'] = area_delivery[[
        'order_accept_datetime', 'delivered_datetime']].apply(calc_delta, axis=1)

    return area_delivery


def get_area_delivery_rank_df(trg_id):
    area_delivery = get_area_delivery(trg_id)
    area_delivery_rank = area_delivery.groupby(
        ['store_id'])['delta'].mean().sort_values()
    area_delivery_rank = pd.merge(
        area_delivery_rank, m_store, on='store_id', how='left')

    return area_delivery_rank


def check_store_delivery_rank(trg_id):
    area_delivery_rank = get_area_delivery_rank_df(trg_id)

    tmp = area_delivery_rank.loc[
        area_delivery_rank['store_id'] == trg_id].index + 1

    return tmp[0]

# %%

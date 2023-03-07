# %%
from D41basic_folder_generation import master_dir, input_dir

import os
import datetime
import pandas as pd


m_area_file = "m_area.csv"
m_store_file = "m_store.csv"
m_area = pd.read_csv(os.path.join(master_dir, m_area_file))
m_store = pd.read_csv(os.path.join(master_dir, m_store_file))
m_area.head(3)

tg_ym = "202007"
target_file = "tbl_order_" + tg_ym + ".csv"
target_data = pd.read_csv(os.path.join(input_dir, target_file))

max_date = pd.to_datetime(target_data["order_accept_date"]).max()
min_date = pd.to_datetime(target_data["order_accept_date"]).min()
max_str_date = max_date.strftime("%Y%m")
min_str_date = min_date.strftime("%Y%m")
if tg_ym == min_str_date and tg_ym == max_str_date:
    print('日付が一致しました')
else:
    raise Exception('日付が一致しません')


def calc_delta(t):
    t1, t2 = t
    delta = t2 - t1
    return delta.total_seconds() / 60


def init_tran_df(trg_df):
    # 保守用店舗データの削除
    trg_df = trg_df.loc[trg_df['store_id'] != 999]

    trg_df = pd.merge(trg_df, m_store, on='store_id', how='left')
    trg_df = pd.merge(trg_df, m_area, on='area_cd', how='left')

    # マスターにないコードに対応した文字列を設定
    takeout_name_dict = {
        0: 'デリバリー',
        1: 'お持ち帰り',
    }

    status_name_dict = {
        0: '受付',
        1: 'お支払済み',
        2: 'お渡し済み',
        9: 'キャンセル'
    }

    def set_str(dict, flag_name):
        for flag, name in dict.items():
            trg_df.loc[trg_df[flag_name] == flag,
                       flag_name.replace('_flag', '') + '_name'] = name

    set_str(takeout_name_dict, 'takeout_flag')
    set_str(status_name_dict, 'status')

    trg_df['order_date'] = pd.to_datetime(trg_df['order_accept_date']).dt.date

    # 配達までの時間を計算
    trg_df['order_accept_datetime'] = pd.to_datetime(
        trg_df['order_accept_date'])
    trg_df['delivered_datetime'] = pd.to_datetime(trg_df['delivered_date'])
    trg_df['delta'] = trg_df[['order_accept_datetime',
                              'delivered_datetime']].apply(calc_delta, axis=1)

    return trg_df


# 当月分を初期化
target_data = init_tran_df(target_data)

# %%

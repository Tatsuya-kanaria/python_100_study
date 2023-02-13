# %%
from D27reason_for_cancellation import order_all

import datetime
from IPython.display import display, clear_output
from ipywidgets import ToggleButtons, Dropdown, DatePicker
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
# missing from current font対策
import matplotlib.font_manager

# データ読込
m_store = pd.read_csv('./data/m_store.csv')
m_area = pd.read_csv('./data/m_area.csv')

# 環境変数
target_store = ""
min_date = datetime.date(2020, 4, 1)
max_date = datetime.date(2020, 4, 30)
area_list = m_area['wide_area'].unique()
store_list = m_store['store_name'].tolist()


def make_board():
    clear_output()
    display(toggle_db)

    # データ作成処理
    pick_order_data = order_all.loc[(
        order_all['store_name'] == target_store
    ) & (
        order_all['order_date'] >= min_date
    ) & (
        order_all['order_date'] <= max_date
    ) & (
        order_all['status'].isin([1, 2]))]

    pick_cancel_data = order_all.loc[(
        order_all['store_name'] == target_store
    ) & (
        order_all['order_date'] >= min_date
    ) & (
        order_all['order_date'] <= max_date
    ) & (
        order_all['status'].isin([9]))]

    pick_order_all = order_all.loc[(
        order_all['order_date'] >= min_date
    ) & (
        order_all['order_date'] <= max_date
    ) & (
        order_all['status'].isin([1, 2]))]

    pick_cancel_all = order_all.loc[(
        order_all['order_date'] >= min_date
    ) & (
        order_all['order_date'] <= max_date
    ) & (order_all['status'] == 9)]

    store_o_cnt = len(pick_order_data)
    store_c_cnt = len(pick_order_data['customer_id'].unique())
    store_cancel_rate = (len(pick_cancel_data) /
                         (len(pick_order_data) + len(pick_cancel_data))) * 100
    delivery_time = pick_order_data.loc[pick_order_data['status'] == 2]['delta'].mean(
    )
    delivery_time_all = pick_order_all.loc[pick_order_all['status'] == 2]['delta'].mean(
    )

    # 画面の描画処理
    temp = pick_order_data[['order_date', 'total_amount']].copy()
    temp['order_date'] = pd.to_datetime(temp['order_date'])
    temp.set_index('order_date', inplace=True)

    print("="*90)
    str_out = f"■■ {target_store} ■■ 【対象期間】: {min_date} ~ {max_date}"
    str_out = str_out + f"【オーダー件数】: {store_o_cnt} 件 【利用顧客数】: {store_c_cnt}"
    print(str_out)

    print("-"*90)
    print(f"■■■■■■ 日毎の売上 ■■■■■■")
    display(temp.resample('D').sum())
    print("-"*90)

    str_out = f"【期間売上総額】: {'{:,}'.format(temp['total_amount'].sum())}"
    str_out = str_out + \
        f"【キャンセル総額】: {'{:,}'.format(pick_cancel_data['total_amount'].sum())}"
    str_out = str_out + f"【キャンセル率】: {round(store_cancel_rate, 2)} %"
    print(str_out)

    str_out = f"【平均配達完了時間】: {round(delivery_time, 2)} 分"
    str_out = str_out + f"【全店舗平均配達時間】: {round(delivery_time_all, 2)} 分"
    print(str_out)
    print("-"*90)

    # グラグ作成処理
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    sns.histplot(temp.resample('D').sum(), ax=ax1, kde=False)
    ax1.set_title("売上(日単位)ヒストグラム")

    sns.countplot(x='order_date', data=pick_cancel_data, ax=ax2)
    ax2.set_title("キャンセル数（日単位）")

    fig, (ax3) = plt.subplots(1, 1, figsize=(20, 5))
    sns.boxplot(x="order_date", y="total_amount", data=pick_order_data)
    ax3.set_title("オーダー状況箱ひげ図")
    plt.show()

# カレンダー変更時の処理


def change_date_min(val):
    global min_date
    min_date = val['new']
    make_board()


def change_date_max(val):
    global max_date
    max_date = val['new']
    make_board()

# ドロップダウン変更時の処理


def change_dropdown(val):
    global target_store
    target_store = val['new']

    # 期間指定機能
    date_picker_min = DatePicker(value=min_date)
    date_picker_min.observe(change_date_min, names='value')
    print('期間')
    date_picker_max = DatePicker(value=max_date)
    date_picker_max.observe(change_date_max, names='value')
    display(date_picker_min, date_picker_max)

# 地域トグルボタン処理


def order_by_area(val):
    clear_output()
    display(toggle_db)
    # 選択された地域の店舗リストを作成する
    store_list = order_all.loc[order_all['wide_area']
                               == val['new']]['store_name'].unique()
    # 作成された店舗リストでドロップダウンを作成する
    dropdown = Dropdown(options=store_list)
    dropdown.observe(change_dropdown, names='value')
    display(dropdown)


# トグルボタンを表示
toggle_db = ToggleButtons(options=area_list)
toggle_db.observe(order_by_area, names='value')
display(toggle_db)

# %%

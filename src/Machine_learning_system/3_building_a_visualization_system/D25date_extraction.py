# %%
from ipywidgets import DatePicker
from IPython.display import display, clear_output
import pandas as pd
import datetime

from D21filter_and_visualize import order_data, m_area


order_data.loc[:, 'order_date'] = pd.to_datetime(order_data['order_accept_date']).dt.date

def order_by_date(val):
    clear_output()
    display(date_picker)
    pick_data = order_data.loc[(order_data['order_date'] == val['new']) & (order_data['status'].isin([1, 2]))]
    print(len(pick_data))
    display(pick_data.head())

date_picker = DatePicker(value=datetime.datetime(2020, 4, 1))
date_picker.observe(order_by_date, names='value')
display(date_picker)

min_date = datetime.date(2020, 4, 1)
max_date = datetime.date(2020, 4, 30)

# 期間が設定されたら呼ばれる関数、期間データを抽出し画面に表示
def order_between_date():
    clear_output()
    display(date_picker_min)
    display(date_picker_max)
    pick_data = order_data.loc[(order_data['order_date'] >= min_date) & (order_data['order_date'] <= max_date) & (order_data['status'].isin([1, 2]))]
    print(len(pick_data))
    display(pick_data.head())

# 最小日（期間自）の日付を変数にセットする関数
def set_min_date(val):
    global min_date
    min_date = val['new']
    order_between_date()

# 最大日（期間至）の日付を変数にセットする関数
def set_max_date(val):
    global max_date
    max_date = val['new']
    order_between_date()

date_picker_min = DatePicker(value=min_date)
date_picker_min.observe(set_min_date, names='value')
print('最小日付')
display(date_picker_min)

date_picker_max = DatePicker(value=max_date)
date_picker_max.observe(set_max_date, names='value')
print('最大日付')
display(date_picker_max)

# %%

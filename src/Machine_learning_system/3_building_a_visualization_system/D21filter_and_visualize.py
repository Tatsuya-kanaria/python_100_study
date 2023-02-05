# %%
from ipywidgets import Dropdown
from IPython.display import display, clear_output
import japanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline

m_store = pd.read_csv('./data/m_store.csv')
m_area = pd.read_csv('./data/m_area.csv')
order_data = pd.read_csv('./data/tbl_order_202004.csv')
order_data = pd.merge(order_data, m_store, on='store_id', how='left')
order_data = pd.merge(order_data, m_area, on='area_cd', how='left')

# マスターにないコードに対応した文字列を設定
order_data.loc[order_data['takeout_flag'] == 0, 'takeout_name'] = 'デリバリー'
order_data.loc[order_data['takeout_flag'] == 1, 'takeout_name'] = 'お待ち帰り'

order_data.loc[order_data['status'] == 0, 'status_name'] = '受付'
order_data.loc[order_data['status'] == 1, 'status_name'] = 'お支払済み'
order_data.loc[order_data['status'] == 2, 'status_name'] = 'お渡し済み'
order_data.loc[order_data['status'] == 9, 'status_name'] = 'キャンセル'

order_data.head()


def order_by_store(val):
    clear_output()
    display(dropdown)
    pick_data = order_data.loc[(order_data['store_name'] == val['new']) & (
        order_data['status'].isin([1, 2]))]
    display(pick_data.head())


store_list = m_store['store_name'].tolist()

dropdown = Dropdown(options=store_list)
dropdown.observe(order_by_store, names='value')
display(dropdown)


def graph_by_store(val):
    clear_output()
    display(dropdown2)
    pick_data = order_data.loc[(order_data['store_name'] == val['new']) & (
        order_data['status'].isin([1, 2]))]
    temp = pick_data[['order_accept_date', 'total_amount']].copy()
    temp.loc[:, 'order_accept_date'] = pd.to_datetime(
        temp['order_accept_date'])
    temp.set_index('order_accept_date', inplace=True)
    temp.resample('D').sum().plot()


dropdown2 = Dropdown(options=store_list)
dropdown2.observe(graph_by_store, names='value')
display(dropdown2)

# %%

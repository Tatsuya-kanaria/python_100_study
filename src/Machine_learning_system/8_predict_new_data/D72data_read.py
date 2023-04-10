# %%
import os
import datetime
import pandas as pd

from D71folder_generation import input_dir, master_dir


m_area_file = 'm_area.csv'
m_store_file = 'm_store.csv'

m_area = pd.read_csv(os.path.join(master_dir, m_area_file))
m_store = pd.read_csv(os.path.join(master_dir, m_store_file))

tg_ym = '202003'
target_file = "tbl_order_" + tg_ym + ".csv"
target_data = pd.read_csv(os.path.join(input_dir, target_file))

max_date = pd.to_datetime(target_data['order_accept_date']).max()
min_date = pd.to_datetime(target_data['order_accept_date']).min()
max_str_date = max_date.strftime("%Y%m")
min_str_date = min_date.strftime("%Y%m")
if tg_ym == min_str_date and tg_ym == max_str_date:
    print("日付が一致しました")
else:
    raise Exception("日付が一致しません")


# %%

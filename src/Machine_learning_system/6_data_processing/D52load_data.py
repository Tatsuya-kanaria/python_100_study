# %%
import os
import pandas as pd

from D51preparation_for_data_processing import master_dir, tbl_order_paths


m_area_file = 'm_area.csv'
m_store_file = 'm_store.csv'
m_area = pd.read_csv(os.path.join(master_dir, m_area_file))
m_store = pd.read_csv(os.path.join(master_dir, m_store_file))
m_area.head(3)

tbl_order_path = tbl_order_paths[0]
print(f'読み込みデータ：{tbl_order_path}')
order_data = pd.read_csv(tbl_order_path)
print(f'データ件数：{len(order_data)}')
order_data.head(3)

# %%

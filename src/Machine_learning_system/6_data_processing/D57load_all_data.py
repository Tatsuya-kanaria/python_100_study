# %%
import os
import pandas as pd
from IPython.core.display import display

from D51preparation_for_data_processing import output_dir, tbl_order_paths
from D56functionalization import data_processing


store_all = []
for tbl_order_path in tbl_order_paths:
    print(f'読み込みデータ:{tbl_order_path}')
    tg_ym = tbl_order_path.split('_')[-1][:6]
    order_data = pd.read_csv(tbl_order_path)
    store_data = data_processing(order_data)
    store_data['year_month'] = tg_ym
    store_data.reset_index(drop=False, inplace=True)
    store_all.append(store_data)

store_all = pd.concat(store_all, ignore_index=True)
display(store_all.head(3))
display(store_all.tail(3))
store_monthly_name = 'store_monthly_data.csv'
store_all.to_csv(os.path.join(output_dir, store_monthly_name), index=False)

# %%

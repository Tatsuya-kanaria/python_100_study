# %%
import pandas as pd
import os
import glob

# ファイルの読込
m_store = pd.read_csv('./data/m_store.csv')
m_area = pd.read_csv('./data/m_area.csv')

# オーダーデータの読込
current_dir = os.getcwd()
tbl_order_file = os.path.join(current_dir, './data/tbl_order_*.csv')
tbl_order_files = glob.glob(tbl_order_file)
order_all = pd.DataFrame()

for file in tbl_order_files:
    order_data = pd.read_csv(file)
    print(f'{file}:{len(order_data)}')
    order_all = pd.concat([order_all, order_data], ignore_index=True)

order_all

# 不要なデータを除外
order_data = order_all.loc[order_all['store_id'] != 999]

# マスタデータ結合
order_data = pd.merge(order_data, m_store, on='store_id', how='left')
order_data = pd.merge(order_data, m_area, on='area_cd', how='left')

# 名称を設定(お渡し方法)
order_data.loc[order_data['takeout_flag'] == 0, 'takeout_name'] = 'デリバリー'
order_data.loc[order_data['takeout_flag'] == 1, 'takeout_name'] = 'お持ち帰り'

# 名称を設定(注文状態)
order_data.loc[order_data['status'] == 0, 'status_name'] = '受付'
order_data.loc[order_data['status'] == 1, 'status_name'] = 'お支払済'
order_data.loc[order_data['status'] == 2, 'status_name'] = 'お渡し済'
order_data.loc[order_data['status'] == 9, 'status_name'] = 'キャンセル'

# ファイル出力
output_dir = os.path.join(current_dir, 'output_data')
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, 'order_data.csv')
order_data.to_csv(output_file, index=False)

# %%
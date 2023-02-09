# %%
from IPython.display import display, clear_output
import glob
import os
import pandas as pd


current_dir = os.getcwd()
tbl_order_file = os.path.join(current_dir, 'data/tbl_order_*.csv')
tbl_order_files = glob.glob(tbl_order_file)

m_store = pd.read_csv('./data/m_store.csv')
m_area = pd.read_csv('./data/m_area.csv')

order_all = pd.DataFrame()
for file in tbl_order_files:
    order_tmp = pd.read_csv(file)
    print(f'{file}:{len(order_tmp)}')
    order_all = pd.concat([order_all, order_tmp], ignore_index=True)

# 保守用店舗データの削除
order_all = order_all.loc[order_all['store_id'] != 999]

order_all = pd.merge(order_all, m_store, on='store_id', how='left')
order_all = pd.merge(order_all, m_area, on='area_cd', how='left')

# マスターにないコードに対応した文字列を設定
order_all.loc[order_all['takeout_flag'] == 0, 'takeout_name'] = 'デリバリー'
order_all.loc[order_all['takeout_flag'] == 1, 'takeout_name'] = 'お持ち帰り'

order_all.loc[order_all['status'] == 0, 'status_name'] = '受付'
order_all.loc[order_all['status'] == 1, 'status_name'] = 'お支払済み'
order_all.loc[order_all['status'] == 2, 'status_name'] = 'お渡し済み'
order_all.loc[order_all['status'] == 9, 'status_name'] = 'キャンセル'

order_all.loc[:, 'order_date'] = pd.to_datetime(
    order_all['order_accept_date']).dt.date

# order_all.groupby(['store_id', 'customer_id'])["total_amount"].describe()

summary_df = order_all.loc[order_all['status'].isin([1, 2])]
store_summary_df = summary_df.groupby(['store_id'])['total_amount'].sum()
store_summary_df = pd.merge(
    store_summary_df, m_store, on='store_id', how='left')
print('売上上位')
display(store_summary_df.sort_values('total_amount', ascending=False).head(10))
print('売上下位')
display(store_summary_df.sort_values('total_amount', ascending=True).head(10))

cancel_df = pd.DataFrame()
cancel_cnt = order_all.loc[order_all['status'] == 9].groupby(['store_id'])[
    'store_id'].count()
order_cnt = order_all.loc[order_all['status'].isin(
    [1, 2, 9])].groupby(['store_id'])['store_id'].count()
cancel_rate = (cancel_cnt / order_cnt) * 100
cancel_df["cancel_rate"] = cancel_rate
cancel_df = pd.merge(cancel_df, m_store, on='store_id', how='left')
print('キャンセル率が低い')
display(cancel_df.sort_values('cancel_rate', ascending=True).head(10))
print('キャンセル率が高い')
display(cancel_df.sort_values('cancel_rate', ascending=False).head())

# %%

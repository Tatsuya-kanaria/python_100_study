# %%
from D21filter_and_visualize import m_area, m_store
from D27reason_for_cancellation import order_all
from D28hypothesis_verification import check_df

from IPython.display import display, clear_output
import pandas as pd


cal_orders_base = order_all.loc[(order_all['status'].isin([1, 2]))]
# 地域のランキング（配達時間）
print("配達時間" + "=" * 17)
print("地域ランキング" + "-" * 17)
display(pd.DataFrame(cal_orders_base.groupby(
    ['narrow_area'])['delta'].mean().sort_values()))
print("地域毎のTOP5" + "-" * 17)
for area in m_area['area_cd']:
    temp = cal_orders_base.loc[cal_orders_base['area_cd'] == area]
    temp = temp.groupby(['store_id'])['delta'].mean().sort_values()
    temp = pd.merge(temp, m_store, on='store_id')[['store_name', 'delta']]
    display(temp.head())

# 地域のランキング（キャンセル率）
base_df = pd.merge(check_df, m_store, on='area_cd')
base_df = pd.merge(base_df, m_area, on='area_cd')
print("キャンセル率" + "=" * 17)
print("地域ランキング" + "-" * 17)
display(pd.DataFrame(base_df.groupby(['narrow_area'])[
        'cancel_rate'].mean().sort_values()))
print("地域毎のTOP5" + "-" * 17)
for area in m_area['area_cd']:
    temp = check_df.loc[check_df['area_cd'] == area]
    temp = temp.groupby(['store_id'])['cancel_rate'].mean().sort_values()
    temp = pd.merge(temp, m_store, on='store_id')[
        ['store_name', 'cancel_rate']]
    display(temp.head())

# %%

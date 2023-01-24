# %%
import pandas as pd


order_data = pd.read_csv('./data/order_data.csv')
if __name__ == '__main__':
    print(len(order_data))
order_data.head()

order_data = order_data.loc[
    (order_data['status'] == 1)
    | (order_data['status'] == 2)]
if __name__ == '__main__':
    print(len(order_data))
order_data.columns

analyze_data = order_data[[
    'store_id',
    'customer_id',
    'coupon_cd',
    'order_accept_date',
    'delivered_date',
    'total_amount',
    'store_name',
    'wide_area',
    'narrow_area',
    'takeout_name',
    'status_name',
]]
print(analyze_data.shape)
analyze_data.head()

# %%

# %%
import D4multiple_data_concat as D4


order_data = D4.order_all.loc[D4.order_all['store_id'] != 999]
order_data

order_data.isnull().sum()

order_data.describe()

order_data['total_amount'].describe()


# %%

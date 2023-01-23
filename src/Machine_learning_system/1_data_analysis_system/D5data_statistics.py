# %%
import D4multiple_data_concat as D4


D4.order_all.isnull().sum()

D4.order_all.describe()

D4.order_all['total_amount'].describe()
if __name__ == '__main__':
    print(D4.order_all['order_accept_date'].min())
    print(D4.order_all['order_accept_date'].max())
    print(D4.order_all['delivered_date'].min())
    print(D4.order_all['delivered_date'].max())

# %%

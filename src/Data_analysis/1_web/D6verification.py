# %%
import D5create_column  as D5
from D4merge2 import  join_data
from D2concat import transaction

if __name__ == '__main__':
    print(join_data['price'].sum)
    print(transaction['price'].sum)

join_data['price'].sum() == transaction['price'].sum()

# %%

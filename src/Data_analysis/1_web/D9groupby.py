# %%
import pandas as pd

import D5create_column as D5
import D8monthly_aggregation as D8
from D4merge2 import join_data

join_data.groupby(['payment_month', 'item_name']).sum()[['price', 'quantity']]

pd.pivot_table(join_data, index='item_name', columns='payment_month', values=[
               'price', 'quantity'], aggfunc='sum')

# %%

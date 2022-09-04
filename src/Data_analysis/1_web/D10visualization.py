# %%
import pandas as pd
import matplotlib.pyplot as plt

import D5create_column as D5
import D8monthly_aggregation as D8
from D4merge2 import join_data

graph_data = pd.pivot_table(join_data, index='payment_month',
                            columns='item_name', values='price', aggfunc='sum')
graph_data.head()

%matplotlib inline
for col_name in graph_data.columns.values:
    plt.plot(list(graph_data.index), graph_data[col_name], label=col_name)
plt.legend()

# %%

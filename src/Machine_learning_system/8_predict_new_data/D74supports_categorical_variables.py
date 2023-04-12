# %%
import pandas as pd

from D73aggregation_by_store import store_data


category_data = pd.get_dummies(
    store_data['store_name'], prefix='store', prefix_sep='_')
del category_data['store_麻生店']
store_data = pd.concat([store_data, category_data], axis=1)

store_data.head(3)

# %%

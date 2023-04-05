# %%
import pandas as pd
from IPython.core.display import display

from D61data_read import ml_data

category_data = pd.get_dummies(
    ml_data['store_name'], prefix='store', prefix_sep='_')

display(category_data.head(3))

del category_data['store_麻生店']
del ml_data['year_month']
del ml_data['store_name']
ml_data = pd.concat([ml_data, category_data], axis=1)
ml_data.columns

# %%

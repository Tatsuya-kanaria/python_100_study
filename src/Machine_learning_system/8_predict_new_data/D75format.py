# %%
import os
import pandas as pd

from D71folder_generation import model_dir
from D74supports_categorical_variables import store_data


X_cols_name = 'X_cols.csv'
X_cols = pd.read_csv(os.path.join(model_dir, X_cols_name))
X_cols = X_cols['X_cols']

X = store_data[X_cols].copy()

X.head(3)

# %%

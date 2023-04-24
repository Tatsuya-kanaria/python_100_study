# %%
import os
import pandas as pd
import pickle

from D81folder_creation_and_initial_variables import model_dir
from D82store_data_from_update_data import store_data


category_data = pd.get_dummies(
    store_data['store_name'], prefix='store', prefix_sep='_')
del category_data['store_麻生店']
store_data = pd.concat([store_data, category_data], axis=1)

X_cols_name = 'X_cols.csv'
X_cols = pd.read_csv(os.path.join(model_dir, X_cols_name))
X_cols = X_cols['X_cols']

X = store_data[X_cols].copy()

model_weekday_name = 'model_y_weekday_GradientBoosting.pickle'
model_weekend_name = 'model_y_weekend_GradientBoosting.pickle'

model_weekday_path = os.path.join(model_dir, model_weekday_name)
model_weekend_path = os.path.join(model_dir, model_weekend_name)

with open(model_weekday_path, mode='rb') as f:
    model_weekday = pickle.load(f)

with open(model_weekend_path, mode='rb') as f:
    model_weekend = pickle.load(f)

# %%

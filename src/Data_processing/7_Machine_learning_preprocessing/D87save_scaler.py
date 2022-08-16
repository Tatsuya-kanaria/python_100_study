
# %%

import pickle
import os

import D86scaling2 as D86


path = './data/scalers/'

os.makedirs(path, exist_ok=True)

for name, scaler in zip(D86.cols_name, D86.scaler_list):
    filepath = os.path.join(path, name + '_scaler.pkl')
    with open(filepath, mode='wb') as f:
        pickle.dump(scaler, f)


os.listdir('./data/scalers')

with open('./data/scalers/age_scaler.pkl', mode='rb') as f:
    age_scaler = pickle.load(f)

age_scaled = D86.test_ds.copy()
age_scaled['age'] = age_scaler.transform(
    age_scaled['age'].values.reshape(-1, 1))

age_scaled.head()

# %%

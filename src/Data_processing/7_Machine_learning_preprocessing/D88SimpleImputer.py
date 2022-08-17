
# %%

from sklearn.impute import SimpleImputer
import os
import pickle

import D86scaling2 as D86

# 中央値を指定して欠損値補完
age_imputer = SimpleImputer(strategy='median')
D86.train_ds['age'] = age_imputer.fit_transform(
    D86.train_ds['age'].values.reshape(-1, 1))

# 欠損値の確認
D86.train_ds.isna().sum()

os.makedirs('./data/imputers/', exist_ok=True)
with open('./data/imputers/age_imputer.pkl', mode='wb') as f:
    pickle.dump(age_imputer, f)

os.listdir('./data/imputers/')

# %%

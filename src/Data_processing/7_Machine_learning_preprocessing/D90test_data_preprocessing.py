# %%

from sklearn.model_selection import train_test_split
import seaborn as sns
import pandas as pd
import os
import pickle

import D86scaling2 as D86

# テストデータ

# データの読み込み
dataset = sns.load_dataset('titanic')

# 目的変数 生還したかどうかを分析する
label = dataset.pop('survived')

train_ds, test_ds, train_label, test_label = train_test_split(
    dataset, label, random_state=2021, stratify=label)

# テストデータの不要項目を削除
test_ds.drop(columns=['embark_town', 'alive'], inplace=True)

# カテゴリカル変数に変換
test_ds = pd.get_dummies(test_ds)
test_ds = pd.get_dummies(test_ds, columns=['pclass'])
test_ds.replace({True: 1, False: 0}, inplace=True)


# カラム違いの解消
test_ds = test_ds.merge(D86.train_ds, how='left')
test_ds = test_ds[D86.train_ds.columns]

cols_name = test_ds.columns[:4]

dict_ = {}
path = './data/scalers/'
for filename in os.listdir(path):
    with open(os.path.join(path, filename), mode='rb') as f:
        dict_.update({os.path.splitext(filename)[0]: pickle.load(f)})

for key, value in dict_.items():
    test_ds[key.replace('_scaler', '')] = value.transform(
        test_ds[key.replace('_scaler', '')].values.reshape(-1, 1))

with open('./data/imputers/age_imputer.pkl', mode='rb') as f:
    age_imputer = pickle.load(f)

test_ds['age'] = age_imputer.transform(test_ds.age.values.reshape(-1, 1))

test_ds

# %%

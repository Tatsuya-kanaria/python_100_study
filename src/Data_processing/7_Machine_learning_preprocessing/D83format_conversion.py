# %%

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import pandas as pd

# データの読み込み
dataset = sns.load_dataset('titanic')

# 目的変数 生還したかどうかを分析する
label = dataset.pop('survived')

train_ds, test_ds, train_label, test_label = train_test_split(
    dataset, label, random_state=2021, stratify=label)

# 必要のないデータ（答え）削除
train_ds.drop(columns=['embark_town', 'alive'], inplace=True)
train_ds.head()

# one_hot エンコーディング
one_hot_encoded = pd.get_dummies(train_ds)

# pclass カテゴリカルなデータなので変換
one_hot_encoded = pd.get_dummies(one_hot_encoded, columns=['pclass'])

# True, Falseはそのまま学習できない
one_hot_encoded = one_hot_encoded.replace({True: 1, False: 0})

one_hot_encoded.head()

train_ds = one_hot_encoded

# labelエンコーディング
# label_encoded = train_ds.copy()
# class_encoder = LabelEncoder()
# label_encoded['class'] = class_encoder.fit_transform(label_encoded['class'])
# label_encoded.head()

# %%

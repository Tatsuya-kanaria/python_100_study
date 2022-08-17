
# %%

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from scipy import stats
from sklearn.preprocessing import RobustScaler, StandardScaler
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

# iqr: 四分位範囲(25% ~ 75%)
q = train_ds.quantile([1 / 4, 3 / 4])
q1, q3 = q.loc[1 / 4], q.loc[3 / 4]
iqr = q3 - q1
# 外れ値  1.5iqr
mx = q3 + 1.5 * iqr
mn = q1 - 1.5 * iqr
# 外れ値の数
((train_ds > mx) | (train_ds < mn)).sum()

# 基本統計量確認
train_ds.describe()
cols_name = train_ds.columns[:4]

if __name__ == '__main__':
    fig, axes = plt.subplots(ncols=4, figsize=(20, 5))
    for i, col_name in enumerate(cols_name):
        axes[i].hist(train_ds[col_name])

# カラム四つめまでを辞書にする


def create_dict(arg_df):
    # {colum: {bins, bin_edges}}
    dict_ = {}
    base_df = arg_df.copy()
    for col_name in base_df.columns[:4]:
        df = base_df[col_name]

        bins, bin_edges = np.histogram(df.dropna(), bins="auto")

        keys = ['bins', 'bin_edges']
        values = [bins, bin_edges]

        dict_.update({col_name: dict(zip(keys, values))})
    return dict_


bins_dict = create_dict(train_ds)

for name, item in bins_dict.items():
    # print(name, item['bins'])
    stat, p = stats.chisquare(item['bins'])

    f1 = f'χ二乗検定のp値: {p}'
    result1 = f'一様性がある' if p >= 0.05 else f'一様性はない'
    # p >= 0.05 ではないので一様性はない

    stat, p = stats.shapiro(item['bins'])
    f2 = f'シャピロウィルク検定のp値: {p}'
    result2 = f'正規性がある' if p >= 0.05 else f'正規性はない'  # p >= 0.05 なので、正規性がある

    if __name__ == '__main__':
        print(name, f1, result1, f2, result2, sep='\n')
# 標準化（正規がある）
age_scaler = StandardScaler()
# ロバストスケーリング(正規でも一様でもない)
sibsp_scaler = RobustScaler()
parch_scaler = RobustScaler()
fare_scaler = RobustScaler()

scaler_list = [age_scaler, sibsp_scaler, parch_scaler, fare_scaler]

for name, scaler in zip(cols_name, scaler_list):
    # スケーリング
    train_ds[name] = scaler.fit_transform(train_ds[name].values.reshape(-1, 1))


if __name__ == '__main__':
    fig2, axes2 = plt.subplots(ncols=4, figsize=(20, 5))
    for i, col_name in enumerate(cols_name):
        axes2[i].hist(train_ds[col_name])


# %%


# %%

from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler


import D86scaling2 as D86

# 目的変数の件数を確認する
D86.train_label.value_counts()


# アンダーサンプリング

# ランダム抽出を固定
under_sampler = RandomUnderSampler(random_state=2021)

under_sampled_train_ds, under_sampled_train_label = under_sampler.fit_resample(
    D86.train_ds, D86.train_label)

# オーバーサンプリング

# ランダム抽出を固定
over_sampler = RandomOverSampler(random_state=2021)

over_sampled_train_ds, over_sampled_train_label = over_sampler.fit_resample(
    D86.train_ds, D86.train_label)

if __name__ == '__main__':
    under_sampled_train_ds.shape
    print('under:', under_sampled_train_label.value_counts(), sep='\n')

    over_sampled_train_ds.shape
    print('over:', over_sampled_train_label.value_counts(), sep='\n')

# %%

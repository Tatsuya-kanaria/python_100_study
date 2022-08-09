# %%

import seaborn as sns

# データの読み込み
dataset = sns.load_dataset('titanic')

# 目的変数 生還したかどうかを分析する
label = dataset.pop('survived')

if __name__ == '__main__':
    print(dataset)
    print(label)

# %%

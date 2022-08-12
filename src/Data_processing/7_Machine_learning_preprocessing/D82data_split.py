# %%

from sklearn.model_selection import train_test_split
import seaborn as sns

# データの読み込み
dataset = sns.load_dataset('titanic')

# 目的変数 生還したかどうかを分析する
label = dataset.pop('survived')

train_ds, test_ds, train_label, test_label = train_test_split(
    dataset, label, random_state=2021, stratify=label)

if __name__ == '__main__':
    print("train:", train_ds, sep='\n')
    print("test:", test_ds, sep='\n')

# %%

# %%
import D47sklearn_tree_withdrawal_model as D47

from sklearn.tree import DecisionTreeClassifier
import sklearn.model_selection
import pandas as pd


D47.results_test.head()

correct = len(
    D47.results_test.loc[D47.results_test["y_test"] == D47.results_test["y_pred"]])
data_count = len(D47.results_test)
score_test = correct / data_count
if __name__ == '__main__':
    print(score_test)

# 精度の評価（関数 .score）
if __name__ == '__main__':
    test_score = D47.model.score(D47.X_test, D47.y_test)
    train_score = D47.model.score(D47.X_train, D47.y_train)

    print(f'accuracy', f'test:{test_score:.2%}',
          f'train:{train_score:.2%}', sep="\n")
    # accuracy
    # test: 89.54%
    # train: 98.16%
    # train > test 過学習傾向にある

X = pd.concat([D47.exit, D47.conti], ignore_index=True)
y = X["is_deleted"]
del X["is_deleted"]
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
    X, y)

# max_depth : 決定木の深さ
model = DecisionTreeClassifier(random_state=0, max_depth=5)
model.fit(X_train, y_train)
if __name__ == "__main__":
    test_score = model.score(X_test, y_test)
    train_score = model.score(X_train, y_train)

    print(f'tuning accuracy', f'test:{test_score:.2%}',
          f'train:{train_score:.2%}', sep="\n")

# %%

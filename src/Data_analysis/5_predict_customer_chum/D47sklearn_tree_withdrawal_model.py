# %%
import D46get_dummies as D46

from sklearn.tree import DecisionTreeClassifier
import sklearn.model_selection
import pandas as pd


exit = D46.predict_data.loc[D46.predict_data["is_deleted"] == 1]

# .sample(len(exit)):比率が50：50になるように設定
conti = D46.predict_data.loc[D46.predict_data["is_deleted"] == 0].sample(
    len(exit))

X = pd.concat([exit, conti], ignore_index=True)
y = X["is_deleted"]
del X["is_deleted"]
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
    X, y)

model = DecisionTreeClassifier(random_state=0)
model.fit(X_train, y_train)
y_test_pred = model.predict(X_test)

if __name__ == '__main__':
    print(y_test_pred)


# 予測と実際の値をデータフレームに格納
results_test = pd.DataFrame({"y_test":y_test, "y_pred":y_test_pred})

results_test.head()

# %%

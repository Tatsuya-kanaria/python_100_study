# %%
import D36forecast_preparation as D36
import D37assigning_variables

import pandas as pd
# sklearn で線形回帰を行うためのライブラリ
import sklearn.model_selection
from sklearn import linear_model

# 2018/04以降
predict_data = D36.predict_data.loc[D36.predict_data["start_date"] >= pd.to_datetime(
    "20180401")]

# モデルの初期化
model = linear_model.LinearRegression()
# 予測に使うX
X = predict_data[["count_0", "count_1", "count_2",
                  "count_3", "count_4", "count_5", "period"]]
# 予測したいデータ
y = predict_data["count_pred"]

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
    X, y)

model.fit(X_train, y_train)
if __name__ == '__main__':
    print(model.score(X_train, y_train))
    print(model.score(X_test, y_test))

# %%

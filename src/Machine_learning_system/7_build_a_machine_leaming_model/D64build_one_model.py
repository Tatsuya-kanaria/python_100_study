# %%
from IPython.core.display import display
from sklearn.tree import DecisionTreeClassifier

from D63split_into_traning_and_testing import train_data, test_data


X_cols = list(train_data.columns)
X_cols.remove('y_weekday')
X_cols.remove('y_weekend')
target_y = 'y_weekday'
y_train = train_data[target_y]
X_train = train_data[X_cols]
y_test = test_data[target_y]
X_test = test_data[X_cols]
display(y_train.head(3))
display(X_train.head(3))

# 乱数種の固定
model = DecisionTreeClassifier(random_state=0)

# モデルの構築
model.fit(X_train, y_train)


# %%

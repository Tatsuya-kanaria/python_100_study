# %%
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score, confusion_matrix
import pandas as pd

from D64build_one_model import X_train, y_train, X_test, y_test, model


y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)
y_pred_test

acc_train = accuracy_score(y_train, y_pred_train)
acc_test = accuracy_score(y_test, y_pred_test)

f1_train = f1_score(y_train, y_pred_train)
f1_test = f1_score(y_test, y_pred_test)

recall_train = recall_score(y_train, y_pred_train)
recall_test = recall_score(y_test, y_pred_test)

precision_train = precision_score(y_train, y_pred_train)
precision_test = precision_score(y_test, y_pred_test)

print(f'【正解率】Train : {round(acc_train, 2)} Test : {round(acc_test, 2)}')
print(f'【F値】 Train : {round(f1_train, 2)} Test : {round(f1_test, 2)}')
print(f'【再現率】 Train : {round(recall_train,2)} Test : {round(recall_test,2)}')
print(
    f'【適合率】 Train : {round(precision_train, 2)} Test : {round(precision_test, 2)}')

# FP, FN が0になっていると過学習
print(confusion_matrix(y_train, y_pred_train))
print(confusion_matrix(y_test, y_pred_test))

tn_train, fp_train, fn_train, tp_train = confusion_matrix(
    y_train, y_pred_train).ravel()
tn_test, fp_test, fn_test, tp_test = confusion_matrix(
    y_test, y_pred_test).ravel()

print(f'【混同行列】 Train : {tn_train},{fp_train}, {fn_train}, {tp_train}')
print(f'【混同行列】 Test : {tn_test},{fp_test}, {fn_test}, {tp_test}')

score_train = pd.DataFrame(
    {
        'DataCategory': ['train'],
        'acc': [acc_train],
        'f1': [f1_train],
        'recall': [recall_train],
        'precision': [precision_train],
        'tp': [tp_train],
        'fn': [fn_train],
        'fp': [fp_train],
        'tn': [tn_train]
    }
)

score_test = pd.DataFrame(
    {
        'DataCategory': ['test'],
        'acc': [acc_test],
        'f1': [f1_test],
        'recall': [recall_test],
        'precision': [precision_test],
        'tp': [tp_test],
        'fn': [fn_test],
        'fp': [fp_test],
        'tn': [tn_test]
    }
)

score = pd.concat([score_train, score_test], axis=0, ignore_index=True)
score

# %%

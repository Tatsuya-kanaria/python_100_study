#
# %%
from sklearn.tree import DecisionTreeClassifier

from D64build_one_model import X_train, y_train, X_test, y_test


def make_model_and_eval(model, X_train, X_test, y_train, y_test):
    from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score, confusion_matrix
    from IPython.core.display import display
    import pandas as pd

    model.fit(X_train, y_train)
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    acc_train = accuracy_score(y_train, y_pred_train)
    acc_test = accuracy_score(y_test, y_pred_test)
    f1_train = f1_score(y_train, y_pred_train)
    f1_test = f1_score(y_test, y_pred_test)
    recall_train = recall_score(y_train, y_pred_train)
    recall_test = recall_score(y_test, y_pred_test)
    precision_train = precision_score(y_train, y_pred_train)
    precision_test = precision_score(y_test, y_pred_test)
    tn_train, fp_train, fn_train, tp_train = confusion_matrix(
        y_train, y_pred_train).ravel()
    tn_test, fp_test, fn_test, tp_test = confusion_matrix(
        y_test, y_pred_test).ravel()
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

    importance = pd.DataFrame(
        {'cols': X_train.columns, 'importance': model.feature_importances_})
    importance = importance.sort_values('importance', ascending=False)

    cols = pd.DataFrame({'X_cols': X_train.columns})
    display(score)

    return score, importance, model, cols


model = DecisionTreeClassifier(random_state=0)
score, importance, model, cols = make_model_and_eval(
    model, X_train, X_test, y_train, y_test)

# %%

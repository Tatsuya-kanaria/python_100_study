# %%
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from IPython.core.display import display
import os
import pandas as pd
import pickle

from D81folder_creation_and_initial_variables import tg_ym, output_ml_result_dir
from D85preprocessing_of_data import train_data, test_data


def make_model_and_eval(model, X_train, X_test, y_train, y_test):
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


X_cols = list(train_data.columns)
X_cols.remove('y_weekday')
X_cols.remove('y_weekend')
targets_y = ['y_weekday', 'y_weekend']

target_output_dir_name = f'results_{tg_ym}'
target_output_dir = os.path.join(output_ml_result_dir, target_output_dir_name)
os.makedirs(target_output_dir, exist_ok=True)
print(target_output_dir)

score_all = []
importance_all = []

for target_y in targets_y:
    y_train = train_data[target_y]
    X_train = train_data[X_cols]
    y_test = test_data[target_y]
    X_test = test_data[X_cols]

    models = {
        'tree': DecisionTreeClassifier(random_state=0),
        'RandomFores': RandomForestClassifier(random_state=0),
        'GradientBoosting': GradientBoostingClassifier(random_state=0)
    }

    for model_name, model in models.items():
        print(model_name)
        score, importance, model, cols = make_model_and_eval(
            model, X_train, X_test, y_train, y_test)
        score['model_name'] = model_name
        importance['model_name'] = model_name

        score['model_target'] = target_y
        importance['model_target'] = target_y

        model_name = f'model_{target_y}_{model_name}.pickle'
        model_path = os.path.join(target_output_dir, model_name)

        with open(model_path, mode='wb') as f:
            pickle.dump(model, f, protocol=2)

        score_all.append(score)
        importance_all.append(importance)

score_all = pd.concat(score_all, ignore_index=True)
importance_all = pd.concat(importance_all, ignore_index=True)
cols = pd.DataFrame({'X_cols': X_train.columns})

score_name = 'score.csv'
importance_name = 'importance.csv'
cols_name = 'X_cols.csv'

score_path = os.path.join(target_output_dir, score_name)
importance_path = os.path.join(target_output_dir, importance_name)
cols_path = os.path.join(target_output_dir, cols_name)

score_all.to_csv(score_path, index=False)
importance_all.to_csv(importance_path, index=False)
cols.to_csv(cols_path, index=False)

# %%

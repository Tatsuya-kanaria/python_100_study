# %%
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from IPython.core.display import display
import pandas as pd
import datetime
import os
import pickle

from D61data_read import output_dir
from D63split_into_traning_and_testing import train_data, test_data
from D67functionalization import make_model_and_eval


X_cols = list(train_data.columns)
X_cols.remove('y_weekday')
X_cols.remove('y_weekend')
targets_y = ['y_weekday', 'y_weekend']


now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

target_output_dir_name = 'result_' + now
target_output_dir = os.path.join(output_dir, target_output_dir_name)
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

if __name__ == '__main__':
    display(score_all.loc[score_all['model_target'] == 'y_weekday'])

    display(score_all.loc[score_all['model_target'] == 'y_weekend'])

importance_all.loc[(importance_all['model_target'] == 'y_weekday') & (
    importance_all['model_name'] == 'GradientBoosting')].head(10)

# %%

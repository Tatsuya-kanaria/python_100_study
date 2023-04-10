# %%
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
import pandas as pd
import datetime
import os
import pickle

from D61data_read import output_dir
from D64build_one_model import X_train, y_train, X_test, y_test
from D67functionalization import make_model_and_eval


models = {
    'tree': DecisionTreeClassifier(random_state=0),
    'RandomFores': RandomForestClassifier(random_state=0),
    'GradientBoostingClassifier': GradientBoostingClassifier(random_state=0)
}

now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

target_output_dir_name = 'result_' + now
target_output_dir = os.path.join(output_dir, target_output_dir_name)
os.makedirs(target_output_dir, exist_ok=True)
print(target_output_dir)

score_all = []
importance_all = []

for model_name, model in models.items():
    print(model_name)
    score, importance, model, cols = make_model_and_eval(
        model, X_train, X_test, y_train, y_test)
    score['model_name'] = model_name
    importance['model_name'] = model_name

    model_name = f'model_{model_name}.pickle'
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

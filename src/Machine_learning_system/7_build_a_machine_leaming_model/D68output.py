# %%
import pickle
import os
import datetime

from D61data_read import output_dir
from D67functionalization import score, importance, cols, model


now = datetime.datetime.now().strftime("%Y%m%d%H%M%s")
target_output_dir_name = "results_" + now
target_output_dir = os.path.join(output_dir, target_output_dir_name)
os.makedirs(target_output_dir, exist_ok=True)
print(target_output_dir)

score_name = 'score.csv'
importance_name = 'importance.csv'
cols_name = 'X_cols.csv'
model_name = 'model.pickle'

score_path = os.path.join(target_output_dir, score_name)
importance_path = os.path.join(target_output_dir, importance_name)
cols_path = os.path.join(target_output_dir, cols_name)
model_path = os.path.join(target_output_dir, model_name)

score.to_csv(score_path, index=False)
importance.to_csv(importance_path, index=False)
cols.to_csv(cols_path, index=False)
with open(model_path, mode='wb') as f:
    pickle.dump(model, f, protocol=2)

# %%

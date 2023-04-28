# %%
import os
import pandas as pd

from D91single_data_load import output_ml_result_dir


ml_results_dirs = os.listdir(output_ml_result_dir)
score_all = []
for ml_results_dir in ml_results_dirs:
    score_file_path = os.path.join(
        output_ml_result_dir, ml_results_dir, 'score.csv')
    score_monthly = pd.read_csv(score_file_path)
    score_monthly['dirs'] = ml_results_dir
    score_all.append(score_monthly)

score_all = pd.concat(score_all, ignore_index=True)

score_all['year_month'] = score_all['dirs'].str.split('_', expand=True)[1]

score_all.head()

# %%

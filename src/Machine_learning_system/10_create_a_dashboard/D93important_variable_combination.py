# %%
import os
import pandas as pd

from D91single_data_load import output_ml_result_dir


ml_results_dirs = os.listdir(output_ml_result_dir)
importance_all = []
for ml_results_dir in ml_results_dirs:
    importance_file_path = os.path.join(
        output_ml_result_dir, ml_results_dir, 'importance.csv')
    importance_monthly = pd.read_csv(importance_file_path)
    importance_monthly['dirs'] = ml_results_dir
    importance_all.append(importance_monthly)
importance_all = pd.concat(importance_all, ignore_index=True)
importance_all['year_month'] = importance_monthly['dirs'].str.split(
    '_', expand=True)[1]

importance_all.head()

# %%

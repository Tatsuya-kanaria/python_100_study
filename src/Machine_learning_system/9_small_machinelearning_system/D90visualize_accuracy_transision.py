# %%
import matplotlib.pyplot as plt
import os
import pandas as pd

from D81folder_creation_and_initial_variables import output_ml_result_dir


ml_result_dirs = os.listdir(output_ml_result_dir)
ml_result_dirs.sort()

score_all = []
for ml_results_dir in ml_result_dirs:
    score_file_path = os.path.join(
        output_ml_result_dir, ml_results_dir, 'score.csv')
    score_monthly = pd.read_csv(score_file_path)
    score_monthly['dirs'] = ml_results_dir
    score_all.append(score_monthly)

score_all = pd.concat(score_all, ignore_index=True)
score_all.head()

score_all_gb = score_all.loc[(score_all['model_name'] == 'GradientBoosting') & (
    score_all['DataCategory'] == 'test')]

model_targets = score_all_gb['model_target'].unique()

for model_target in model_targets:
    view_data = score_all_gb.loc[score_all_gb['model_target'] == model_target]
    plt.scatter(view_data['dirs'], view_data['acc'], label=model_target)

plt.legend(loc='center right')

# %%

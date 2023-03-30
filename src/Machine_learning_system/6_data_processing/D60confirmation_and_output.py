# %%
import os
from IPython.core.display import display

from D51preparation_for_data_processing import output_dir
from D59data_for_machineleaning import ml_data


ml_data.isna().sum()

display(ml_data.groupby('y_weekday').count()[['store_name']])
display(ml_data.groupby('y_weekend').count()[['store_name']])

ml_data.to_csv(os.path.join(output_dir, 'ml_base_data.csv'), index=False)

# %%

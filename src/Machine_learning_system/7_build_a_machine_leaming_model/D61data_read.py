# %%
import os
import pandas as pd


data_dir = 'data'
input_dir = os.path.join(data_dir, '0_input')
output_dir = os.path.join(data_dir, '1_output')

dirs = [input_dir, output_dir]

for dir in dirs:
    os.makedirs(dir, exist_ok=True)

ml_data_file = 'ml_base_data.csv'
ml_data = pd.read_csv(os.path.join(input_dir, ml_data_file))

ml_data.head(3)

# %%
